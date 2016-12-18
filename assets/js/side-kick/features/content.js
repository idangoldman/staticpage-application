import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from './mixins/toggle';

// child components
import fileFieldComponent from './components/file-field';
import textFieldComponent from './components/text-field';

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