import { component } from 'imports?$=jquery!flightjs';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';

export default component( withFocus, withState, function textField() {

    this.attributes({
        'field': '.field',
        'fieldName': null,
        'optionSelected': 'option:selected',
        'selectTextField': '.selected-text'
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        value: ''
    });

    this.after('initialize', function() {
        this.select('field').on( 'change', this.fieldChanged.bind(this) );

        this.after( 'stateChanged', this.updateField );
        // this.on( document, 'updateField_' + this.attr.fieldName + '_success', function() { console.log('Yay!'); });
        // this.on( document, 'updateField_' + this.attr.fieldName + '_error', function() { console.log('Nay!'); });
    });

    this.fieldChanged = function() {
        this.selectText();

        this.mergeState({
            value: event.currentTarget.value.trim()
        });
    };

    this.updateField = function( state, previousState ) {
        if ( previousState.value !== state.value ) {
            this.trigger( document, 'updateField', state );
        }
    };

    this.selectText = function() {
        this.select('selectTextField')
            .html( this.select('optionSelected').text() );
    };
});