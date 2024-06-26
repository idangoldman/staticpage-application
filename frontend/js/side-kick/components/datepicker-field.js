import { component } from 'flightjs';
import 'air-datepicker/dist/js/datepicker.min';
import 'air-datepicker/dist/js/i18n/datepicker.en';

import withFocus from 'side-kick/components/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/components/mixins/validation';


export default component(withFocus, withState, withValidation, function datePickerField() {
  this.attributes({
    field: '.field',
    fieldName: null,
    closeIcon: '.icon.close',

    startDate: new Date(new Date().getTime() + 24 * 60 * 60 * 1000), // 24 Hours ahead
    datePicker: {},
  });

  this.initialState({
    name: this.fromAttr('fieldName'),
    value() {
      return this.select('field').val();
    },
  });

  this.after('initialize', function initialize() {
    this.select('field').on('fieldChanged', this.fieldChanged.bind(this));
    this.select('closeIcon').on('click', this.fieldClear.bind(this));

    this.after('stateChanged', this.updateField);

    this.attr.datePicker = this.initDatePicker();
  });

  this.fieldChanged = function fieldChanged(event) {
    const value = event.currentTarget.value.trim();

    this.toggleFilledClass(value);
    this.mergeState({ value });
  };

  this.fieldClear = function fieldChanged() {
    this.attr.datePicker.clear();
    this.select('field').trigger('fieldChanged');
  };

  this.updateField = function updateField(state, previousState) {
    if (previousState.value !== state.value) {
      this.trigger(document, 'updateField', state);
    }
  };

  this.initDatePicker = function initDatePicker() {
    return this.select('field')
      .datepicker({
        language: 'en',
        minDate: new Date(),
        startDate: this.attr.startDate,
        dateFormat: 'yyyy/mm/dd',
        timeFormat: 'hh:ii',
        timepicker: true,
        onSelect: this.onSelect.bind(this),
        onShow: this.onShow.bind(this),
      })
      .data('datepicker');
  };

  this.onSelect = function onSelect() {
    this.select('field').trigger('fieldChanged');
  };

  this.onShow = function onShow(instance) {
    if (!instance.selectedDates.length) {
      const fieldValue = this.select('field').val();

      if (fieldValue.length) {
        this.attr.startDate = new Date(fieldValue);
      }

      instance.selectDate(this.attr.startDate);
    }
  };

  this.toggleFilledClass = function toggleFilledClass(value) {
    if (value.length) {
      this.select('field').addClass('filled');
    } else {
      this.select('field').removeClass('filled');
    }
  };
});
