import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';
import template from 'views/side-kick/features/page-info.njk';

var pageInfoComponent = component( function application() {
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
        this.selectText( this.select('typeSelect') )

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

    this.selectText = function( event ) {

        // event could be a dom element as well.
        var $element = $( event.currentTarget || event[0] );

        $element.parent().children('.selected-text').html(
            $element.find('option:selected').text()
        );
    }

    this.uploadImage = function( event ) {
        var $element = $( event.currentTarget );

        if ( !! $element[0].files.length ) {
            var file = $element[0].files[0],
                imageTypes = [
                    'image/png',
                    'image/gif',
                    'image/jpg',
                    'image/webp'
                ],
                megabyte = 1024000;

            // set file name text
            $element
                .parent()
                    .children('.file-name').html( file.name );

            // check for image file type
            if ( imageTypes.indexOf( file.type ) === -1 ) {
                this.select('logoMessage')
                    .addClass('red')
                    .html(
                        'File type "' + file.type + '" doesn\'t supported.'
                    );

                return false;
            } else {
                this.select('logoMessage')
                    .removeClass('red')
                    .html(
                        'Upload gif, jpg, and png only, up to 1MB.'
                    );
            }

            // check for image size
            if ( file.size > megabyte ) {
                this.select('logoMessage')
                    .addClass('red')
                    .html(
                        'File size greater than 1024KB.'
                    );

                return false;
            } else {
                this.select('logoMessage')
                    .removeClass('red')
                    .html(
                        'Upload gif, jpg, and png only, up to 1MB.'
                    );
            }
        }
    }
});

export default pageInfoComponent;