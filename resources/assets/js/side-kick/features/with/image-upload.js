import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var withImageUpload = function mixin() {
    function getFileContent( file ) {
        return new Promise( function ( resolve, reject ) {
            var fileReader = new FileReader();

            fileReader.onload = function( event ) {
                resolve( event.target.result );
            };

            fileReader.readAsDataURL( file );
        } );
    }

    this.uploadImage = function( event ) {
        var $element = $( event.currentTarget );

        if ( !! $element[0].files.length ) {
            var file = $element[0].files[0],
                imageTypes = [
                    'image/png',
                    'image/gif',
                    'image/jpg',
                    'image/webp'
                ],
                megabyte = 1024000;

            // set file name text
            $element
                .parent()
                    .children('.file-name').html( file.name );

            // check for image file type
            if ( imageTypes.indexOf( file.type ) === -1 ) {
                this.select('logoMessage')
                    .addClass('red')
                    .html(
                        'File type "' + file.type + '" doesn\'t supported.'
                    );

                return false;
            } else {
                this.select('logoMessage')
                    .removeClass('red')
                    .html(
                        'Upload gif, jpg, and png only, up to 1MB.'
                    );
            }

            // check for image size
            if ( file.size > megabyte ) {
                this.select('logoMessage')
                    .addClass('red')
                    .html(
                        'File size greater than 1024KB.'
                    );

                return false;
            } else {
                this.select('logoMessage')
                    .removeClass('red')
                    .html(
                        'Upload gif, jpg, and png only, up to 1MB.'
                    );
            }

            getFileContent( file ).then( function( content ) {
                console.log( content );
            });
        }
    }
};

export default withImageUpload;