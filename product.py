from openerp import api, fields, models, _

import logging

_logger = logging.getLogger(__name__)

class product_kit_version(models.Model):
	_name = 'product.kit.version'
	_description = 'Product Kit Version'
	_order = "name"

	name = fields.Char('Product Kit Version', required=True)

class product_template(models.Model):
	_inherit = 'product.template'
	_order = "product_kit_version_ids"

	def _get_default_product_kit_version(self):
		cr = self.pool.cursor()
		self.env
		return self.pool.get('product.kit.version').search(cr, self.env.uid, [])

	product_kit_version_ids = fields.Many2many('product.kit.version',
		'product_product_kit_version_rel','product_id','product_kit_version_id', 
		string='Product Kit Version',
	    help="Those categories are used to group similar products for internal kit version")

