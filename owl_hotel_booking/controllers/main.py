from odoo import http
from odoo.http import request


class MainController(http.Controller):
    @http.route("/owl_hotel_booking", auth="public")
    def standalone_app(self):
        return request.render(
            'owl_hotel_booking.hotel_booking_app',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
            }
        )
