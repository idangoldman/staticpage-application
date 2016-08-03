import $ from 'jquery';
import { component } from 'imports?$=jquery!flightjs';

// template
import template from 'views/side-kick/features/page-info.njk';

// mixins
import withImageUpload from './with/image-upload';
import withSelectText from './with/select-text';
import withToggle from './with/toggle';

var pageInfoComponent = component( withSelectText, withImageUpload, withToggle, function application() {

    this.attributes({
        typeSelect: '.fieldset.type .select-wrap .field',
        logoUpload: '.fieldset.logo .upload-wrap .field',
        logoMessage: '.fieldset.logo .message',
        fields: '.field',
        url: '/page-info/'
    });

    this.after('initialize', function() {
        this.on( document, 'initial.data', function( event, { pageInfo } ) {
            this.load( pageInfo );
        });
    });

    this.load = function( data ) {
        this.render( data );
        this.events();
    };

    this.render = function( data ) {
        this.$node.html(
            template.render( data )
        );
    };

    this.events = function() {

        // toggle feature box
        this.on( '.header', 'click', this.toggle );

        // focus click
        this.on( this.attr.fields, 'focus', function( event ) {
            $( event.currentTarget ).parent().addClass('focus');
        });

        // blur click
        this.on( this.attr.fields, 'blur', function( event ) {
            $( event.currentTarget ).parent().removeClass('focus');
        });

        // set a selected text
        this.on( '.select-wrap .field', 'change', this.selectText );
        this.on( '.upload-wrap .field', 'change', this.uploadImage );
    };
});

export default pageInfoComponent;