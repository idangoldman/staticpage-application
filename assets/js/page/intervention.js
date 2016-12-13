import $ from 'jquery';

$( window ).on( 'message onmessage', function receiveMessage( event ) {
    var message = event.originalEvent.data;

    if ( ! $.isEmptyObject( message ) ) {
        switch( message.type ) {
            case 'content_logo':
                console.log( message );
                break;
        }
    }
});