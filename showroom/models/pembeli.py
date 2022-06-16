from odoo import models, fields, api
#_ untuk translate

class pembeli(models.Model): #inherit dari Model -> ini nama class sesuai python
    _name = 'showroom.pembeli' #attribut dari class Model (lihat dokumen odoo) Modul.Model  jadi nama tabel
    # (ini nama class/tabel sesuai odoo), jadi kalau akses data berdasarkan nama ini
    _description = 'class untuk pembeli'
    _rec_name = 'name' #default-nya name, ini untuk memberi tahu field mana yang jadi rec_name.

    id_pembeli = fields.Char('Number', size=64, required=True, index=True, readonly=False,)

    name = fields.Char('Nama Pembeli', size=64, required=True, index=True, readonly=False,)

    jenis_kelamin = fields.Selection([('pria', 'Pria'),
                             ('wanita', 'Wanita'),
                             ], 'Jenis Kelamin', required=True, readonly=False)

    umur = fields.Char('Umur', size=64, required=True, index=True, readonly=False,)

    alamat = fields.Char('Alamat', size=64, required=True, index=True, readonly=False,)

    # pembeli_id = fields.Many2one('showroom.transaksi', string='Transaksi', readonly=True, ondelete="cascade",
    #                           domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    _sql_constraints = [('name_unik', 'unique(id_pembeli)', ('Ideas must be unique!'))]

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
