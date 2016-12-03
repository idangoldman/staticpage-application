import flight, { component } from 'imports?$=jquery!flightjs';
import devicesComponent from './side-kick/devices';

let SideKick = component( function application() {
    this.attributes({
        devices: '.devices'
    });

    this.after('initialize', function() {
        devicesComponent.attachTo( this.attr.devices );

        // this.on( document, 'switchDeviceView', function( event, { deviceType } ) {
        //     console.log( deviceType );
        // } );
    });
});

SideKick.attachTo('.side-kick');