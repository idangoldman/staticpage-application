import { component } from 'imports?$=jquery!flightjs';
import 'imports?jQuery=jquery!air-datepicker/dist/js/datepicker.min';
import 'imports?jQuery=jquery!air-datepicker/dist/js/i18n/datepicker.en.js';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/features/mixins/validation';

export default component( withFocus, withState, withValidation, function fileField() {

    this.attributes({
        'field': '.field',
        'fieldName': null,
        'closeIcon': '.icon.close'
    });

    this.initialState({
        name: this.fromAttr('fieldName'),
        value: '',

        datePicker: {}
    });

    this.after('initialize', function() {

        this.state.datePicker = this.initDatePicker();
    });

    this.initDatePicker = function() {
        var startDate = new Date( new Date().getTime() + 24 * 60 * 60 * 1000 ); // 24 Hours ahead

        return this.select('field')
            .datepicker({
                'language': 'en',
                'minDate': new Date(),
                'startDate': startDate,
                'timeFormat': 'hh:ii',
                'timepicker': true,
                'onShow': function( instance ) {
                    if ( ! instance.selectedDates.length ) {
                        instance.selectDate( startDate );
                    }
                }
            })
            .data('datepicker');
    }
});
