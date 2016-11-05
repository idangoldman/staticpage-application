import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';
import template from 'views/side-kick/devices.njk';

var devicesComponent = component( function application() {
    this.after('initialize', function() {
        this.$node.html(
            template.render()
        );

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

export default devicesComponent;