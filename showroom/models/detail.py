from odoo import models, fields, api
#_ untuk translate

class detail(models.Model): #inherit dari Model -> ini nama class sesuai python
    _name = 'showroom.detail' #attribut dari class Model (lihat dokumen odoo) Modul.Model  jadi nama tabel
    # (ini nama class/tabel sesuai odoo), jadi kalau akses data berdasarkan nama ini
    _description = 'class untuk detail'
    _rec_name = 'id_detail' #default-nya name, ini untuk memberi tahu field mana yang jadi rec_name.
    _order = 'date desc' #defaultnya adalah id, pengaruhnya saat list view

    #membuat attribute field. Field ini punya common parameter

    id_detail = fields.Char('Number', size=64, required=True, index=True, readonly=False)

    date = fields.Date('Tanggal Detail', default=fields.Date.context_today, readonly=True)

    jumlah_barang = fields.Integer('Jumlah Barang', default=0, readonly=False)

    harga_motor = fields.Integer('Harga', related='motor_id.harga', readonly=True)

    total = fields.Integer('Total Harga', store=True, compute='_compute_total')

    id_transaksi = fields.Many2one('showroom.transaksi', string='Details', readonly=True, ondelete="cascade")

    motor_id = fields.Many2one('showroom.motor', string='Motor', readonly=False, ondelete="cascade")

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    # _sql_constraints = [('name_unik', 'unique(id_detail)', ('Ideas must be unique!'))]

    @api.depends('harga_motor', 'jumlah_barang')
    def _compute_total(self):
        for detail in self:
            val = {
                'total': 0,
            }
            for rec in detail:
                val['total'] = (rec.harga_motor * rec.jumlah_barang)
            detail.update(val)

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'

