// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import codeComponent from 'side-kick/features/components/text-field';


var googleAnalyticsFeature = baseBox.mixin( function box() {

    this.attributes({
        'codeField': '.google_analytics_code'
    });

    this.after('initialize', function() {

        // Code
        this.attachChild( codeComponent, this.select('codeField'), {
            'fieldName': 'google_analytics_code',
            'toValidate': ['ua_code']
        });
    });
});

googleAnalyticsFeature.attachTo( '.feature.google-analytics' );
