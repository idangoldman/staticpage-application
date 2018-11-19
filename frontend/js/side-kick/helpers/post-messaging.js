import { component } from 'flightjs';
import * as pageUpdateFields from '../../page/constants';

const postMessaging = component(function postMessaging() {
  const message = (event, data) => {
    const type = event.type ? event.type : event;

    window.parent.postMessage({ type, data }, '*');
  };

  const updatePage = (event, data) => {
    Object.keys(pageUpdateFields).forEach((key) => {
      if (pageUpdateFields[key] === data.name) {
        message('updatePageContent', data);
      }
    });
  };

  this.after('initialize', () => {
    this.on(document, 'switchDeviceView', message);
    this.on(document, 'updateField', updatePage);
  });
});

postMessaging.attachTo(document);
