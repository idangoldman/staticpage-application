import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';
import withRequest from 'imports?$=jquery!flight-request/lib/with_request';

let apiUrl = 'http://0.0.0.0:5000/fake-api';

var apiCalls = component( withRequest, function() {
    this.after('initialize', function() {
        setCsrfHeader();
        this.on( document, 'updateField', updateField );
    });

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

    function updateField( event, data ) {
        console.log(event);
        var postConfig = {
            url: apiUrl,
            data: data,
            success: function( responseData ) {
                this.trigger( document, event.type + '.success', responseData );
            },
            // error: function(jqXHR, textStatus, errorThrown) {
            error: function() {
                this.trigger( document, event.type + '.error' );
            }
        };

        this.post( postConfig );
    }
});

apiCalls.attachTo( document );