from odoo import models, fields, api, _
from datetime import date, timedelta

class HospitalPatient(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = "hospital.patient"
    _description = "Hospital Patient Model"

    name = fields.Char(string="Name")
    reference = fields.Char(string='Order Reference', required=True,
                            copy=False, readonly=True, default=lambda self: _('New'))
    age = fields.Integer(string='Age', tracking=True)
    dob = fields.Date(string="Date of Birth", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    active = fields.Boolean(string="Active", default=True)
    patient_seq = fields.Char(string="Patient No.", required=True,
                              copy=False,
                              readonly=True,
                              index=True,
                              default=lambda self: 'New')
    # notes = fields.Html('Note', sanitize_style=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done'),
                              ('cancel', 'Cancelled')],
                             default='draft', string="Status", tracking=True)
    patient_age = fields.Integer(string="Age", compute='_compute_age')
    address = fields.Char(string="Address")
    responsible_ID = fields.Many2one(comodel_name='res.partner', string="Responsible")
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count")
    image = fields.Binary(string="Patient Image")
    appointments_ids = fields.One2many('hospital.appointment', 'patient_ID', string="Appointments")

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_ID', '=', rec.id)])
            rec.appointment_count = appointment_count

    def _compute_age(self):
        """age calculation of patient"""
        for rec in self:
            rec.patient_age = False
            if rec.dob:
                rec.patient_age = (date.today() - rec.dob) // timedelta(days=365.2425)

    # Action_confirm_BTN function
    def action_confirm(self):
        print("Confirm Pressed")
        self.state = 'confirm'

    # Action_done_BTN function
    def action_done(self):
        self.state = 'done'

    # Action_draft_BTN function
    def action_draft(self):
        self.state = 'draft'

    # Action_cancel_BTN function
    def action_cancel(self):
        self.state = 'cancel'


    @api.model
    def create(self, vals):
        print("Create overrided")
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', _('New') == _('New')):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res
