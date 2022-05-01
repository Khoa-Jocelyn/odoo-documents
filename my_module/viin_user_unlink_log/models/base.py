from odoo import models, api, fields
from odoo.tools import config
import datetime
import json



class JSONEncoder(json.JSONEncoder):
 
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S")
        return super(JSONEncoder, self).default(obj)


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
        field_name_list = []
        # for field in ir_model_fields_recs:
        #     field_name_list.append(field.name)
        field_name_list = ir_model_fields_recs.mapped("name")
        return field_name_list

    def _prepare_unlink_log_vals(self):
        user_unlink_log_val_list = []
        field_name_list = self._get_track_field_unlink_ids()
        print(field_name_list)
        company_id = self.company_id.id if hasattr(self, 'company_id') and self.company_id else self.env.company.id
        for rec in self:
            record_infor_json = None
            if field_name_list:
                record_infor = {}
                for field_name in field_name_list:
                    record_infor[field_name] = getattr(rec, field_name)
                # record_infor = rec.read(field_name_list)
                # record_infor_json = json.dumps(record_infor, indent=1, cls=JSONEncoder)
                record_infor_json = record_infor
            model_record = self.env['ir.model'].sudo().search([('model', '=', rec._name)], limit=1)
            user_unlink_log_val_list.append({"user_id": self.env.user.id,
                                             "model_id": model_record.id,
                                             "res_id": rec.id,
                                             "datetime": fields.Datetime.now(),
                                             "res_name": rec.name,
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
