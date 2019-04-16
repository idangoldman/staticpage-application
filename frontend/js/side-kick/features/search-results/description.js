import textFieldComponent from 'side-kick/components/text-field';

export default textFieldComponent.mixin(function searchPreview() {
  this.attributes({
    changedContentSubTitle: null,
  });

  this.after('initialize', function initialize() {
    this.on(
      document,
      this.attr.changedContentSubTitle,
      this.changeDescriptionPlaceholder.bind(this),
    );
  });

  this.changeDescriptionPlaceholder = function changeDescriptionPlaceholder(event, { value }) {
    this.select('field').attr('placeholder', value);

    if (!this.select('field').val().length) {
      this.trigger(document, `placeholderChanged_${this.attr.fieldName}`, { placeholder: value });
    }
  };
});
