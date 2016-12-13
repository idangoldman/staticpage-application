import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';
import withRequest from 'imports?$=jquery!flight-request/lib/with_request';

let apiUrl = 'http://0.0.0.0:5000/fake-api';

var apiCalls = component( withRequest, function() {
    this.after('initialize', function() {
        setCsrfHeader();

        this.on( document, 'updateField', this.updateField );
    });

    this.updateField = function( event, data ) {
        var eventName = event.type + '_' + data.name,
            putConfig = {
                url: apiUrl,
                data: { 'data': JSON.stringify( data ) },
                success: function( responseData ) {
                    this.trigger( document, eventName + '_success', responseData );
                },
                // error: function(jqXHR, textStatus, errorThrown) {
                error: function() {
                    this.trigger( document, eventName + '_error' );
                }
            };

        this.put( putConfig );
    };

    function setCsrfHeader() {
        // code from: https://flask-wtf.readthedocs.io/en/stable/csrf.html
        var csrftoken = $('meta[name=csrf-token]').attr('content')
        $.ajaxSetup({
            beforeSend: function( xhr, settings ) {
                if ( ! /^(GET|HEAD|OPTIONS|TRACE)$/i.test( settings.type ) && ! this.crossDomain ) {
                    xhr.setRequestHeader( "X-CSRFToken", csrftoken );
                }
            }
        })
    }
});

apiCalls.attachTo( document );