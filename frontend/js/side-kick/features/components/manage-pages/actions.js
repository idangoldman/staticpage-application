import selectFieldComponent from 'side-kick/features/components/select-field';

export default selectFieldComponent.mixin(function searchPreview() {
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
    const pageName = prompt('How you want to name your page?');

    if (pageName !== null && pageName.trim().length) {
      console.log('create page');
    }

    this.resetSelectedIndex();
  };

  this.renamePage = function renamePage() {
    const pageRename = prompt('How you want to rename your page?');

    if (pageRename !== null && pageRename.trim().length) {
      console.log('rename page');
    }

    this.resetSelectedIndex();
  };

  this.deletePage = function deletePage() {
    if (confirm('Are you sure?')) {
      console.log('yes');
    }

    this.resetSelectedIndex();
  };
});
