import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from 'side-kick/features/mixins/toggle';

// child components
import codeComponent from 'side-kick/features/components/text-field';

var googleAnalyticsFeature = component( withChildComponents, withToggle, function() {

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
