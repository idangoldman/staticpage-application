import $ from 'jquery';

const withToggle = function mixin() {
  this.attributes({
    toggleBox: '.body',
    toggleClass: 'close',
    toggleClick: '.header',
  });

  const toggle = function toggle(event) {
    const $target = $(event.currentTarget);
    const isClosed = $target.parent().hasClass('close');

    $target
      .parents('.features')
        .children()
          .addClass(this.attr.toggleClass)
          .children(this.attr.toggleBox)
            .slideUp();

    if (isClosed) {
      $target
        .parent()
          .removeClass(this.attr.toggleClass)
          .children(this.attr.toggleBox)
            .slideDown();
    }
  };

  this.after('initialize', function initialize() {
    this.select('toggleClick').on('click', toggle.bind(this));
  });
};

export default withToggle;
