from odoo import fields,models,api,_
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'estate.property'
    _description = "Estate Properties"

    name = fields.Char(string="Name", required = True)
    creation_date = fields.Date(string="Creation Date")
    code = fields.Integer(string="code", unique=True)
    city = fields.Char(string="city")
    is_available = fields.Boolean(string="availability",tracking=True)

    @api.model_create_multi
    def create(self,vals):
        for rec in vals:
            if not rec.get('creation_date'):
                rec['creation_date'] = fields.Date.today()
        return super(Property, self).create(vals) # use of create CRM

    @api.constrains('code')
    def _unique_check(self):
        for record in self:
            if self.search_count([('code', '=', record.code)]) > 1: # use of search count CRM
                raise ValidationError(_("code should be unique"))

    def write(self,vals):
        print(vals)

        # Using CRM to find the list of is_available = True
        available_property = self.env['estate.property'].search([  # use of search CRM
            ('is_available','=',True),]).mapped('name')            #use of mapped CRM

        print(available_property)

        punekars = available_property.filtered(lambda x:x.city =='pune') #use of filtered CRM

        print(punekars)

        return super(Property, self).write(vals)

    def unlink(self):#use of unlink CRM
        return super(Property, self).unlink()

    def copy(self, default=None):#use of copy CRM
        if default is None:
            default = {}
        default.update({
            'name': self.name + ' (copy)',
        })
        return super(Property, self).copy(default)












