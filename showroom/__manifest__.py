{
    'name': 'Showroom',
    'version': '1.0',
    'author': 'Kevin',
    'summary': 'Modul Showroom SIB UK Petra',
    'description': 'Showroom management module',
    'category': 'UAS',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base', 'sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/pembeli_views.xml',
        'views/pegawai_views.xml',
        'views/motor_views.xml',
        'views/sparepart_views.xml',
        'views/transaksi_views.xml'
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
