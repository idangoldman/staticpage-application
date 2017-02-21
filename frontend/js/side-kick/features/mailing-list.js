// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import textFieldComponent from 'side-kick/features/components/text-field';
import selectGroupFieldComponent from 'side-kick/features/components/select-group-field';
import urlFieldComponent from 'side-kick/features/components/url-field';


var mailingList = baseBox.mixin( function box() {

    this.attributes({
        'serviceField': '.mailing_list_service',
        'completionUrlField': '.mailing_list_completion_url',
        'mailChimpUsernameField': '.mailing_list_mailchimp_username',
        'mailChimpAPIKeyField': '.mailing_list_mailchimp_api_key',
        'mailChimpListIdField': '.mailing_list_mailchimp_list_id'
    });

    this.after('initialize', function() {

        // Service
        this.attachChild( selectGroupFieldComponent, this.select('serviceField'), {
            'fieldName': 'mailing_list_service'
        });

        // MailChimp Username
        this.attachChild( textFieldComponent, this.select('mailChimpUsernameField'), {
            'fieldName': 'mailing_list_mailchimp_username'
        });

        // MailChimp API Key
        this.attachChild( textFieldComponent, this.select('mailChimpAPIKeyField'), {
            'fieldName': 'mailing_list_mailchimp_api_key'
        });

        // MailChimp List Id
        this.attachChild( textFieldComponent, this.select('mailChimpListIdField'), {
            'fieldName': 'mailing_list_mailchimp_list_id'
        });

        // Completion URL
        this.attachChild( urlFieldComponent, this.select('completionUrlField'), {
            'fieldName': 'mailing_list_completion_url',
            'toValidate': ['url']
        });

    });

});

mailingList.attachTo( '.feature.mailing-list' );
