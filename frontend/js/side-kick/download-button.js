import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

import withState from 'flight-with-state';

var downloadButton = component( withState, function() {

    this.initialState({
        disabled: false
    });

    this.after('initialize', function() {
        this.on( 'click', this.siteDownload.bind( this ) );
        this.on( document, 'siteDownload_success', this.siteDownloadSuccess.bind( this ) );
        // this.on( document, 'siteDownload_error', this.siteDownloadError.bind( this ) );
    });

    this.siteDownload = function( event ) {
        if ( ! this.state.disabled ) {
            this.mergeState({ disabled: true });
            this.trigger( document, 'siteDownload', {} );
        }

        event.preventDefault();
    };

    this.siteDownloadSuccess = function( event, { url } ) {
        this.mergeState({ disabled: false });
        if ( !! url ) {
            window.location = url;
        }
    };
});

downloadButton.attachTo( '#download-button' );
