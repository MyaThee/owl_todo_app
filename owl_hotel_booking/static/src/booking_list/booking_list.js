/** @odoo-module */
import {Component,onWillStart,useRef,useState} from "@odoo/owl";

export class BookingList extends Component {
    static template = "owl_hotel_booking.BookingList";
    static props = {};

    setup(){
        // this.inputRef = useRef("input");
    }

    _today() {
        return new Date().toISOString().split("T")[0];
    }
}