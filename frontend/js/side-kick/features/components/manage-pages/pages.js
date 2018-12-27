import selectFieldComponent from 'side-kick/features/components/select-field';

export default selectFieldComponent.mixin(function searchPreview() {
  this.updateField = function updateField(state, previousState) {
    if (previousState.value !== state.value) {
      window.top.location.href = state.value;
    }
  };
});
