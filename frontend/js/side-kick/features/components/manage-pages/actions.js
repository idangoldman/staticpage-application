import $ from 'jquery';
import selectFieldComponent from 'side-kick/features/components/select-field';

export default selectFieldComponent.mixin(function searchPreview() {
  this.attributes({
      pageId: undefined
  });

  this.after('initialize', function initialize() {
    this.attr.pageId = this.$node.find('label').attr('for').split('_').pop();

    this.on(document, 'pageManage_success', this.pageManageSuccess.bind(this));
    this.on(document, 'pageManage_error', this.pageManageError.bind(this));
  });

  this.updateField = function updateField(state, previousState) {
    switch (state.value) {
      case 'create_page':
        this.createPage();
        break;
      case 'rename_page':
        this.renamePage();
        break;
      case 'delete_page':
        this.deletePage();
        break;
      default:
        this.resetSelectedIndex();
        break;
    }
  };

  this.createPage = function createPage() {
    const pageName = prompt('How you want to name your page? Only 128 charecters allowed using alphanumeric, dashes, and underscores charecters');

    if (pageName !== null && pageName.trim().length) {
      this.trigger(document, 'pageManage', {
        'type': 'create',
        'name': pageName
      });
    }

    this.resetSelectedIndex();
  };

  this.renamePage = function renamePage() {
    const pageName = $('#manage_pages_pages option:selected').text();
    const pageRename = prompt(
      'How you want to rename your page? Only 128 charecters allowed using alphanumeric, dashes, and underscores charecters', pageName
    );

    if (pageRename !== null && pageRename.trim().length && pageRename != pageName) {
      this.trigger(document, 'pageManage', {
        'type': 'rename',
        'id': this.attr.pageId,
        'name': pageRename
      });
    }

    this.resetSelectedIndex();
  };

  this.deletePage = function deletePage() {
    if (confirm('Are you sure?')) {
      console.log('yes');
    }

    this.resetSelectedIndex();
  };

  this.pageManageSuccess = function pageManageSuccess(event, { redirect_url }) {
    window.top.location.href = redirect_url;
  };

  this.pageManageError = function pageManageError(event, { message }) {
    alert(message);
    // this.renamePage();
  };
});
