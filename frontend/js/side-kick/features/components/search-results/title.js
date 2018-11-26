import textFieldComponent from 'side-kick/features/components/text-field';

export default textFieldComponent.mixin(function searchPreview() {
  this.attributes({
    changedContentTitle: null,
  });

  this.after('initialize', function initialize() {
    this.on(document, this.attr.changedContentTitle, this.changeTitlePlaceholder.bind(this));
  });

  this.changeTitlePlaceholder = function changeTitlePlaceholder(event, { value }) {
    this.select('field').attr('placeholder', value);

    if (!this.select('field').val().length) {
      this.trigger(document, `placeholderChanged_${this.attr.fieldName}`, { placeholder: value });
    }
  };
});
