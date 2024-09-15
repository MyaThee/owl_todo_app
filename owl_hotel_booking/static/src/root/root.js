/** @odoo-module */

import {Component, onWillStart, useState, useSubEnv} from "@odoo/owl";
import {BookingList} from "../booking_list/booking_list";

export class Root extends Component {
    static props = {};
    static template = "owl_hotel_booking.Root";
    static components = {BookingList};
    static props = {};

    setup() {
        this.state = useState({
        })
    }

}

