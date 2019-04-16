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

    this.on(document, 'pageManage_success', this.pageManageSuccess.bind(this));
    this.on(document, 'pageManage_error', this.pageManageError.bind(this));
  });

  this.create = function() {
    const nameValue = this.attr.nameField.val().trim();
    const templateValue = this.attr.templateField.val().trim();

    if (nameValue.length) {
      if (templateValue.length) {
        this.trigger(document, 'pageManage', {
          'action': 'create_page',
          'name': nameValue,
          'template': templateValue
        });
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

  this.pageManageSuccess = function pageManageSuccess(event, { redirect_url }) {
    if (redirect_url.length) {
      window.top.location.href = redirect_url;
    }
  };

  this.pageManageError = function pageManageError(event, { message }) {
    alert(message);
  };
});
