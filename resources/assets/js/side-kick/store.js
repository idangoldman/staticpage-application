import { component } from 'imports?$=jquery!flightjs';
import withRequest from 'bower_components/flight-request/lib/with_request';

let data = window.initialData;

let Store = component( withRequest, function application() {

    this.after('initialize', function() {

        // distribute initial data
        this.trigger( document, 'initial.data', data );

        // catch upload image event
        this.on( document, 'upload_image', function( event, { imageData } ) {
            // console.log( event );
        } );
    });
});

export default Store;