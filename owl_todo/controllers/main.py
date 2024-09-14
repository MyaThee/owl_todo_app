from odoo import http
from odoo.http import request


class MainController(http.Controller):
    @http.route("/owl_todo", auth="public")
    def standalone_app(self):
        return request.render(
            'owl_todo.standalone_app',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
                # 'session_info': request.env['ir.http'].get_session_info(),
            }
        )
