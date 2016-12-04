import $ from 'jquery';

var withValidation = function mixin() {
    this.attributes({
        'fieldParent': '.fieldset',
    });

    this.validate = function( type, value ) {
        var regex = {
            'name': /^[a-zA-Z0-9_]*$/
        };

        value = typeof value === 'string' ? value.trim() : '';

        return regex[type].test( value );
    };

    this.addClassError = function( element ) {
        console.log('fail.');
        $( element )
            .parents( this.attr.fieldParent )
                .addClass('error');
    };

    this.removeClassError = function( element ) {
        $( element )
            .parents( this.attr.fieldParent )
                .removeClass('error');
    };
};

export default withValidation;