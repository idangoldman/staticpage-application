import { component } from 'flightjs';
import withState from 'flight-with-state';

const downloadButton = component(withState, function downloadButton() {
  this.initialState({
    disabled: false,
  });

  this.after('initialize', function initial() {
    this.on('click', this.siteDownload.bind(this));
    this.on(document, 'siteDownload_success', this.siteDownloadSuccess.bind(this));
    // this.on( document, 'siteDownload_error', this.siteDownloadError.bind( this ) );
  });

  this.siteDownload = function siteDownload(event) {
    if (!this.state.disabled) {
      this.mergeState({ disabled: true });
      this.toggleLoadingClass();
      this.trigger(document, 'siteDownload', {});
    }

    event.preventDefault();
  };

  this.siteDownloadSuccess = function siteDownloadSuccess(event, { url }) {
    this.mergeState({ disabled: false });
    this.toggleLoadingClass();
    if (url) {
      window.location = url;
    }
  };

  this.toggleLoadingClass = function toggleLoadingClass() {
    this.$node.toggleClass('loading');
  };
});

downloadButton.attachTo('#download-button');
