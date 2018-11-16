import $ from 'jquery';
import { component } from 'flightjs';

let featuresData = window.featuresData;

let Storage = component(function Storage() {

    this.before('initialize', function() {
    });

    this.after('initialize', function() {
    });
});

Storage.attachTo( document );
