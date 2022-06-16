from odoo import models, fields, api, _

class transaksi(models.Model):
    _name = 'showroom.transaksi'
    _description = 'class untuk transaksi'
    _order = 'date desc'

    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    confirm_date = fields.Date('Confirm date')

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    id_transaksi = fields.Char('Number', size=64, required=True, index=True, readonly=True,
                             states={'draft': [('readonly', False)]})

    _sql_constraints = [('name_unik', 'unique(id_transaksi)', ('Ideas must be unique!'))]

    totall = fields.Integer('Total Harga', store=True, compute='_compute_total')

    date = fields.Date('Date Release', default=fields.Date.context_today, readonly=True)

    pembeli_id = fields.Many2one('showroom.pembeli', string='Pembeli', readonly=False, ondelete="cascade")

    pegawai_id = fields.Many2one('showroom.pegawai', string='Pegawai', readonly=False, ondelete="cascade")

    sparepart_id = fields.Many2one('showroom.sparepart', string='Sparepart', readonly=False, ondelete="cascade")

    jumlah = fields.Integer('Jumlah Barang', store=True, compute='_compute_jumlah')

    harga_motor = fields.Integer('Harga', related='motor_id.harga', readonly=True)

    detail_ids = fields.One2many('showroom.detail', 'id_transaksi', string='Detail Transaksi')

    motor_id = fields.Many2one('showroom.motor', string='Nama Motor', readonly=False, ondelete="cascade")

    # detail_id = fields.Many2one('showroom.detail', string='Nama Motor', readonly=False, ondelete="cascade")

    @api.depends("totall", "detail_ids.total")

    def _compute_total(self):
        for transaksi in self:
            val = {
                'totall': 0,
            }
            for rec in transaksi.detail_ids:
                val['totall'] += rec.total
            transaksi.update(val)

    @api.depends("jumlah", "detail_ids.jumlah_barang")

    def _compute_jumlah(self):
        for transaksi in self:
            val = {
                'jumlah': 0,
            }
            for rec in transaksi.detail_ids:
                val['jumlah'] += rec.jumlah_barang
            transaksi.update(val)

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'