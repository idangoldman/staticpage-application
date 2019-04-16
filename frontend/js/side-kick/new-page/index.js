import { component } from 'flightjs';

// mixins
import withChildComponents from 'flight-with-child-components';
import withPreventSubmit from 'side-kick/components/mixins/prevent-submit';

// child components
import textFieldComponent from 'side-kick/components/text-field';
import selectFieldComponent from 'side-kick/components/select-field';
import actionButtonsComponent from 'side-kick/new-page/action-buttons';

const newPage = component(withChildComponents, withPreventSubmit, function page() {
  this.attributes({
    nameField: '.name',
    templateField: '.template',
    actionButtons: '.action-buttons'
  });

  this.after('initialize', function initialize() {
    const $name = this.select('nameField');
    const $template = this.select('templateField');

    // Page Name
    const nameFieldComponent = textFieldComponent.mixin(function name() {
      this.updateField = function updateField() {};
    });
    this.attachChild(nameFieldComponent, $name, {
      fieldName: 'name',
    });

    // Page Template
    const templateFieldComponent = selectFieldComponent.mixin(function template() {
      this.updateField = function updateField() {};
    });
    this.attachChild(templateFieldComponent, $template, {
      fieldName: 'template',
    });

    // Button Actions
    this.attachChild(actionButtonsComponent, this.select('actionButtons'), {
      nameField: $name.find('input'),
      templateField: $template.find('select'),
    });
  });
});

newPage.attachTo('.new-page');
