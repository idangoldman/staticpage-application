import flight, { component } from 'imports?$=jquery!flightjs';
import template from './../../views/side-kick/master.njk';
import devicesComponent from './side-kick/devices';

var SideKick = component( function application() {
    this.attributes({
        devices: '.devices',
        features: '.features',
        footer: '.footer'
    });

    this.after('initialize', function() {
        this.$node.html(
            template.render()
        );

        devicesComponent.attachTo('.devices');
    });
});

SideKick.attachTo('.side-kick');