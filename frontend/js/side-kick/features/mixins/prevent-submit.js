export default function withPreventSubmit() {
    this.attributes({
        'form': 'form',
    });

    this.after('initialize', function() {
        this.select('form').on( 'submit', function( event ) {
            event.preventDefault();
        } );
    });
};
