import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from 'side-kick/features/mixins/toggle';

// child components
import titleComponent from 'side-kick/features/components/search-results/title';
import descriptionComponent from 'side-kick/features/components/search-results/description';
import previewComponent from 'side-kick/features/components/search-results/preview';

var serchResultsFeature = component( withChildComponents, withToggle, function() {

    this.attributes({
        'titleField': '.search_results_title',
        'descriptionField': '.search_results_description',
        'preview': '.search_results_preview'
    });

    this.after('initialize', function() {

        // Title
        this.attachChild( titleComponent, this.select('titleField'), {
            'fieldName': 'search_results_title',
            'changedContentTitleEvent': 'fieldChanged_content_title'
        });

        // Description
        this.attachChild( descriptionComponent, this.select('descriptionField'), {
            'fieldName': 'search_results_description',
            'changedContentSubTitleEvent': 'fieldChanged_content_sub_title'
        });

        // Search Preview
        this.attachChild( previewComponent, this.select('preview'), {
            'changedTitleEvent': 'fieldChanged_search_results_title',
            'changedDescriptionEvent': 'fieldChanged_search_results_description',
            'changedPlaceholderTitleEvent': 'placeholderChanged_search_results_title',
            'changedPlaceholderDescriptionEvent': 'placeholderChanged_search_results_description',
        });
    });
});

serchResultsFeature.attachTo( '.feature.search-results' );
