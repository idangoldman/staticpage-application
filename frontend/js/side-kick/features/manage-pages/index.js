// base component
import baseBox from 'side-kick/components/base-box';

// child components
import pagesFieldComponent from 'side-kick/features/manage-pages/pages';
import actionsFieldComponent from 'side-kick/features/manage-pages/actions';

const managePagesFeature = baseBox.mixin(function box() {
  this.attributes({
    pagesField: '.manage_pages_pages',
    actionsField: '.manage_pages_actions',
  });

  this.after('initialize', function initialize() {
    // Page List
    this.attachChild(pagesFieldComponent, this.select('pagesField'), {
      fieldName: 'manage_pages_pages',
    });

    // Page Actions
    this.attachChild(actionsFieldComponent, this.select('actionsField'), {
      fieldName: 'manage_pages_actions',
    });
  });
});

managePagesFeature.attachTo('.feature.manage-pages');
