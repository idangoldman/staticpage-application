import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from 'side-kick/features/mixins/toggle';

// child components
import textFieldComponent from 'side-kick/features/components/text-field';
import searchPreviewComponent from 'side-kick/features/components/search-preview';

var serchResultsFeature = component( withChildComponents, withToggle, function() {

    this.attributes({
        'titleField': '.search_results_title',
        'descriptionField': '.search_results_description',
        'searchPreviewField': '.search_results_preview'
    });

    this.after('initialize', function() {

        // Title
        this.attachChild( textFieldComponent, this.select('titleField'), {
            'fieldName': 'search_results_title'
        });

        // Description
        this.attachChild( textFieldComponent, this.select('descriptionField'), {
            'fieldName': 'search_results_description'
        });

        // Search Preview
        this.attachChild( searchPreviewComponent, this.select('searchPreviewField'), {
            'changedTitleEvent': 'fieldChanged_search_results_title',
            'changedDescriptionEvent': 'fieldChanged_search_results_description'
        });
    });
});

serchResultsFeature.attachTo( '.feature.search-results' );
