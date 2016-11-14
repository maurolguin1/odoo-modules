# -*- coding: utf-8 -*-
# Copyright 2016 Critech Limited (contact@critech-services.com)
# License MIT (https://opensource.org/licenses/mit-license.php)

from . import models


def setup_default_code(cr, registry):
    cr.execute("""UPDATE sale_order_type SET code = substr(md5(random()::text), 1, 6) WHERE code IS NULL """)
    cr.execute("""ALTER TABLE sale_order_type ALTER COLUMN code SET NOT NULL""")

    return True
