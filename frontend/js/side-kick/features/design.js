// base component
import baseBox from 'side-kick/components/base-box';

// child components
import fileFieldComponent from 'side-kick/components/file-field';
import textFieldComponent from 'side-kick/components/text-field';
import selectFieldComponent from 'side-kick/components/select-field';


const designFeature = baseBox.mixin(function box() {
  this.attributes({
    backgroundImageField: '.design_background_image',
    backgroundColorField: '.design_background_color',
    backgroundRepeatField: '.design_background_repeat',
    fontFamilyField: '.design_font_family',
    fontColorField: '.design_font_color',
    contentAlignmentField: '.design_content_alignment',
    contentDirectionField: '.design_content_direction',
    additionalStyleField: '.design_additional_styles',
  });

  this.after('initialize', function initialize() {
    // Background Image
    this.attachChild(fileFieldComponent, this.select('backgroundImageField'), {
      fieldName: 'design_background_image',
      toValidate: ['file_size', 'file_format'],
    });

    // Background Color
    this.attachChild(textFieldComponent, this.select('backgroundColorField'), {
      fieldName: 'design_background_color',
      toValidate: ['hex_color'],
    });

    // Background Repeat
    this.attachChild(selectFieldComponent, this.select('backgroundRepeatField'), {
      fieldName: 'design_background_repeat',
    });

    // Font Family
    this.attachChild(selectFieldComponent, this.select('fontFamilyField'), {
      fieldName: 'design_font_family',
    });

    // Font Color
    this.attachChild(textFieldComponent, this.select('fontColorField'), {
      fieldName: 'design_font_color',
      toValidate: ['hex_color'],
    });

    // Content Alignment
    this.attachChild(selectFieldComponent, this.select('contentAlignmentField'), {
      fieldName: 'design_content_alignment',
    });

    // Content Direction
    this.attachChild(selectFieldComponent, this.select('contentDirectionField'), {
      fieldName: 'design_content_direction',
    });

    // Additional Style
    this.attachChild(textFieldComponent, this.select('additionalStyleField'), {
      fieldName: 'design_additional_styles',
      // 'toValidate': ['css']
    });
  });
});

designFeature.attachTo('.feature.design');
