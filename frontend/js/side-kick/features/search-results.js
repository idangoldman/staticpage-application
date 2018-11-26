// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import titleComponent from 'side-kick/features/components/search-results/title';
import descriptionComponent from 'side-kick/features/components/search-results/description';
import previewComponent from 'side-kick/features/components/search-results/preview';


const searchResultsFeature = baseBox.mixin(function box() {
  this.attributes({
    titleField: '.search_results_title',
    descriptionField: '.search_results_description',
    preview: '.search_results_preview',
  });

  this.after('initialize', function initialize() {
    // Title
    this.attachChild(titleComponent, this.select('titleField'), {
      fieldName: 'search_results_title',
      changedContentTitle: 'fieldChanged_content_title',
    });

    // Description
    this.attachChild(descriptionComponent, this.select('descriptionField'), {
      fieldName: 'search_results_description',
      changedContentSubTitle: 'fieldChanged_content_sub_title',
    });

    // Search Preview
    this.attachChild(previewComponent, this.select('preview'), {
      changedTitle: 'fieldChanged_search_results_title',
      changedDescription: 'fieldChanged_search_results_description',
      changedPlaceholderTitle: 'placeholderChanged_search_results_title',
      changedPlaceholderDescription: 'placeholderChanged_search_results_description',
    });
  });
});

searchResultsFeature.attachTo('.feature.search-results');
