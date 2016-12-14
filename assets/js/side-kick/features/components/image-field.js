import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

import withFocus from '../mixins/focus';
import withState from 'flight-with-state';

var Logo = component( withFocus, withState, function application() {

    this.attributes({
        'field': '.field',
        'fieldName': '',
        'message': '.message',
        'choosenFileName': '.choosen-file-name'
    });

    this.after('initialize', function() {
        this.select('field').on( 'change', this.fieldChanged.bind(this) );

        // this.on( document, 'updateField_' + this.attr.fieldName + '_success', function() { console.log('Yay!'); });
        // this.on( document, 'updateField_' + this.attr.fieldName + '_error', function() { console.log('Nay!'); });
    });

    this.fieldChanged = function( event ) {

        var that = this,
            file = this.setFile( event.currentTarget );

        if ( 'empty' !== file.name ) {

            this.setChoosenFileName( file.name );

            this.getFileContent( file )
                .then(function( rawFile ) {

                    that.select('message')
                        .removeClass('red')
                        .html( 'Upload gif, jpg, and png only, up to 1MB.' );

                    that.trigger( document, 'updateField', {
                        name: that.attr.fieldName,
                        raw_image: rawFile,
                        value: file.name
                    });
                })
                .catch(function( errorMessage ) {

                    that.select('message')
                        .addClass('red')
                        .html( errorMessage );
                });
        }
    }

    this.setChoosenFileName = function( filename ) {
        this.select('choosenFileName').html( filename );
    }

    this.setFile = function( element ) {
        var file = new File([], 'empty');

        if ( !! element.files.length ) {
            file = element.files[0];
        }

        return file;
    }

    this.getFileContent = function( file ) {
        return new Promise( function ( resolve, reject ) {
            var fileReader = new FileReader();

            if ( ! isImageTypeMatches( file.type ) ) {
                reject('File type "' + file.type + '" doesn\'t supported.');
            } else if ( ! isImageSizeMatches( file.size ) ) {
                reject('File size greater than 1MB.');
            } else {
                fileReader.onload = function( event ) {
                    resolve( event.target.result );
                };

                fileReader.readAsDataURL( file );
            }

        } );
    }

    // check for image file type
    function isImageTypeMatches( imageType ) {
        return [
            'image/png',
            'image/gif',
            'image/jpg',
            'image/jpeg',
            'image/webp'
        ].indexOf( imageType ) !== -1;
    }

    // checking for image size to be greater than 1024KB.
    function isImageSizeMatches( imageSize ) {
        return imageSize < 1024000; // 1024KB
    }
});

export default Logo;