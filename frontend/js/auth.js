import { component } from 'flightjs';

// mixins
import withChildComponents from 'flight-with-child-components';
import selectFieldComponent from 'side-kick/components/select-field';

const registerPage = component(withChildComponents, function page() {
  this.attributes({
    templateField: '.template'
  });

  this.after('initialize', function initialize() {
    // Page Template
    const templateFieldComponent = selectFieldComponent.mixin(function template() {
      this.updateField = function updateField() {};
    });
    this.attachChild(templateFieldComponent, this.select('templateField'), {
      fieldName: 'template',
    });
  });
});

registerPage.attachTo('.register');
