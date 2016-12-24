import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/features/mixins/validation';

export default component( withFocus, withState, withValidation, function textField() {

    this.attributes({
        'field': '.field',
        'message': '.message',

        'fieldName': null
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        value: ''
    });

    this.after('initialize', function() {
        this.select('field').on( 'keyup keypress blur', this.fieldChanged.bind(this) );

        this.after( 'stateChanged', this.updateField );
        // this.on( document, 'updateField_' + this.attr.fieldName + '_success', function() { console.log('Yay!'); });
        // this.on( document, 'updateField_' + this.attr.fieldName + '_error', function() { console.log('Nay!'); });
    });

    this.fieldChanged = function( event ) {
        var value = event.currentTarget.value.trim();

        if ( ! this.validate( value ) ) {
            return true;
        }

        this.mergeState({
            value: value
        });
    }

    this.updateField = function( state, previousState ) {
        if ( previousState.value !== state.value ) {
            this.trigger( document, 'updateField', state );
        }
    };
});