import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var withSelect = function mixin() {
    this.attributes({
        focusField: '.field',
    });

    this.after('initialize', function() {
        // focus click
        this.select('focusField').on( 'focus', focus );

        // blur click
        this.select('focusField').on( 'blur', blur );
    });

    function focus( event ) {
        $( event.currentTarget )
            .parent()
                .addClass('focus');
    }

    function blur( event ) {
        $( event.currentTarget )
            .parent()
                .removeClass('focus');
    }

};

export default withSelect;