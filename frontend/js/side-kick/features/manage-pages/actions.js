import $ from 'jquery';
import selectFieldComponent from 'side-kick/components/select-field';

export default selectFieldComponent.mixin(function manageActions() {
  this.attributes({
      pageId: undefined,
      pageName: undefined,
      currentAction: undefined,
      charectersRestriction: 'Only 128 charecters allowed using alphanumeric, dashes, and underscores charecters'
  });

  this.after('initialize', function initialize() {
    this.attr.pageId = this.$node.find('label').attr('for').split('_').pop();
    this.attr.pageName = $('#manage_pages_pages option:selected').text();

    this.on(document, 'pageManage_success', this.pageManageSuccess.bind(this));
    this.on(document, 'pageManage_error', this.pageManageError.bind(this));
  });

  this.updateField = function updateField({ value }) {
    this.attr.currentAction = value;

    switch (this.attr.currentAction) {
      case 'create_page':
        this.createPage();
        break;
      case 'rename_page':
        this.renamePage();
        break;
      case 'delete_page':
        this.deletePage();
        break;
    }

    this.resetSelectedIndex();
  };

  this.createPage = function createPage() {
    window.location.href = '/side-kick/new_page/';
  };

  this.renamePage = function renamePage() {
    const pageRename = prompt(
      `How do you want to rename your page?\n${this.attr.charectersRestriction}`,
      this.attr.pageName
    );

    if (pageRename !== null && pageRename.trim().length && pageRename != this.attr.pageName) {
      this.trigger(document, 'pageManage', {
        'action': this.attr.currentAction,
        'id': this.attr.pageId,
        'name': pageRename
      });
    }
  };

  this.deletePage = function deletePage() {
    if (confirm(`Are you sure to delete "${this.attr.pageName}" page?`)) {
      this.trigger(document, 'pageManage', {
        'action': this.attr.currentAction,
        'id': this.attr.pageId
      });
    }
  };

  this.pageManageSuccess = function pageManageSuccess(event, { redirect_url }) {
    if (redirect_url.length) {
      window.top.location.href = redirect_url;
    }
  };

  this.pageManageError = function pageManageError(event, { message }) {
    alert(message);

    switch(this.attr.currentAction) {
      case 'rename_page':
        this.renamePage();
        break;
      case 'create_page':
        this.createPage();
        break;
      default:
        this.resetSelectedIndex();
        break;
    }
  };
});
