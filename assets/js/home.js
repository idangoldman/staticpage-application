import $ from 'jquery';

$( window ).on( 'message onmessage', receiveMessage );

function receiveMessage( event ) {
    var message = event.originalEvent.data;

    if ( ! $.isEmptyObject( message ) ) {
        switch( message.type ) {
            case 'switchDeviceView':
                switchDeviceView( message.data );
                break;
        }
    }
}

function switchDeviceView( { deviceType } ) {
    $('.page')
        .removeClass( function( index, css ) {
            return ( css.match(/\w+-view/g) || [] ).join(' ');
        })
        .addClass( deviceType + '-view');
}