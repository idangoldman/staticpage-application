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

        utils.throttle( $.ajax( this.requestConfig( eventName, field ) ) );
    };

    this.requestConfig = function( eventName, field ) {
        var config = {
                url: PAGE_API_URL,
                type: 'POST',
                success: function requestSuccess( response ) {
                    this.trigger( document, eventName + '_success', response.data );
                }.bind(this),
                error: function requestError( jqXHR, textStatus, errorThrown ) {
                    this.trigger( document, eventName + '_error', jqXHR.responseJSON );
                }.bind(this)
            },
            fileConfig = {},
            jsonConfig = {};

        if ( !! field.base64 ) {
            var requestData = new FormData();
                requestData.append( field.name, field.value );

            fileConfig = {
                data: requestData,
                dataType: 'json',
                processData: false,
                contentType: false
            };

            config = utils.merge( {}, config, fileConfig );
        } else {
            jsonConfig = {
                data: JSON.stringify( field ),
                contentType: 'application/json'
            };

            config = utils.merge( {}, jsonConfig, config );
        }


        return config;
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
