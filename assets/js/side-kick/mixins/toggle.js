import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var withToggle = function mixin() {
    this.attributes({
        'toggleBox': '.body',
        'toggleClass': 'close',
        'toggleClick': '.header'
    });

    this.after('initialize', function() {
        // toggle feature box
        this.select('toggleClick').on( 'click', this.toggle.bind(this) );
    });

    this.toggle = function( event ) {
        $( event.currentTarget )
            .toggleClass( this.attr.toggleClass )
            .parent()
                .children( this.attr.toggleBox )
                    .slideToggle();
    }
};

export default withToggle;