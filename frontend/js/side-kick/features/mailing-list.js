// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import textFieldComponent from 'side-kick/features/components/text-field';
import selectGroupFieldComponent from 'side-kick/features/components/select-group-field';
import urlFieldComponent from 'side-kick/features/components/url-field';


const mailingList = baseBox.mixin(function box() {
  this.attributes({
    serviceField: '.mailing_list_service',
    mailChimpUsernameField: '.mailing_list_mailchimp_username',
    mailChimpAPIKeyField: '.mailing_list_mailchimp_api_key',
    mailChimpListIdField: '.mailing_list_mailchimp_list_id',
    successfulSubmissionField: '.mailing_list_successful_submission',
    messageField: '.mailing_list_message',
    redirectUrlField: '.mailing_list_redirect_url',
    ctaColorField: '.mailing_list_cta_color',
    ctaTextField: '.mailing_list_cta_text',
    placeholderTextField: '.mailing_list_placeholder_text',
  });

  this.after('initialize', function initialize() {
    // Service
    this.attachChild(selectGroupFieldComponent, this.select('serviceField'), {
      fieldName: 'mailing_list_service',
    });

    // MailChimp Username
    this.attachChild(textFieldComponent, this.select('mailChimpUsernameField'), {
      fieldName: 'mailing_list_mailchimp_username',
    });

    // MailChimp API Key
    this.attachChild(textFieldComponent, this.select('mailChimpAPIKeyField'), {
      fieldName: 'mailing_list_mailchimp_api_key',
    });

    // MailChimp List Id
    this.attachChild(textFieldComponent, this.select('mailChimpListIdField'), {
      fieldName: 'mailing_list_mailchimp_list_id',
    });

    // Successful Submission
    this.attachChild(selectGroupFieldComponent, this.select('successfulSubmissionField'), {
      fieldName: 'mailing_list_successful_submission',
    });

    // Message
    this.attachChild(textFieldComponent, this.select('messageField'), {
      fieldName: 'mailing_list_message',
    });

    // Redirect URL
    this.attachChild(urlFieldComponent, this.select('redirectUrlField'), {
      fieldName: 'mailing_list_redirect_url',
      toValidate: ['url'],
    });

    // CTA Button Color
    this.attachChild(textFieldComponent, this.select('ctaColorField'), {
      fieldName: 'mailing_list_cta_color',
      toValidate: ['hex_color'],
    });

    // CTA Button Text
    this.attachChild(textFieldComponent, this.select('ctaTextField'), {
      fieldName: 'mailing_list_cta_text',
    });

    // Placeholer Text
    this.attachChild(textFieldComponent, this.select('placeholderTextField'), {
      fieldName: 'mailing_list_placeholder_text',
    });
  });
});

mailingList.attachTo('.feature.mailing-list');
