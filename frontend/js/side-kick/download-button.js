import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

import withState from 'flight-with-state';

var downloadButton = component( withState, function() {

    this.initialState({
        disabled: false
    });

    this.after('initialize', function() {
        this.on( 'click', this.siteDownload.bind( this ) );
        this.on( document, 'siteDownload_success', this.siteDownload.bind( this ) );
        this.on( document, 'siteDownload_error', this.siteDownload.bind( this ) );
    });

    this.siteDownload = function( event ) {
        if ( ! this.state.disabled ) {
            this.mergeState({ disabled: true });
            this.trigger( document, 'siteDownload', {} );
        }

        event.preventDefault();
    };

    this.siteDownload = function( event, data ) {
        console.log( 'download games are done! :)', data );
        this.mergeState({ disabled: false })
    }
});

downloadButton.attachTo( '.download-button' );
