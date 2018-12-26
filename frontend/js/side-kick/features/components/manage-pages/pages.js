import selectFieldComponent from 'side-kick/features/components/select-field';

export default selectFieldComponent.mixin(function searchPreview() {
  this.updateField = function updateField(state, previousState) {
    if (previousState.value !== state.value) {
      console.log('updateField', state.value);
    }
  };
});
