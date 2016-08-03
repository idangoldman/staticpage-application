import flight, { component } from 'imports?$=jquery!flightjs';
import template from 'views/side-kick/master.njk';
import devicesComponent from './side-kick/devices';
import featuresComponent from './side-kick/features';
import storeComponent from './side-kick/store';

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

        devicesComponent.attachTo( this.attr.devices );
        featuresComponent.attachTo( this.attr.features );

        storeComponent.attachTo( document );

        // this.on( document, 'switchDeviceView', function( event, { deviceType } ) {
        //     console.log( deviceType );
        // } );

        // this.on( document, 'app-loaded', function( event, data ) {
        // } );
    });
});

SideKick.attachTo('.side-kick');