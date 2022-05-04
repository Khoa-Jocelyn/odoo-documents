from odoo import models, api, fields
from odoo.tools import config
import json


class Base(models.AbstractModel):
    _inherit = 'base'
        
    def unlink(self):
        self._generate_user_unlink_logs()
        return super(Base, self).unlink()
     
    @api.model
    def _can_log_user_unlink(self):
        return not isinstance(self, self.env['user.unlink.log'].__class__) \
            and not isinstance(self, models.TransientModel) \
            and self._name in config.options.get('track_user_unlink_whitelisted_models', []) \
            and self._auto == True
    
    def _get_track_field_unlink_ids(self):
        ir_model_recs = self.env["ir.model"].search([("track_user_unlink", "=", True), ("model", "=", self._name)])
        ir_model_fields_recs = ir_model_recs.mapped("track_field_unlink_ids")
        field_list = []
        for fields in ir_model_fields_recs:
            field = {"name": fields.name, "ttype": fields.ttype}
            field_list.append(field)
        return field_list
    
    def JSONEncoder(self, object_type, vals):
        if object_type in ["many2many", "one2many", "many2one"]:
            vals = [r.id for r in vals]
        elif object_type in ["date", "datetime"]:
            vals = fields.Datetime.to_string(vals)
        elif object_type in ["binary"]:
            vals = str(vals)
        return vals

    def _prepare_unlink_log_vals(self):
        user_unlink_log_val_list = []
        field_list = self._get_track_field_unlink_ids()
        company_id = self.company_id.id if hasattr(self, 'company_id') and self.company_id else self.env.company.id
        for rec in self:
            record_infor_json = None
            model_record = self.env['ir.model'].sudo().search([('model', '=', rec._name)], limit=1)
            if field_list:
                record_infor = {}
                for field in field_list:
                    record_infor[field["name"]] = getattr(rec, field["name"])
                    record_infor[field["name"]] = self.JSONEncoder(field["ttype"], record_infor[field["name"]])
                record_infor_json = json.dumps(record_infor, indent=1)
            else:
                record_infor_json = json.dumps({}, indent=1)
            user_unlink_log_val_list.append({"user_id": self.env.user.id,
                                             "model_id": model_record.id,
                                             "res_id": rec.id,
                                             "datetime": fields.Datetime.now(),
                                             "res_name": rec.display_name,
                                             "company_id": company_id,
                                             "record_infor": record_infor_json})
        return user_unlink_log_val_list
        
    def _generate_user_unlink_logs(self):
        user_unlink_log_val_list = []
        if self._can_log_user_unlink():
            if self._prepare_unlink_log_vals():
                user_unlink_log_val_list = self._prepare_unlink_log_vals()
        if user_unlink_log_val_list:
            self.env["user.unlink.log"].sudo().create(user_unlink_log_val_list)
        return self.env['user.unlink.log']
