{
    "name": "Owl ToDo",
    "depends": ["base", "web", "mail"],
    "license": "LGPL-3",
    "data": [
        'views/templates.xml',
        'views/menus.xml',
    ],
    "assets": {
        "web.assets_backend": [
        ],
        'owl_todo.assets_standalone_app': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'web/static/lib/odoo_ui_icons/*',
            'owl_todo/static/src/**/*',
        ],
        # "owl_todo.custom_assets": [
        #     'owl_todo/static/src/standalone_app/**/*.scss',
        # ],
    }
}
