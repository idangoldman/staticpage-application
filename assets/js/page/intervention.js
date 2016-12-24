import $ from 'jquery';
import StyleSheet from 'page/styles';
import {
    UPDATE_LOGO,
    UPDATE_TITLE,
    UPDATE_SUB_TITLE,
    UPDATE_DESCRIPTION,
    UPDATE_BACKGROUND_IMAGE,
    UPDATE_BACKGROUND_COLOR,
    UPDATE_BACKGROUND_REPEAT
} from 'page/constants';

var css = new StyleSheet('additional');

$( window ).on( 'message onmessage', function receiveMessage( event ) {
    var data = event.originalEvent.data;

    if ( ! $.isEmptyObject( data ) ) {
        switch( data.name ) {
            case UPDATE_LOGO: handleLogo( data ); break;
            case UPDATE_TITLE: handleTitle( data ); break;
            case UPDATE_SUB_TITLE: handleSubTitle( data ); break;
            case UPDATE_DESCRIPTION: handleDescription( data ); break;
            case UPDATE_BACKGROUND_IMAGE: handleBackgroundImage( data ); break;
            case UPDATE_BACKGROUND_COLOR: handleBackgroundColor( data ); break;
            case UPDATE_BACKGROUND_REPEAT: handleBackgroundRepeat( data ); break;
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

function handleTitle( { value } ) {
    $('.title').html( value );
}

function handleSubTitle( { value } ) {
    var text = htmlLineBreak( value );
    $('.sub-title').html( text );
}

function handleDescription( { value } ) {
    var text = htmlLineBreak( value );
    $('.description').html( text );
}

function handleBackgroundImage( { raw_file } ) {
    var css = new StyleSheet('additional');
    var propertyValue = '';

    if ( raw_file.length ) {
        propertyValue = ['url(', raw_file, ')'].join('');
    }

    css( '.background', 'backgroundImage', propertyValue );
}

function handleBackgroundColor( { value } ) {
    css( '.background', 'backgroundColor', value );
}

function handleBackgroundRepeat( { value } ) {
    css( '.background', 'backgroundRepeat', value );
}

function htmlLineBreak( text ) {
    return text.replace( /(?:\r\n|\r|\n)/g, '<br />' );
}