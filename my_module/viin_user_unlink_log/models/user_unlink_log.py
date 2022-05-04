from odoo import models, fields


class UserUnlinkLogs(models.Model):
    _name = 'user.unlink.log'
    _description = "User Unlink Logs"
    _rec_name = "res_name"
    model_id = fields.Many2one('ir.model', string='Model', readonly=True, index=True)
    res_model = fields.Char(string='Resource Model', related='model_id.model', store=True, index=True)
    res_id = fields.Integer(string='Document ID', required=True, readonly=True, index=True)
    res_name = fields.Char(string='Document Name', help="Display name of the related document.", required=True, readonly=True)
    datetime = fields.Datetime(string='Unlink Datetime', required=True, readonly=True, index=True)
    user_id = fields.Many2one('res.users', string='Unlink By User', required=True, readonly=True,index=True)
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, index=True)
    record_infor = fields.Text(string="Document  Information Unlinked", required=True, readonly=True)

