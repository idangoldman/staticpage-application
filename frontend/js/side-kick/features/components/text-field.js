import { component } from 'flightjs';

import withFocus from 'side-kick/features/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/features/mixins/validation';

export default component(withFocus, withState, withValidation, function textField() {
  this.attributes({
    field: '.field',
    message: '.message',

    fieldName: null,
  });

  this.initialState({
    name: this.fromAttr('fieldName'),
    value() {
      return this.select('field').val();
    },
  });

  this.after('initialize', () => {
    this.select('field').on('keyup keypress blur', this.fieldChanged.bind(this));

    this.after('stateChanged', this.updateField);
    // this.on( document, 'updateField_' + this.attr.fieldName + '_success', console.log('Yay!'));
    // this.on( document, 'updateField_' + this.attr.fieldName + '_error', console.log('Nay!'));
  });

  this.fieldChanged = (event) => {
    const value = event.currentTarget.value.trim();

    if (!this.validate(value)) {
      return true;
    }

    this.trigger(document, `fieldChanged_${this.attr.fieldName}`, {
      placeholder: this.select('field').attr('placeholder'),
      value,
    });

    this.mergeState({ value });

    return false;
  };

  this.updateField = (state, previousState) => {
    if (previousState.value !== state.value) {
      this.trigger(document, 'updateField', state);
    }
  };
});
