import $ from 'jquery';
import * as C from 'page/constants';

import StyleSheet from 'page/styles';
var css = new StyleSheet('intervention'),
    additionalCSS = new StyleSheet('additional');

$( window ).on( 'message onmessage', function receiveMessage( event ) {
    var data = event.originalEvent.data;

    if ( ! $.isEmptyObject( data ) ) {
        switch( data.name ) {
            case C.UPDATE_LOGO: handleLogo( data ); break;
            case C.UPDATE_TITLE: handleTitle( data ); break;
            case C.UPDATE_SUB_TITLE: handleSubTitle( data ); break;
            case C.UPDATE_DESCRIPTION: handleDescription( data ); break;
            case C.UPDATE_BACKGROUND_IMAGE: handleBackgroundImage( data ); break;
            case C.UPDATE_BACKGROUND_COLOR: handleBackgroundColor( data ); break;
            case C.UPDATE_BACKGROUND_REPEAT: handleBackgroundRepeat( data ); break;
            case C.UPDATE_FONT_FAMILY: handleFontFamily( data ); break;
            case C.UPDATE_FONT_COLOR: handleFontColor( data ); break;
            case C.UPDATE_CONTENT_ALIGNMENT: handleContentAlignmnet( data ); break;
            case C.UPDATE_CONTENT_DIRECTION: handleContentDirection( data ); break;
            case C.UPDATE_ADDITIONAL_STYLES: handleAdditionalStyles( data ); break;
            case C.UPDATE_COUNT_DOWN_DATETIME: handleCountDownDatetime( data ); break;
            case C.UPDATE_COUNT_DOWN_TIMEZONE: handleCountDownTimezone( data ); break;
            case C.UPDATE_MAILING_LIST_SERVICE: handleMailingListService( data ); break;
            case C.UPDATE_MAILING_LIST_CTA_COLOR: handleMailingListCtaColor( data ); break;
            case C.UPDATE_MAILING_LIST_CTA_TEXT: handleMailingListCtaText( data ); break;
            case C.UPDATE_MAILING_LIST_PLACEHOLDER_TEXT: handleMailingListPlaceholderText( data ); break;
        }
    }
});

// http://shebang.brandonmintern.com/foolproof-html-escaping-in-javascript/
function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild( document.createTextNode( str ) );
    return div.innerHTML;
}

function htmlLineBreak( text ) {
    return text.replace( /(?:\r\n|\r|\n)/g, '<br />' );
}

function handleLogo( { base64 } ) {
     var $logo = $('.logo');

     if ( $logo.length ) {
        if ( base64.length ) {
            $logo.attr( 'src', base64 );
        } else {
            $logo.remove();
        }
    } else if ( ! $logo.length && base64.length ) {
        $('<img />')
            .addClass('logo')
            .attr( 'src', base64 )
            .prependTo('.content');
     }
}

function handleTitle( { value } ) {
    $('.title').html( escapeHtml( value ) );
}

function handleSubTitle( { value } ) {
    var text = htmlLineBreak( escapeHtml( value ) );
    $('.sub-title').html( text );
}

function handleDescription( { value } ) {
    var text = htmlLineBreak( escapeHtml( value ) );
    $('.description').html( text );
}

function handleBackgroundImage( { base64 } ) {
    var propertyValue = '';

    if ( base64.length ) {
        propertyValue = ['url(', base64, ')'].join('');
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

function handleFontFamily( { value } ) {
    var fontFamily = value.split(', ')[0],
        googleFonts = [
            "Arvo",
            "Lato",
            "Lora",
            "Merriweather",
            "Merriweather Sans",
            "Noticia Text",
            "Open Sans",
            "Playfair Display",
            "Roboto",
            "Source Sans Pro"
        ];

    if ( googleFonts.indexOf( fontFamily ) !== -1 ) {
        fontFamily = fontFamily.split(' ').join('+');
        css( '@import url("//fonts.googleapis.com/css?family=' + fontFamily + ':400,600,700,800&subset=latin");' );
    }

    css( 'body, button, input, select, textarea', 'fontFamily', value );
}

function handleFontColor( { value } ) {
    css( 'body, button, input, select, textarea', 'color', value );

    var placeholder = '.newsletter .email',
        placeholder_prefixes = [
            '::-webkit-input-placeholder',
            '::-moz-placeholder',
            ':-ms-input-placeholder',
            '::placeholder'
        ];

    for ( var index = 0; index < placeholder_prefixes.length; index++ ) {
        css( placeholder + placeholder_prefixes[ index ], 'color', value );
    }
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

function handleAdditionalStyles( { value } ) {
    $('.css-additional').html( escapeHtml( value ) );
}

function handleCountDownDatetime( { value } ) {
    if ( value.length ) {
        window.countDown.datetime = value;
        window.countDown.tick();
    } else {
        window.countDown.datetime = '';
        window.countDown.countDownTimeoutID = 0;
        window.countDown.node.style.display = 'none';
    }
}

function handleCountDownTimezone( { value } ) {
    var timezone = value.split('|').pop();

    window.countDown.timezone = timezone;
    window.countDown.tick();
}

function handleMailingListService( { value } ) {
    var displayValue = value.length ? 'block' : 'none';
    css( '.newsletter', 'display', displayValue );
}

function handleMailingListCtaColor( { value } ) {
    css('.newsletter .submit', {
        'background-color': value,
        'border-color': value
    });
}

function handleMailingListCtaText( { value } ) {
    $('.newsletter .submit').html( escapeHtml( value ) );
}

function handleMailingListPlaceholderText( { value } ) {
    $('.newsletter .email').attr( 'placeholder', escapeHtml( value ) );
}
