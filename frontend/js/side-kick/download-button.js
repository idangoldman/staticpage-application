import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

var downloadButton = component( function() {

    this.attributes({
        'additionalStyleField': '.design_additional_styles'
    });

    this.after('initialize', function() {
        this.on('click', function(event) {
            console.log('Let the download games begin! :)');
            event.preventDefault();
        })
    });
});

downloadButton.attachTo( '.download-button' );
