import { component } from 'imports?$=jquery!flightjs';
import 'imports?jQuery=jquery!air-datepicker/dist/js/datepicker.min';
import 'imports?jQuery=jquery!air-datepicker/dist/js/i18n/datepicker.en.js';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/features/mixins/validation';

let startDate = new Date( new Date().getTime() + 24 * 60 * 60 * 1000 ); // 24 Hours ahead


export default component( withFocus, withState, withValidation, function fileField() {

    this.attributes({
        'field': '.field',
        'fieldName': null,
        'closeIcon': '.icon.close',

        'datePicker': {}
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        value: ''
    });

    this.after('initialize', function() {
        this.select('field').on( 'fieldChanged', this.fieldChanged.bind( this ) );
        this.select('closeIcon').on( 'click', this.fieldClear.bind( this ) );

        this.after( 'stateChanged', this.updateField );

        this.attr.datePicker = this.initDatePicker();
    });

    this.fieldChanged = function( event ) {
        var value = event.currentTarget.value.trim();

        this.toggleFilledClass( value );
        this.mergeState({ value });
    }

    this.fieldClear = function( event ) {
        this.attr.datePicker.clear();
    };

    this.updateField = function( state, previousState ) {
        if ( previousState.value !== state.value ) {
            this.trigger( document, 'updateField', state );
        }
    };

    this.initDatePicker = function() {
        return this.select('field')
            .datepicker({
                'language': 'en',
                'minDate': new Date(),
                'startDate': startDate,
                'timeFormat': 'hh:ii',
                'timepicker': true,
                'onSelect': this.onSelect.bind( this ),
                'onShow': this.onShow
            })
            .data('datepicker');
    };

    this.onSelect = function( instance ) {
        this.select('field').trigger('fieldChanged');
    };

    this.onShow = function( instance ) {
        if ( ! instance.selectedDates.length ) {
            instance.selectDate( startDate );
        }
    };

    this.toggleFilledClass = function( value ) {
        if ( value.length ) {
            this.select('field').addClass('filled');
        } else {
            this.select('field').removeClass('filled');
        }
    };
});
