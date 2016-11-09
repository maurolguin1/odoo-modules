# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from . import models


def setup_default_uom_so(cr, registry):
    cr.execute("""UPDATE product_template SET uom_so_id = uom_id WHERE uom_so_id IS NULL""")
    cr.execute("""ALTER TABLE product_template ALTER COLUMN uom_so_id SET NOT NULL""")

    return True
