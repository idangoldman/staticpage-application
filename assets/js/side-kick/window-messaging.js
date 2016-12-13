import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

let dataNames = ['content_logo'];

var windowMessaging = component( function() {
    this.after('initialize', function() {
        this.on( document, 'switchDeviceView', messagePost );
        this.on( document, 'updateField', updatePage );
    });

    function updatePage( event, data ) {
        if ( dataNames.indexOf( data.name ) !== -1 ) {
            messagePost( event, data );
        }
    }

    function messagePost( { type }, data ) {
        window.parent.postMessage( { type, data }, '*' );
    }
});

windowMessaging.attachTo( document );