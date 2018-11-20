import $ from 'jquery';
import { component } from 'flightjs';

let currentDeviceType = 'desktop';

const devicesComponent = component(function flightDevices() {
  this.switchDevice = function switchDevice(event) {
    const $device = $(event.currentTarget);
    const deviceType = $device.text().trim().toLowerCase();

    // TODO: href regex and not text.trim
    // \/(\w+)$

    if (deviceType !== currentDeviceType) {
      this.$node
        .children()
        .removeClass('current');

      $device
        .addClass('current');

      this.trigger(document, 'switchDeviceView', { deviceType });
      currentDeviceType = deviceType;
    }

    event.preventDefault();
  };

  this.after('initialize', function initialize() {
    this.on('.device', 'click', this.switchDevice);
  });
});

devicesComponent.attachTo('.devices');
