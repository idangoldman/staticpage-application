import $ from 'jquery';

const regexPatterns = {
  name: /^[a-zA-Z0-9_]*$/,
  hex_color: /^#([0-9a-f]{3}|[0-9a-f]{6})$/i,
  ua_code: /^ua-\d{4,10}-\d{1,4}$/i,
  url: /(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,12}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/,
  // https://regex101.com/r/fK9mY3/1
  // 'css': /([#.@]?[\w.:> ]+)[\s]?{[\r\n]?([A-Za-z\- \r\n\t]+[:][\s]*[\w .\/()\-!]+;[\r\n]*)*}/gi
};

const withValidation = function mixin() {
  this.attributes({
    validationEL: '.validation',

    errorClass: '',
    toValidate: [],
  });

  this.after('initialize', function initialize() {
    // var attrs = this.attr;
    // this.select('validationEL').children().each(function() {
    //     attrs.toValidate.push( this.className );
    // });

    this.before('validate', this.removeErrorClass);
    this.after('validate', this.addErrorClass);
  });

  this.valueIsNotEmpty = function valueIsNotEmpty(value) {
    let isNotEmpty = false;

    switch (typeof value) {
      case 'string':
      default:
        isNotEmpty = !!value.trim().length;
        break;
      case 'object':
        isNotEmpty = !$.isEmptyObject(value);
        break;
    }

    return !!isNotEmpty;
  };

  this.validate = function validate(value) {
    let isValid = true;

    if (!!this.attr.toValidate.length && this.valueIsNotEmpty(value)) {
      this.attr.toValidate.some(function callback(rule) {
        switch (rule) {
          case 'css':
          case 'hex_color':
          case 'ua_code':
          case 'url':
          default:
            isValid = this.regexValidation(rule, value);
            break;
          case 'file_format':
            isValid = this.isFileFormatAccepted(value.type);
            break;
          case 'file_size':
            isValid = this.isFileSizeAccepted(value.size);
            break;
        }

        if (!isValid) {
          this.attr.errorClass = rule;
          return true;
        }

        return false;
      });
    }

    return isValid;
  };

  this.addErrorClass = function addErrorClass() {
    if (this.attr.errorClass.length) {
      this.select('validationEL')
        .children(`.${this.attr.errorClass}`)
        .addClass('error');

      this.attr.errorClass = '';
    }
  };

  this.removeErrorClass = function removeErrorClass() {
    this.select('validationEL')
      .children()
      .removeClass('error');
  };

  this.regexValidation = function regexValidation(patternName, value) {
    if (patternName === 'css') {
      // console.log(regexPatterns[patternName].test(value));
    }
    return regexPatterns[patternName].test(value);
  };

  this.isFileFormatAccepted = function isFileFormatAccepted(fileFormat) {
    const acceptedFormats = this.select('field').attr('accept').split(/,\s?/g);

    return acceptedFormats.indexOf(fileFormat) !== -1;
  };

  this.isFileSizeAccepted = function isFileSizeAccepted(fileSize) {
    const acceptedSize = this.select('field').attr('data-accept-size');

    return acceptedSize >= fileSize;
  };
};

export default withValidation;
