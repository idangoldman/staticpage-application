import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';
import template from 'views/side-kick/features/page-info.njk';

var pageInfoComponent = component( function application() {
    this.after('initialize', function() {
        this.$node.html(
            template.render()
        );

        // toggle feature box
        this.on('.header', 'click', function( event ) {
            $( event.currentTarget )
                .toggleClass('close')
                .parent()
                    .children('.body')
                        .slideToggle();
        });

        // focus click
        this.on('.field-wrap .field', 'focus', function( event ) {
            $( event.currentTarget ).parent().addClass('focus');
        });
        // blur click
        this.on('.field-wrap .field', 'blur', function( event ) {
            $( event.currentTarget ).parent().removeClass('focus');
        });
    });
});

export default pageInfoComponent;