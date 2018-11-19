import textFieldComponent from 'side-kick/features/components/text-field';

export default textFieldComponent.mixin(function searchPreview() {
  this.attributes({
    changedContentSubTitle: null,
  });

  this.after('initialize', () => {
    this.on(
      document,
      this.attr.changedContentSubTitle,
      this.changeDescriptionPlaceholder.bind(this),
    );
  });

  this.changeDescriptionPlaceholder = (event, { value }) => {
    this.select('field').attr('placeholder', value);

    if (!this.select('field').val().length) {
      this.trigger(document, `placeholderChanged_${this.attr.fieldName}`, { placeholder: value });
    }
  };
});
