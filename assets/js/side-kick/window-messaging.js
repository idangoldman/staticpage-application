import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var windowMessaging = component( function() {
    this.after('initialize', function() {
        this.on( document, 'switchDeviceView', post );
    });

    function post( { type }, data ) {
        // console.log( event.type, data );
        window.parent.postMessage( { type, data }, '*' );
    }
});

windowMessaging.attachTo( document );