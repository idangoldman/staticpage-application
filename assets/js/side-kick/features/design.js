import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from 'side-kick/features/mixins/toggle';

// child components
import fileFieldComponent from 'side-kick/features/components/file-field';
import textFieldComponent from 'side-kick/features/components/text-field';

var designFeature = component( withChildComponents, withToggle, function() {

    this.attributes({
        'backgroundImageField': '.design_background_image',
        'backgroundColorField': '.design_background_color'
    });

    this.after('initialize', function() {

        // Background Image
        this.attachChild( fileFieldComponent, this.select('backgroundImageField'), {
            'fieldName': 'design_background_image'
        });

        // Background Color
        this.attachChild( textFieldComponent, this.select('backgroundColorField'), {
            'fieldName': 'design_background_color'
        });
    });
});

designFeature.attachTo( '.feature.design' );