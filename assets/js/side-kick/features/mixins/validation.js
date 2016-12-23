import $ from 'jquery';

let regexPatterns = {
    'name': /^[a-zA-Z0-9_]*$/,
    'hex_color': /^#([0-9a-f]{3}|[0-9a-f]{6})$/i
};

var withValidation = function mixin() {
    this.attributes({
        'validationEL': '.validation',

        'errorClass': '',
        'toValidate': []
    });

    this.after('initialize', function() {
        var attrs = this.attr;

        this.select('validationEL').children().each(function() {
            attrs.toValidate.push( this.className );
        });

        this.before('validate', this.removeErrorClass);
        this.after('validate', this.addErrorClass);
    });

    this.validate = function( value ) {
        var isValid = true;
        if ( !! this.attr.toValidate.length && !! value.trim().length ) {

            this.attr.toValidate.some(function( rule ) {
                switch ( rule ) {
                    case 'hex_color':
                        isValid = this.regexValidation( 'hex_color', value );
                        break;
                }

                if ( ! isValid ) {
                    this.attr.errorClass = rule;
                    return true;
                }
            }.bind( this ));
        }

        return isValid;
    };

    this.addErrorClass = function() {
        if ( this.attr.errorClass.length ) {
            this.select('validationEL')
                .children('.' + this.attr.errorClass)
                .addClass('error');

            this.attr.errorClass = '';
        }
    };

     this.removeErrorClass = function() {
        this.select('validationEL')
            .children()
            .removeClass('error');
    };

    this.regexValidation = function( patternName, value ) {
        return regexPatterns[ patternName ].test( value );
    };
};

export default withValidation;