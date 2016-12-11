import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

let currentDeviceType = 'desktop';

var devicesComponent = component( function() {
    this.after('initialize', function() {
        this.on( '.device', 'click', this.switch );
    });

    this.switch = function( event ) {
        var $device = $( event.currentTarget ),
            deviceType = $device.text().trim().toLowerCase();

        // TODO: href regex and not text.trim
        // \/(\w+)$

        if ( deviceType !== currentDeviceType ) {
            this.$node
                .children()
                    .removeClass('current');

            $device
                .addClass('current');

            this.trigger( document, 'switchDeviceView', { deviceType } );

            currentDeviceType = deviceType;
        }

        event.preventDefault();
    }
});

devicesComponent.attachTo( '.devices' );