import $ from 'jquery';

$( window ).on( 'message onmessage', receiveMessage );

function receiveMessage( event ) {
    var message = event.originalEvent.data;

    if ( ! $.isEmptyObject( message ) ) {
        switch( message.type ) {
            case 'switchDeviceView':
                switchDeviceView( message.data );
                break;
            case 'updatePageContent':
                updatePageContent( message.data );
                break;
        }
    }
}

function updatePageContent( messageData ) {
    window.frames['page'].postMessage( messageData, '*' );
}

function switchDeviceView( { deviceType } ) {
    $('.page')
        .removeClass( function( index, css ) {
            return ( css.match(/\w+-view/g) || [] ).join(' ');
        })
        .addClass( deviceType + '-view');
}