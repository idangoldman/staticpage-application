const switchDeviceView = ({ deviceType }) => {
  $('.page')
    .removeClass((index, css) => (css.match(/\w+-view/g) || []).join(' '))
    .addClass(`${deviceType}-view`);
};

const updatePageContent = (messageData) => {
  window.frames.page.postMessage(messageData, '*');
};

const receiveMessage = (event) => {
  const message = event.originalEvent.data;

  if (!$.isEmptyObject(message)) {
    switch (message.type) {
      case 'switchDeviceView':
        switchDeviceView(message.data);
        break;
      case 'updatePageContent':
      default:
        updatePageContent(message.data);
        break;
    }
  }
};

$(window).on('message onmessage', receiveMessage);
