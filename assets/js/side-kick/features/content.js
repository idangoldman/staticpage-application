import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from 'side-kick/features/mixins/toggle';

// child components
import fileFieldComponent from 'side-kick/features/components/file-field';
import textFieldComponent from 'side-kick/features/components/text-field';

var contentFeature = component( withChildComponents, withToggle, function() {

    this.attributes({
        'logoField': '.content_logo',
        'titleField': '.content_title',
        'subTitleField': '.content_sub_title',
        'descriptionField': '.content_description'
    });

    this.after('initialize', function() {

        // Logo
        this.attachChild( fileFieldComponent, this.select('logoField'), {
            'fieldName': 'content_logo'
        });

        // Title
        this.attachChild( textFieldComponent, this.select('titleField'), {
            'fieldName': 'content_title'
        });

        // Sub-title
        this.attachChild( textFieldComponent, this.select('subTitleField'), {
            'fieldName': 'content_sub_title'
        });

        // Description
        this.attachChild( textFieldComponent, this.select('descriptionField'), {
            'fieldName': 'content_description'
        });
    });
});

contentFeature.attachTo( '.feature.content' );