import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

import withFocus from '../mixins/focus';
import withState from 'flight-with-state';

var fileField = component( withFocus, withState, function application() {

    this.attributes({
        'field': '.field',
        'fieldName': null,
        'message': '.message',
        'error': '.error',
        'choosenFileName': '.choosen-file-name',
        'closeIcon': '.close.icon'
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        raw_file: null,
        value: ''
    });

    this.after('initialize', function() {
        this.select('field').on( 'change', this.fieldChanged.bind(this) );
        this.select('closeIcon').on( 'click', this.resetField.bind(this) );

        this.after( 'stateChanged', this.updateField );

        // this.on( document, 'updateField_' + this.attr.fieldName + '_success', function() { console.log('Yay!'); });
        // this.on( document, 'updateField_' + this.attr.fieldName + '_error', function() { console.log('Nay!'); });
    });

    this.fieldChanged = function( event ) {

        var file = this.setFile( event.currentTarget );

        if ( 'empty' !== file.name ) {

            this.getFileContent( file )
                .then(function( rawFile ) {
                    this.select('error').html('');
                    this.setChoosenFileName( file.name );
                    this.mergeState({
                        raw_file: rawFile,
                        value: file.name
                    });
                }.bind( this ))
                .catch(function( errorMessage ) {
                    this.select('error').html( errorMessage );
                }.bind( this ));
        }
    };

    this.updateField = function( state, previousState ) {
        if ( previousState.raw_file !== state.raw_file ) {
            this.trigger( document, 'updateField', state );
        }
    };

    this.resetField = function( event ) {
        this.select('error').html('');
        this.setChoosenFileName('');
        this.mergeState({
            raw_file: '',
            value: ''
        });
    };

    this.setChoosenFileName = function( filename ) {
        this.select('choosenFileName').html( filename );
    };

    this.setFile = function( element ) {
        var file = new File([], 'empty');

        if ( !! element.files.length ) {
            file = element.files[0];
        }

        return file;
    };

    this.getFileContent = function( file ) {
        return new Promise( function ( resolve, reject ) {
            var fileReader = new FileReader();

            if ( ! this.isFileTypeAccepted( file.type ) ) {
                reject('File type "' + file.type + '" doesn\'t supported.');
            } else if ( ! this.isFileSizeAccepted( file.size ) ) {
                reject('File size greater than 1MB.');
            } else {
                fileReader.onload = function( event ) {
                    resolve( event.target.result );
                };

                fileReader.readAsDataURL( file );
            }

        }.bind(this) );
    };

    this.isFileTypeAccepted = function( fileType ) {
        var acceptedTypes = this.select('field').attr('accept').split(/,\s?/g);

        return acceptedTypes.indexOf( fileType ) !== -1;
    };

    this.isFileSizeAccepted = function( fileSize ) {
        var acceptedSize = this.select('field').attr('data-accept-size');

        return acceptedSize >= fileSize;
    };
});

export default fileField;