import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var withSelect = function mixin() {
    this.attributes({
        focusField: '.field',
    });

    this.after('initialize', function() {
        // focus click
        this.select('focusField').on( 'focus', this.focus );

        // blur click
        this.select('focusField').on( 'blur', this.blur );
    });

    this.focus = function( event ) {
        $( event.currentTarget )
            .parent()
                .addClass('focus');
    }

    this.blur = function( event ) {
        $( event.currentTarget )
            .parent()
                .removeClass('focus');
    }

};

export default withSelect;