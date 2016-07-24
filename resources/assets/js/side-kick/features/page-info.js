import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';
import template from 'views/side-kick/features/page-info.njk';

var pageInfoComponent = component( function application() {
    this.after('initialize', function() {
        this.$node.html(
            template.render()
        );
    });
});

export default pageInfoComponent;