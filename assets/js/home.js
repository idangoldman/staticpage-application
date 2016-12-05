import $ from 'jquery';

$( window ).on( 'message onmessage', receiveMessage );

function receiveMessage( event ) {
    console.log( event.originalEvent.data );
}