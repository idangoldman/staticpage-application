// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import selectFieldComponent from 'side-kick/features/components/select-field';
import datepickerFieldComponent from 'side-kick/features/components/datepicker-field';
import urlFieldComponent from 'side-kick/features/components/url-field';


var countDownFeature = baseBox.mixin( function box() {

    this.attributes({
        'timezoneField': '.count_down_timezone',
        'datetimeField': '.count_down_datetime',
        'redirectUrlField': '.count_down_redirect_url'
    });

    this.after('initialize', function() {

        // Timezone
        this.attachChild( selectFieldComponent, this.select('timezoneField'), {
            'fieldName': 'count_down_timezone'
        });

        // Datepicker
        this.attachChild( datepickerFieldComponent, this.select('datetimeField'), {
            'fieldName': 'count_down_datetime'
        });

        // Redirect URL
        this.attachChild( urlFieldComponent, this.select('redirectUrlField'), {
            'fieldName': 'count_down_redirect_url',
            'toValidate': ['url']
        });

    });
});

countDownFeature.attachTo( '.feature.count-down' );
