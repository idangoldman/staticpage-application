import { component } from 'flightjs';

import withFocus from 'side-kick/components/mixins/focus';
import withState from 'flight-with-state';
import withValidation from 'side-kick/components/mixins/validation';

export default component(withFocus, withState, withValidation, function fileField() {
  this.attributes({
    field: '.field',
    fieldName: null,
    choosenFileName: '.choosen-file-name',
    closeIcon: '.icon.close',
  });

  this.initialState({
    name: this.fromAttr('fieldName'),
    base64: '',
    value: '',
  });

  this.after('initialize', function initialize() {
    this.select('field').on('change', this.fieldChanged.bind(this));
    this.select('closeIcon').on('click', this.resetField.bind(this));

    this.after('stateChanged', this.updateField);

    this.on(document, `updateField_${this.attr.fieldName}_success`, this.updateFileName.bind(this));
    // this.on( document, 'updateField_' + this.attr.fieldName + '_error', console.log('Nay!'));
  });

  this.fieldChanged = function fieldChanged(event) {
    const file = this.setFile(event.currentTarget);

    if (file.name !== 'empty') {
      this.getFileContent(file)
        .then((rawFile) => {
          this.setChoosenFileName(file.name);
          this.mergeState({
            base64: rawFile,
            value: file,
          });
        });
      // .catch(function callback() {
      //   console.log('something went wrong...')
      // });
    }
  };

  this.updateField = function updateField(state) {
    this.trigger(document, 'updateField', state);
  };

  this.resetField = function resetField() {
    this.removeErrorClass();
    this.setChoosenFileName('');
    this.mergeState({
      base64: '',
      value: '',
    });
  };

  this.updateFileName = function updateFileName(event, data) {
    const fileName = data.value.split('/').pop();
    this.setChoosenFileName(fileName);
  };

  this.setChoosenFileName = function setChoosenFileName(fileName) {
    this.select('choosenFileName').html(fileName);
  };

  this.setFile = function setFile(element) {
    let file = new File([], 'empty');

    if (element.files.length) {
      // eslint-disable-next-line prefer-destructuring
      file = element.files[0];
      // eslint-disable-next-line no-param-reassign
      element.value = '';
    }

    return file;
  };

  this.getFileContent = function getFileContent(file) {
    return new Promise((resolve, reject) => {
      const fileReader = new FileReader();

      if (!this.validate(file)) {
        reject();
      } else {
        fileReader.onload = function onload(event) {
          resolve(event.target.result);
        };

        fileReader.readAsDataURL(file);
      }
    });
  };
});
