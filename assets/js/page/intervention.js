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
     var $logo = $('.logo');

     if ( $logo.length ) {
        $logo.attr( 'src', data.raw_image );
     } else {
        $('<img />')
            .addClass('logo')
            .attr( 'src', data.raw_image )
            .prependTo('.content');
     }
}