/**
    Copyright 2016 Critech Limited (contact@critech-services.com)
    License MIT (https://opensource.org/licenses/mit-license.php)
*/

odoo.define('web_widget_unit.form_widgets', function (require) {
    "use strict";

    var core = require('web.core');
    var Model = require('web.Model');
    var FieldChar = core.form_widget_registry.get('char');
    var FieldMonetary = core.form_widget_registry.get('monetary');

    var unitMixin = {
        init: function() {
            this._super.apply(this, arguments);

            var unit_data = (this.options && this.options.unit) || this.field.unit;
            var self = this;

            if (unit_data && 'field' in unit_data && 'model' in unit_data) {
                this.field_manager.on("field_changed:" + unit_data.field, this, function() {
                    this.set({"unit_model": unit_data.model});
                    this.set({"unit_model_label": 'model_label' in unit_data ? unit_data.model_label : 'name'});

                    // Set unit_field at the end for ensure that previous values set are available in event handler
                    this.set({"unit_field": this.field_manager.get_field_value(unit_data.field)});
                });

                this.on("change:unit_field", this, this.get_unit);
            }
        },
        start: function() {
            var result = this._super();

            this.on("change:unit", this, function() {
                this.$el.addClass('oe_form_field_float');

                if (this.view.options.is_list_editable){
                    return;
                } else {
                    return this.reinitialize();
                }
            });

            return result;
        },
        get_unit: function() {
            if (this.get("unit_field")) {
                var self = this;
                var id = this.get('unit_field');
                var model = this.get('unit_model');
                var field = this.get('unit_model_label');

                new Model(model).call("read", [id], {'fields': [field]}).done(function(data) {
                    self.set({'unit': data[field]});
                });
            }
        },
    };

    FieldChar.include(jQuery.extend({}, {
        template: 'FieldCharWithUnit',
    }, unitMixin));

    FieldMonetary.include(jQuery.extend({}, {
        template: 'FieldMonetaryWithUnit',
    }, unitMixin));
});