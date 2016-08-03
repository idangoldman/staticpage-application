import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

var withImageUpload = function mixin() {
    function getFileContent( file ) {
        return new Promise( function ( resolve, reject ) {
            var fileReader = new FileReader();

            fileReader.onload = function( event ) {
                resolve( event.target.result );
            };

            if ( ! isImageTypeMatches( file.type ) ) {
                reject('File type "' + file.type + '" doesn\'t supported.');
            } else if ( ! isImageSizeMatches( file.size ) ) {
                reject('File size greater than 1024KB.');
            } else {
                fileReader.readAsDataURL( file );
            }

        } );
    }

    // set file name text
    function setFileName( $element, file ) {
        $element.parent().children('.file-name').html( file.name );
    }

    // check for image file type
    function isImageTypeMatches( imageType ) {
        return [
            'image/png',
            'image/gif',
            'image/jpg',
            'image/webp'
        ].indexOf( imageType ) !== -1;
    }

    // checking for image size to be greater than 1024KB.
    function isImageSizeMatches( imageSize ) {
        return imageSize < 1024000; // 1024KB
    }

    this.uploadImage = function( event ) {
        var $element = $( event.currentTarget ),
            that = this,
            $logoMessage = this.select('logoMessage');

        if ( !! $element[0].files.length ) {
            var file = $element[0].files[0];

            setFileName( $element, file );

            getFileContent( file )
                .then( function( result ) {
                    $logoMessage
                        .removeClass('red')
                        .html( 'Upload gif, jpg, and png only, up to 1MB.' );

                    that.trigger( $element, 'upload_image', { imageData: result } );
                })
                .catch( function( reason ) {
                    $logoMessage
                        .addClass('red')
                        .html( reason );
                });
        }
    }
};

export default withImageUpload;