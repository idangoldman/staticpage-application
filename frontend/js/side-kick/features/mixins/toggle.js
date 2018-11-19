const withToggle = function mixin() {
  this.attributes({
    toggleBox: '.body',
    toggleClass: 'close',
    toggleClick: '.header',
  });

  const toggle = (event) => {
    $(event.currentTarget)
      .parent()
      .toggleClass(this.attr.toggleClass)
      .children(this.attr.toggleBox)
      .slideToggle();
  };

  this.after('initialize', () => {
    // toggle feature box
    this.select('toggleClick').on('click', toggle.bind(this));
  });
};

export default withToggle;
