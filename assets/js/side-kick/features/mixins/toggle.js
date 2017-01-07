import $ from 'jquery';

var withToggle = function mixin() {
    this.attributes({
        'toggleBox': '.body',
        'toggleClass': 'close',
        'toggleClick': '.header'
    });

    this.after('initialize', function() {
        // toggle feature box
        this.select('toggleClick').on( 'click', toggle.bind(this) );
    });

    function toggle( event ) {
        $( event.currentTarget )
            .toggleClass( this.attr.toggleClass )
            .parent()
                .children( this.attr.toggleBox )
                    .slideToggle();
    }
};

export default withToggle;