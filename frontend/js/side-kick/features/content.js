// base component
import baseBox from 'side-kick/features/components/base-box';

// child components
import fileFieldComponent from 'side-kick/features/components/file-field';
import textFieldComponent from 'side-kick/features/components/text-field';


const contentFeature = baseBox.mixin(function box() {
  this.attributes({
    logoField: '.content_logo',
    titleField: '.content_title',
    subTitleField: '.content_sub_title',
    descriptionField: '.content_description',
  });

  this.after('initialize', () => {
    // Logo
    this.attachChild(fileFieldComponent, this.select('logoField'), {
      fieldName: 'content_logo',
      toValidate: ['file_size', 'file_format'],
    });

    // Title
    this.attachChild(textFieldComponent, this.select('titleField'), {
      fieldName: 'content_title',
    });

    // Sub-title
    this.attachChild(textFieldComponent, this.select('subTitleField'), {
      fieldName: 'content_sub_title',
    });

    // Description
    this.attachChild(textFieldComponent, this.select('descriptionField'), {
      fieldName: 'content_description',
    });
  });
});

contentFeature.attachTo('.feature.content');
