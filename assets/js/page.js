jQuery( document ).ready(function ( $ ) {
    $('.newsletter').on('submit', function( event ) {
        var emailAdress = $(this).children('.email').val().trim();

        function isEmail( address ) {
            return /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/.test( address );
        }

        if ( ! emailAdress.length || ! isEmail( emailAdress ) ) {
            event.preventDefault();
        }
    });
});