from openerp import api, fields, models, _

import logging

_logger = logging.getLogger(__name__)

class product_kit_version(models.Model):
	_name = 'product.kit.version'
	_description = 'Product Kit Version'
	_order = "product_kit_version"

	product_kit_version = fields.Char('Product Kit Version', required=True)

	@api.model
	def create(self):
		return super(product_kit_version, self).create(vals)

	@api.multi
	def write(self):
		return super(product_kit_version, self).write(vals)

class product_template(models.Model):
	_inherit = 'product.product'

	product_kit_version_id = fields.Many2many('product.kit.version', string='Product Kit Version',
	 help="Those categories are used to group similar products for internal kit version")

