import $ from 'jquery';

var withPreventSubmit = function mixin() {
    this.attributes({
        'form': 'form',
    });

    this.after('initialize', function() {
        this.select('form').on( 'submit', function( event ) {
            event.preventDefault();
        } );
    });
};

export default withPreventSubmit;
