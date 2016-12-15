import $ from 'jquery';
import {
    UPDATE_LOGO,
    UPDATE_TITLE,
    UPDATE_SUB_TITLE,
    UPDATE_DESCRIPTION
} from '../constants';

$( window ).on( 'message onmessage', function receiveMessage( event ) {
    var data = event.originalEvent.data;

    if ( ! $.isEmptyObject( data ) ) {
        switch( data.name ) {
            case UPDATE_LOGO: handleLogo( data ); break;
            case UPDATE_TITLE: handleTitle( data ); break;
            case UPDATE_SUB_TITLE: handleSubTitle( data ); break;
            case UPDATE_DESCRIPTION: handleDescription( data ); break;
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

function handleTitle( data ) {
    $('.title').html( data.value );
}

function handleSubTitle( data ) {
    $('.sub-title').html( data.value );
}

function handleDescription( data ) {
    $('.description').html( data.value );
}