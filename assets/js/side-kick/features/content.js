import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from './mixins/toggle';

// child components
import imageFieldComponent from './components/image-field';

var contentFeature = component( withChildComponents, withToggle, function() {

    this.attributes({
        'logoField': '.content_logo'
    });

    this.after('initialize', function() {
        this.attachChild( imageFieldComponent, this.select('logoField'), {
            'fieldName': 'content_logo'
        });
    });
});

contentFeature.attachTo( '.feature.content' );