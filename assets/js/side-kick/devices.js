import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var devicesComponent = component( function() {
    this.after('initialize', function() {
        this.on( '.device', 'click', this.toggle );
    });

    this.toggle = function( event ) {
        var $device = $( event.currentTarget );

        this.$node
            .children()
                .removeClass('current');

        $device
            .addClass('current');

        this.trigger(
            document, 'switchDeviceView', { deviceType: $device.text().trim().toLowerCase() }
        );
    }
});

devicesComponent.attachTo( '.devices' );