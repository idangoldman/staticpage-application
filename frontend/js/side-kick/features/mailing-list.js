// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import textFieldComponent from 'side-kick/features/components/text-field';
import selectFieldComponent from 'side-kick/features/components/select-field';
import urlFieldComponent from 'side-kick/features/components/url-field';


var mailingList = baseBox.mixin( function box() {

    this.attributes({
        'serviceField': '.mailing_list_service',
        'completionUrlField': '.mailing_list_completion_url'
    });

    this.after('initialize', function() {

        // Service
        this.attachChild( selectFieldComponent, this.select('serviceField'), {
            'fieldName': 'mailing_list_service'
        });

        // Completion URL
        this.attachChild( urlFieldComponent, this.select('completionUrlField'), {
            'fieldName': 'mailing_list_completion_url',
            'toValidate': ['url']
        });

    });

});

mailingList.attachTo( '.feature.mailing-list' );
