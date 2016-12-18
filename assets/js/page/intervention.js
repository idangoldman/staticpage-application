import $ from 'jquery';
import {
    UPDATE_LOGO,
    UPDATE_TITLE,
    UPDATE_SUB_TITLE,
    UPDATE_DESCRIPTION,
    UPDATE_BACKGROUND_IMAGE
} from 'page/constants';

$( window ).on( 'message onmessage', function receiveMessage( event ) {
    var data = event.originalEvent.data;

    if ( ! $.isEmptyObject( data ) ) {
        switch( data.name ) {
            case UPDATE_LOGO: handleLogo( data ); break;
            case UPDATE_TITLE: handleTitle( data ); break;
            case UPDATE_SUB_TITLE: handleSubTitle( data ); break;
            case UPDATE_DESCRIPTION: handleDescription( data ); break;
            case UPDATE_BACKGROUND_IMAGE: handleBackgroundImage( data ); break;
        }
    }
});

function handleLogo( { raw_file } ) {
     var $logo = $('.logo');

     if ( $logo.length ) {
        if ( raw_file.length ) {
            $logo.attr( 'src', raw_file );
        } else {
            $logo.remove();
        }
     } else if ( ! $logo.length && raw_file.length ) {
        $('<img />')
            .addClass('logo')
            .attr( 'src', raw_file )
            .prependTo('.content');
     }
}

function handleTitle( data ) {
    $('.title').html( data.value );
}

function handleSubTitle( data ) {
    var text = htmlLineBreak( data.value );
    $('.sub-title').html( text );
}

function handleDescription( data ) {
    var text = htmlLineBreak( data.value );
    $('.description').html( text );
}

function handleBackgroundImage( { raw_file } ) {
    var image = '';

    if ( raw_file.length ) {
        image = ['url(', raw_file, ')'].join('');
    }

    $('.background').css( 'background-image', image );
}

function htmlLineBreak( text ) {
    return text.replace( /(?:\r\n|\r|\n)/g, '<br />' );
}