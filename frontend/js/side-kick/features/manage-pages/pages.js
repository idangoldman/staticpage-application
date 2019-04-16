import selectFieldComponent from 'side-kick/components/select-field';

export default selectFieldComponent.mixin(function pagesList() {
  this.updateField = function updateField(state, previousState) {
    if (previousState.value !== state.value) {
      window.top.location.href = state.value;
    }
  };
});
