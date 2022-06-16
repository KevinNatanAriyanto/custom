from odoo import models, fields, api
#_ untuk translate

class detail(models.Model): #inherit dari Model -> ini nama class sesuai python
    _name = 'showroom.motor' #attribut dari class Model (lihat dokumen odoo) Modul.Model  jadi nama tabel
    # (ini nama class/tabel sesuai odoo), jadi kalau akses data berdasarkan nama ini
    _description = 'class untuk motor'
    _rec_name = 'name' #default-nya name, ini untuk memberi tahu field mana yang jadi rec_name.

    id = fields.Char('Number', size=64, required=True, index=True, readonly=False,)

    name = fields.Char('Nama Motor', size=64, required=True, index=True, readonly=False,)

    stok = fields.Integer('Stok', default=0, readonly=False,)

    # motor_id = fields.Many2one('showroom.transaksi', string='Nama Motor', readonly=True, ondelete="cascade",
    #                              domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    warna = fields.Char('Warna', size=64, required=True, index=True, readonly=False, )

    harga = fields.Integer('Harga Motor', default=0, readonly=False)

    _sql_constraints = [('name_unik', 'unique(id_motor)', ('Ideas must be unique!'))]

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'

