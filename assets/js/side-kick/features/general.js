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
        'fileNameField': '.general_file_name .field'
    });

    this.after('initialize', function() {
        this.select('fileNameField').on( 'keyup keypress blur', utils.throttle( fileNameSave.bind(this), 250 ) );
    });

    function fileNameSave( event ) {
        var element = event.currentTarget,
            value = element.value.trim();

        if ( this.validate( 'name', value ) ) {
            console.log( value );
            this.removeClassError( element );
        } else {
            this.addClassError( element );
        }
    }
});

featureGeneral.attachTo( '.features .general' );