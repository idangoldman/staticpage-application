// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
// import checkboxFieldComponent from 'side-kick/features/components/checkbox-field';
import selectFieldComponent from 'side-kick/features/components/select-field';
// import dateFieldComponent from 'side-kick/features/components/date-field';
// import timeFieldComponent from 'side-kick/features/components/time-field';


var countDownFeature = baseBox.mixin( function box() {

    this.attributes({
        'enableField': '.count_down_enable',
        'timezoneField': '.count_down_timezone',
        'dateField': '.count_down_date',
        'timeField': '.count_down_time'
    });

    this.after('initialize', function() {

        // Enable
        this.attachChild( checkboxFieldComponent, this.select('enableField'), {
            'fieldName': 'count_down_enable'
        });

        // Timezone
        this.attachChild( selectFieldComponent, this.select('timezoneField'), {
            'fieldName': 'count_down_timezone'
        });

        // // Date
        // this.attachChild( dateFieldComponent, this.select('dateField'), {
        //     'fieldName': 'count_down_date'
        // });
        //
        // // Time
        // this.attachChild( timeFieldComponent, this.select('timeField'), {
        //     'fieldName': 'count_down_time'
        // });
    });
});

countDownFeature.attachTo( '.feature.count-down' );
