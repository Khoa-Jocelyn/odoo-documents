# -*- coding: utf-8 -*-

from odoo import fields, models, api


class LibraryProducer(models.Model):
    _name = 'library.producer'
    _description = 'Library Producer'

    name = fields.Char(string="Name", required=True)
    infor = fields.Text(string="Information")
    book_ids = fields.One2many("library.book", "producer_id", string="Book")
    note = fields.Text(string="Note")


class LibraryProducerExtend(models.Model):
    _inherit = "library.producer"
    mobile = fields.Char(string="Mobile", group="group_manager")

    def update_mobile_number(self, new_number):
        self.ensure_one()
        self = self.sudo()
        self.mobile = new_number
    
    @api.model
    def name_create(self, name):
        return self.create({'title': name}).name_get()[0]
    #
    # def _compute_mobile(self):
    #     _query = """SELECT library_producer.id, regexp_replace('[^0-9]+','','g') 
    #     FROM library_producer WHERE library_producer.id in """ + str(tuple(self.ids))
    #     self.env.cr.execute(_query)
    #     producer_data = self.env.cr.dictfetchall()
    #     mapped_data = dict([
    #         (row['id'], {'mobile': row['mobile']}) for row in producer_data])
    #     for r in self:
    #         r.mobile = mapped_data.get(r.id, {}).get('mobile', False)
            
            
