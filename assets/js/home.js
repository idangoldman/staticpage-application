import $ from 'jquery';

$( window ).on( 'message onmessage', receiveMessage );

function receiveMessage( event ) {
    var message = event.originalEvent.data;

    if ( ! $.isEmptyObject( message ) ) {
        switch( message.type ) {
            case 'switchDeviceView':
                switchDeviceView( message.data );
                break;
            case 'updateField':
                updateField( message.data );
                break;
        }
    }
}

function updateField( data ) {
    switch( data.name ) {
        case 'content_logo':
            window.frames['page'].postMessage( { type: data.name, rawImage: data.raw_image }, '*' );
            break;
    }
}

function switchDeviceView( { deviceType } ) {
    $('.page')
        .removeClass( function( index, css ) {
            return ( css.match(/\w+-view/g) || [] ).join(' ');
        })
        .addClass( deviceType + '-view');
}