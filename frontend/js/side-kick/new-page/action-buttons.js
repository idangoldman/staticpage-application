import { component } from 'flightjs';

export default component(function actionButtons() {
  this.attributes({
    nameField: null,
    templateField: null,
    createButton: '#create-button',
    cancelButton: '#cancel-button'
  });

  this.after('initialize', function initialize() {
    this.on(this.attr.createButton, 'click', this.create.bind(this));
    this.on(this.attr.cancelButton, 'click', this.cancel.bind(this));
  });

  this.create = function() {
    const nameValue = this.attr.nameField.val().trim();
    const templateValue = this.attr.templateField.val().trim();

    if (nameValue.length) {
      if (templateValue) {
        console.log(nameValue, templateValue);
      } else {
        this.attr.templateField.focus();
      }
    } else {
      this.attr.nameField.focus();
    }
  };

  this.cancel = function() {
    window.history.back();
  };
});
