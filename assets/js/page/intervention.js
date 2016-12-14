import $ from 'jquery';
import { UPDATE_LOGO } from '../constants';

$( window ).on( 'message onmessage', function receiveMessage( event ) {
    var data = event.originalEvent.data;

    if ( ! $.isEmptyObject( data ) ) {
        switch( data.name ) {
            case UPDATE_LOGO: handleLogo( data ); break;
        }
    }
});

function handleLogo( data ) {
    console.log('legs are the new hands.');
}