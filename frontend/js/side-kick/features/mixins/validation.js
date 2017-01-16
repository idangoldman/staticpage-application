import $ from 'jquery';

let regexPatterns = {
    'name': /^[a-zA-Z0-9_]*$/,
    'hex_color': /^#([0-9a-f]{3}|[0-9a-f]{6})$/i,
    'ua_code': /^ua-\d{4,10}-\d{1,4}$/i
    // https://regex101.com/r/fK9mY3/1
    // 'css': /([#.@]?[\w.:> ]+)[\s]?{[\r\n]?([A-Za-z\- \r\n\t]+[:][\s]*[\w .\/()\-!]+;[\r\n]*)*}/gi
};

var withValidation = function mixin() {
    this.attributes({
        'validationEL': '.validation',

        'errorClass': '',
        'toValidate': []
    });

    this.after('initialize', function() {
        // var attrs = this.attr;
        // this.select('validationEL').children().each(function() {
        //     attrs.toValidate.push( this.className );
        // });

        this.before('validate', this.removeErrorClass);
        this.after('validate', this.addErrorClass);
    });

    this.valueIsNotEmpty = function( value ) {
        var isNotEmpty = false;

        switch ( typeof value ) {
            case 'string':
                isNotEmpty = !! value.trim().length;
                break;
            case 'object':
                isNotEmpty = ! $.isEmptyObject( value );
                break;

        }

        return !! isNotEmpty;
    };

    this.validate = function( value ) {
        var isValid = true;

        if ( !! this.attr.toValidate.length && this.valueIsNotEmpty( value ) ) {

            this.attr.toValidate.some(function( rule ) {
                switch ( rule ) {
                    case 'css':
                    case 'hex_color':
                    case 'ua_code':
                        isValid = this.regexValidation( rule, value );
                        break;
                    case 'file_format':
                        isValid = this.isFileFormatAccepted( value.type );
                        break;
                    case 'file_size':
                        isValid = this.isFileSizeAccepted( value.size );
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
        if (patternName === 'css') {
            console.log(regexPatterns[ patternName ].test( value ));
        }
        return regexPatterns[ patternName ].test( value );
    };

    this.isFileFormatAccepted = function( fileFormat ) {
        var acceptedFormats = this.select('field').attr('accept').split(/,\s?/g);

        return acceptedFormats.indexOf( fileFormat ) !== -1;
    };

    this.isFileSizeAccepted = function( fileSize ) {
        var acceptedSize = this.select('field').attr('data-accept-size');

        return acceptedSize >= fileSize;
    };
};

export default withValidation;
