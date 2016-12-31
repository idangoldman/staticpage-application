import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

const PAGE_API_URL = window.page_api_url;

var apiCalls = component( function() {
    this.after('initialize', function() {
        setCsrfHeader();

        this.on( document, 'updateField', this.updateField );
    });

    this.updateField = function( event, field ) {
        var eventName = event.type + '_' + field.name;
        // var requestData = {};
        //     requestData[field.name] = field.value;

        utils.throttle( $.ajax({
            url: PAGE_API_URL,
            type: 'POST',
            data: JSON.stringify( field ),
            contentType: 'application/json',
            success: function( responseData ) {
                console.log( responseData );
                this.trigger( document, eventName + '_success', responseData );
            },
            // error: function(jqXHR, textStatus, errorThrown) {
            error: function() {
                this.trigger( document, eventName + '_error' );
            }
        }) );
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