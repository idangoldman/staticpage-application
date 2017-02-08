// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
// import checkboxFieldComponent from 'side-kick/features/components/checkbox-field';
import selectFieldComponent from 'side-kick/features/components/select-field';
// import datepickerFieldComponent from 'side-kick/features/components/datepicker-field';


var countDownFeature = baseBox.mixin( function box() {

    this.attributes({
        'enableField': '.count_down_enable',
        'timezoneField': '.count_down_timezone',
        'datetimeField': '.count_down_datetime'
    });

    this.after('initialize', function() {

        // Enable
        // this.attachChild( checkboxFieldComponent, this.select('enableField'), {
        //     'fieldName': 'count_down_enable'
        // });

        // Datepicker
        // this.attachChild( datepickerFieldComponent, this.select('datetimeField'), {
        //     'fieldName': 'count_down_datetime'
        // });

        // Timezone
        this.attachChild( selectFieldComponent, this.select('timezoneField'), {
            'fieldName': 'count_down_timezone'
        });

    });
});

countDownFeature.attachTo( '.feature.count-down' );
