import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from 'side-kick/features/mixins/toggle';

// child components
import fileFieldComponent from 'side-kick/features/components/file-field';
import textFieldComponent from 'side-kick/features/components/text-field';
import selectFieldComponent from 'side-kick/features/components/select-field';

var designFeature = component( withChildComponents, withToggle, function() {

    this.attributes({
        'backgroundImageField': '.design_background_image',
        'backgroundColorField': '.design_background_color',
        'backgroundRepeatField': '.design_background_repeat',
        'contentAlignmentField': '.design_content_alignment',
        'contentDirectionField': '.design_content_direction'
    });

    this.after('initialize', function() {

        // Background Image
        this.attachChild( fileFieldComponent, this.select('backgroundImageField'), {
            'fieldName': 'design_background_image',
            'toValidate': ['file_size', 'file_format']
        });

        // Background Color
        this.attachChild( textFieldComponent, this.select('backgroundColorField'), {
            'fieldName': 'design_background_color',
            'toValidate': ['hex_color']
        });

        // Background Repeat
        this.attachChild( selectFieldComponent, this.select('backgroundRepeatField'), {
            'fieldName': 'design_background_repeat'
        });

        // Content Alignment
        this.attachChild( selectFieldComponent, this.select('contentAlignmentField'), {
            'fieldName': 'design_content_alignment'
        });

        // Content Direction
        this.attachChild( selectFieldComponent, this.select('contentDirectionField'), {
            'fieldName': 'design_content_direction'
        });
    });
});

designFeature.attachTo( '.feature.design' );