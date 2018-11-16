import $ from 'jquery';
import { component } from 'flightjs';
import * as pageUpdateFields from 'page/constants';


var postMessaging = component( function() {
    this.after('initialize', function() {
        this.on( document, 'switchDeviceView', message );
        this.on( document, 'updateField', updatePage );
    });

    function message( event, data ) {
        var type = !! event.type ? event.type : event;

        window.parent.postMessage( { type, data }, '*' );
    }

    function updatePage( event, data ) {
        Object.keys(pageUpdateFields).forEach(function( key ) {
            if ( pageUpdateFields[ key ] === data.name ) {
                message( 'updatePageContent', data );
            }
        });
    }
});

postMessaging.attachTo( document );
