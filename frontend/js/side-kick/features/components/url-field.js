import { component } from 'imports?$=jquery!flightjs';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/features/mixins/validation';

export default component( withFocus, withState, withValidation, function urlField() {

    this.attributes({
        'field': '.field',
        'message': '.message',

        'fieldName': null
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        value: function() {
            return this.select('field').val()
        }
    });

    this.after('initialize', function() {
        this.select('field').on( 'keyup keypress fieldChanged', this.fieldChanged.bind( this ) );
        this.select('field').on( 'blur', this.fieldBlur.bind( this ) );

        this.after( 'stateChanged', this.updateField );
    });

    this.fieldChanged = function( event ) {
        var value = event.currentTarget.value.trim();

        if ( ! this.validate( value ) ) {
            return true;
        }

        this.mergeState({ value });
    };

    this.updateField = function( state, previousState ) {
        if ( previousState.value !== state.value ) {
            this.trigger( document, 'updateField', state );
        }
    };

    this.fieldBlur = function( event ) {
        var value = event.currentTarget.value.trim(),
            httpRegex = /^(https?:\/\/)/;

        if ( value.length && ! httpRegex.test( value ) ) {
            this.select('field')
                .val( 'http://' + value )
                .trigger('fieldChanged');
        }
    };
});
