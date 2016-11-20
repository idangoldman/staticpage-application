jQuery( document ).ready(function ( $ ) {
    $('.newsletter').on('submit', function( event ) {
        var emailEl = $(this).children('#email');
        var emailAdress = emailEl.val().trim();

        function isEmail( address ) {
            return /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/.test( address );
        }

        if ( ! emailAdress.length || ! isEmail( emailAdress ) ) {
            emailEl.css({ 'border-color': '#f00' });
            event.preventDefault();
        }
    });
});