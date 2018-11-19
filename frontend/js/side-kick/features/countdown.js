// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import selectFieldComponent from 'side-kick/features/components/select-field';
import datepickerFieldComponent from 'side-kick/features/components/datepicker-field';
import urlFieldComponent from 'side-kick/features/components/url-field';


const countDownFeature = baseBox.mixin(function box() {
  this.attributes({
    timezoneField: '.countdown_timezone',
    datetimeField: '.countdown_datetime',
    redirectUrlField: '.countdown_redirect_url',
  });

  this.after('initialize', () => {
    // Timezone
    this.attachChild(selectFieldComponent, this.select('timezoneField'), {
      fieldName: 'countdown_timezone',
    });

    // Datepicker
    this.attachChild(datepickerFieldComponent, this.select('datetimeField'), {
      fieldName: 'countdown_datetime',
    });

    // Redirect URL
    this.attachChild(urlFieldComponent, this.select('redirectUrlField'), {
      fieldName: 'countdown_redirect_url',
      toValidate: ['url'],
    });
  });
});

countDownFeature.attachTo('.feature.countdown');
