import $ from 'jquery';

const withSelect = function mixin() {
  this.attributes({
    focusField: '.field',
  });

  const focus = function focus(event) {
    $(event.currentTarget)
      .parent()
      .addClass('focus');
  };

  const blur = function blur(event) {
    $(event.currentTarget)
      .parent()
      .removeClass('focus');
  };

  this.after('initialize', function initialize() {
    // focus click
    this.select('focusField').on('focus', focus);

    // blur click
    this.select('focusField').on('blur', blur);
  });
};

export default withSelect;
