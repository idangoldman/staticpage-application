import $ from 'jquery';
import StyleSheet from 'page/styles';
import {
    UPDATE_LOGO,
    UPDATE_TITLE,
    UPDATE_SUB_TITLE,
    UPDATE_DESCRIPTION,
    UPDATE_BACKGROUND_IMAGE,
    UPDATE_BACKGROUND_COLOR,
    UPDATE_BACKGROUND_REPEAT,
    UPDATE_FONT_COLOR,
    UPDATE_BASE_FONT_SIZE,
    UPDATE_CONTENT_ALIGNMENT,
    UPDATE_CONTENT_DIRECTION
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
            case UPDATE_BASE_FONT_SIZE: handleBaseFontSize( data ); break;
            case UPDATE_FONT_COLOR: handleFontColor( data ); break;
            case UPDATE_CONTENT_ALIGNMENT: handleContentAlignmnet( data ); break;
            case UPDATE_CONTENT_DIRECTION: handleContentDirection( data ); break;
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
    var backgroundProperties = {
        'backgroundRepeat': value,
        'backgroundSize': 'cover'
    };

    if ( 'repeat' === value ) {
        backgroundProperties['backgroundSize'] = 'auto';
    }

    css( '.background', backgroundProperties, value );
}

function handleBaseFontSize( { value } ) {
    console.log('font size?');
    css( 'html', 'fontSize', value );
}

function handleFontColor( { value } ) {
    css( 'body, button, input, select, textarea', 'color', value );
}

function handleContentAlignmnet( { value } ) {
    var logoProperties = {
        'marginRight': 'auto',
        'marginLeft': 'auto'
    };

    if ( 'left' === value ) {
        logoProperties['marginLeft'] = 0;
    } else if ( 'right' === value ) {
        logoProperties['marginRight'] = 0;
    }

    css( '.page', 'textAlign', value );
    css( '.logo', logoProperties );
}

function handleContentDirection( { value } ) {
    css( 'body', 'direction', value );
}

function htmlLineBreak( text ) {
    return text.replace( /(?:\r\n|\r|\n)/g, '<br />' );
}