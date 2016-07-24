import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

import pageInfoComponent from './page-info';

var featuresComponent = component( function application() {
    this.after('initialize', function() {
        pageInfoComponent.attachTo( this.$node );
    });
});

export default featuresComponent;