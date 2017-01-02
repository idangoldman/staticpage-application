import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/features/mixins/validation';

export default component( withFocus, withState, withValidation, function fileField() {

    this.attributes({
        'field': '.field',
        'fieldName': null,
        'choosenFileName': '.choosen-file-name',
        'closeIcon': '.close.icon'
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        base64: null,
        value: {}
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
                    this.setChoosenFileName( file.name );
                    this.mergeState({
                        base64: rawFile,
                        value: file
                    });
                }.bind( this ))
                .catch(function() {
                    // console.log('something went wrong...')
                }.bind( this ));
        }
    };

    this.updateField = function( state, previousState ) {
        if ( previousState.base64 !== state.base64 ) {
            this.trigger( document, 'updateField', state );
        }
    };

    this.resetField = function( event ) {
        this.removeErrorClass();
        this.setChoosenFileName('');
        this.mergeState({
            base64: null,
            value: {}
        });
        // this.replaceState( this.defaultState );
    };

    this.setChoosenFileName = function( filename ) {
        this.select('choosenFileName').html( filename );
    };

    this.setFile = function( element ) {
        var file = new File([], 'empty');

        if ( !! element.files.length ) {
            file = element.files[0];
            element.value = '';
        }

        return file;
    };

    this.getFileContent = function( file ) {
        return new Promise( function ( resolve, reject ) {
            var fileReader = new FileReader();

            if ( ! this.validate( file ) ) {
                reject();
            } else {
                fileReader.onload = function( event ) {
                    resolve( event.target.result );
                };

                fileReader.readAsDataURL( file );
            }
        }.bind(this) );
    };
});
