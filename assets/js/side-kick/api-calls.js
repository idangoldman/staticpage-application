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
        // new FormData('form')

        var basicRequest = {
            url: PAGE_API_URL,
            type: 'POST',
            success: function( responseData ) {
                console.log( responseData );
                this.trigger( document, eventName + '_success', responseData );
            }.bind(this),
            error: function(jqXHR, textStatus, errorThrown) {
                console.log( jqXHR.responseJSON );
                this.trigger( document, eventName + '_error', jqXHR.responseJSON );
            }.bind(this)
        };

        var jsonRequest = utils.merge( {}, {
            data: JSON.stringify( field ),
            contentType: 'application/json'
        }, basicRequest );

        var requestData = new FormData();
        requestData.append(field.name, field.value);
        var fileRequest = utils.merge( {}, {
            data: requestData,
            dataType: 'json',
            processData: false,
            contentType: false
        }, basicRequest );

        utils.throttle( $.ajax( fileRequest ) );
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
