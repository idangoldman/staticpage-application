const withSelect = function mixin() {
  this.attributes({
    focusField: '.field',
  });

  const focus = (event) => {
    $(event.currentTarget)
      .parent()
      .addClass('focus');
  };

  const blur = (event) => {
    $(event.currentTarget)
      .parent()
      .removeClass('focus');
  };

  this.after('initialize', () => {
    // focus click
    this.select('focusField').on('focus', focus);

    // blur click
    this.select('focusField').on('blur', blur);
  });
};

export default withSelect;
