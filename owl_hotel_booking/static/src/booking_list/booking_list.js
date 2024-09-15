/** @odoo-module */
import {Component,onWillStart,useState} from "@odoo/owl";

export class BookingList extends Component {
    static template = "owl_hotel_booking.BookingList";
    static props = {};

    setup(){
        console.log(this.props)
    }
}