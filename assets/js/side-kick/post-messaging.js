import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';
import { UPDATE_LOGO } from '../constants';

let pageUpdateFieldsFilter = [
    UPDATE_LOGO
];

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
        if ( pageUpdateFieldsFilter.indexOf( data.name ) !== -1 ) {
            message( 'updatePageContent', data );
        }
    }
});

postMessaging.attachTo( document );