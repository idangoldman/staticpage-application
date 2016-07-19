import flight, { component } from 'imports?$=jquery!flightjs';
import template from './../../../views/side-kick/devices.njk';

var devicesComponent = component( function application() {
    this.after('initialize', function() {
        this.$node.html(
            template.render()
        );
    });
});

export default devicesComponent;