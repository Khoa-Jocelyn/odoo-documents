from odoo import models, fields, api
from odoo import tools
from odoo.tools.sql import column_exists


class IrModel(models.Model):
    _inherit = 'ir.model'

    track_user_unlink = fields.Boolean(string='Track User Unlink')
    track_field_unlink_ids = fields.Many2many("ir.model.fields", string="Fields To Track When Unlink")

    @classmethod
    def _build_model(cls, pool, cr):
        ModelClass = super(IrModel, cls)._build_model(pool, cr)
        if column_exists(cr, 'ir_model', 'track_user_unlink'):
            cr.execute("""
            SELECT model FROM ir_model WHERE track_user_unlink = True 
            """)
            track_user_unlink_whitelisted_models = [row[0] for row in cr.fetchall()]
            tools.config.options['track_user_unlink_whitelisted_models'] = track_user_unlink_whitelisted_models
            print("tools.config.options: ", tools.config.options['track_user_unlink_whitelisted_models'])
        return ModelClass
    
    @api.model_create_multi
    @api.returns('self', lambda value:value.id)
    def create(self, vals_list):
        records = super(IrModel, self).create(vals_list)
        self._update_user_unlink_whitelisted_models_config()
        return records

    def write(self, vals):
        res = super(IrModel, self).write(vals)
        if 'track_user_unlink' in vals:
            self._update_user_unlink_whitelisted_models_config()
        return res

    def unlink(self):
        res = super(IrModel, self).unlink()
        self._update_user_unlink_whitelisted_models_config()
        return res

    @api.model
    def _update_user_unlink_whitelisted_models_config(self):
        ir_models = self.sudo().search([
            ('track_user_unlink', '=', True),
            ])
        tools.config.options['track_user_unlink_whitelisted_models'] = ir_models.mapped('model')
        
