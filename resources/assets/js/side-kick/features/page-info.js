import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

// template
import template from 'views/side-kick/features/page-info.njk';

// mixins
import withImageUpload from './with/image-upload';
import withSelectText from './with/select-text';

var pageInfoComponent = component( withSelectText, withImageUpload, function application() {
    this.attributes({
        typeSelect: '.fieldset.type .select-wrap .field',
        logoUpload: '.fieldset.logo .upload-wrap .field',
        logoMessage: '.fieldset.logo .message',
        fields: '.field'
    });

    this.after('initialize', function() {
        this.$node.html(
            template.render()
        );

        // set an init selected text
        // this.selectText( this.select('typeSelect') )

        // toggle feature box
        this.on('.header', 'click', function( event ) {
            $( event.currentTarget )
                .toggleClass('close')
                .parent()
                    .children('.body')
                        .slideToggle();
        });

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
    });
});

export default pageInfoComponent;