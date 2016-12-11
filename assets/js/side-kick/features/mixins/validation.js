import $ from 'jquery';

let cacheValue = '';

var withValidation = function mixin() {
    this.attributes({
        'fieldParent': '.fieldset',
    });

    this.validate = function( type, value ) {
        var valid = false,
            regex = {
                'name': /^[a-zA-Z0-9_]*$/
            };

        value = typeof value === 'string' ? value.trim() : '';

        if (value !== cacheValue && regex[type].test( value )) {
            cacheValue = value;
            valid = true;
        }

        return valid;
    };

    this.addClassError = function( element ) {
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