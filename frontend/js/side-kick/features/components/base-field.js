import $ from 'jquery';
import { component } from 'flightjs';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/features/mixins/validation';


export default component( withFocus, withState, withValidation, function Field() {

    this.attributes({
        'field': '.field'
    });


    this.initialState({
        name: function() {
            return this.select('field').attr('name');
        },
        value: function() {
            return this.select('field').val();
        },
        placeholder: function() {
            return this.select('field').attr('placeholder') || ''
        }
    });


    this.after('initialize', function() {
        this.select('field').on( 'change', this.change.bind( this ) );
        this.select('field').on( 'blur', this.blur.bind( this ) );

        this.after( 'stateChanged', this.update );

        this.on( document, 'fieldUpdatedSuccessful_' + this.state.name, this.success });
        this.on( document, 'fieldUpdateFailed_' + this.state.name, this.error });
    });


    this.change = function( event ) {
        var value = event.currentTarget.value.trim();

        this.trigger( document, 'fieldChanged_' + this.state.name, this.state );
    };


    this.blur = function( event ) {
        var value = event.currentTarget.value.trim();

        if ( this.validate( value ) ) {
            this.mergeState({ value });
        }
    };


    this.update = function( state, previousState ) {
        if ( state.value !== previousState.value ) {
            this.trigger( document, 'fieldUpdate', state );
        }
    };


    this.success = function( event, data ) {
        console.log( 'success:', data );
    }


    this.error = function( event, data ) {
        console.log( 'error:', data );
    }
});
