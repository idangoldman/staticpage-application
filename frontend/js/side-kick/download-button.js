import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

import withState from 'flight-with-state';

var downloadButton = component( withState, function() {

    this.initialState({
        disabled: false
    });

    this.after('initialize', function() {
        this.on( 'click', this.startDownload.bind() );
        this.on( document, 'finishDownload', this.finishDownload.bind() );
    });

    this.startDownload = function( event ) {
        if ( !! this.state.disabled ) {
            this.mergeState({ disabled: true });
            console.log('Let the download games begin! :)');
            this.trigger( document, 'startDownload', {} );
        }

        event.preventDefault();
    };

    this.finishDownload = function() {
        console.log('download games are done! :)');
        this.mergeState({ disabled: false })
    }
});

downloadButton.attachTo( '.download-button' );
