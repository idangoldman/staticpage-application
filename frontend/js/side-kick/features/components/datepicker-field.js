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
        value: ''
    });

    this.after('initialize', function() {

        this.select('field').datepicker({
            'language': 'en',
            'timepicker': true,
            'timeFormat': 'hh:ii'
        });
    });
});
