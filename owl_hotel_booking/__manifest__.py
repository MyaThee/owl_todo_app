{
    "name": "Owl Hotel Booking",
    "depends": ["base", "web", "mail"],
    "license": "LGPL-3",
    "data": [
        'views/templates.xml',
        'views/menus.xml',
    ],
    "assets": {
        'owl_hotel_booking.assets_hotel_booking': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'owl_hotel_booking._assets_boostrap5'),
            ('include', 'web._assets_core'),
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'web/static/lib/odoo_ui_icons/*',
            'owl_hotel_booking/static/src/**/*',
        ],
        "owl_hotel_booking._assets_boostrap5": [
            "owl_hotel_booking/static/lib/bootstrap5/**/*",
        ],
    }
}
