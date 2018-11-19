import selectField from 'side-kick/features/components/select-field';

export default selectField.mixin(function selectGroupField() {
  this.after('initialize', () => {
    this.select('field').on('change', this.changeGroup.bind(this));

    if (this.state.value) {
      this.showGroup(this.state.value);
    }
  });

  this.changeGroup = (event) => {
    this.showGroup(event.currentTarget.value);
  };

  this.showGroup = (value) => {
    let groupClass = '';

    if (value.length) {
      groupClass = `.${value}`;
    }

    this.$node
      .parents('form')
      .find('.group')
      .slideUp()
      .filter(groupClass)
      .slideDown();
  };
});
