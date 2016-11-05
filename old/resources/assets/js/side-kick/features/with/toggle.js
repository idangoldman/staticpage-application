import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var withToggle = function mixin() {

    this.toggle = function( event ) {
        $( event.currentTarget )
            .toggleClass('close')
            .parent()
                .children('.body')
                    .slideToggle();
    }
};

export default withToggle;