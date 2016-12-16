import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

import withFocus from '../mixins/focus';
import withState from 'flight-with-state';

var textField = component( withFocus, withState, function application() {

    this.attributes({
        'field': '.field',
        'fieldName': null,
        'message': '.message'
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        value: ''
    });

    this.after('initialize', function() {
        this.select('field').on( 'keyup keypress blur', utils.throttle( this.fieldChanged.bind(this), 250 ) );

        this.after( 'stateChanged', this.updateField );

        // this.on( document, 'updateField_' + this.attr.fieldName + '_success', function() { console.log('Yay!'); });
        // this.on( document, 'updateField_' + this.attr.fieldName + '_error', function() { console.log('Nay!'); });
    });

    this.fieldChanged = function( event ) {

        this.mergeState({
            value: event.currentTarget.value.trim()
        });
    }

    this.updateField = function( state, previousState ) {
        if ( previousState.value !== state.value ) {
            this.trigger( document, 'updateField', state );
        }
    };
});

export default textField;