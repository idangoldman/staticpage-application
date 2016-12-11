import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withFocus from './mixins/focus';
import withSelect from './mixins/select';
import withToggle from './mixins/toggle';
import withValidation from './mixins/validation';


var featureGeneral = component( withFocus, withSelect, withToggle, withValidation, function() {
    this.attributes({
        'fileTypeField': '.general_type_name .field',
        'fileNameField': '.general_file_name .field',
        'fileNameFieldName': 'general_file_name'
    });

    this.after('initialize', function() {
        this.select('fileNameField').on( 'keyup keypress blur', utils.throttle( fileNameSave.bind(this), 250 ) );

        // this.on( document, 'updateField_' + this.attr.fileNameFieldName + '_success', function(event) {
        //     console.log(event.type);
        // });
    });

    function fileNameSave( event ) {
        var element = event.currentTarget,
            name = element.name,
            value = element.value.trim();

        if ( this.validate( 'name', value ) ) {
            this.trigger( document, 'updateField', { name, value } );
            this.removeClassError( element );
        } else {
            this.addClassError( element );
        }
    }
});

featureGeneral.attachTo( '.features .general' );