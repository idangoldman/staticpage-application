import $ from 'jquery';
import { component, utils } from 'imports?$=jquery!flightjs';

// mixins
import withFocus from 'side-kick/features/mixins/focus';
import withSelect from 'side-kick/features/mixins/select';
import withToggle from 'side-kick/features/mixins/toggle';
import withValidation from 'side-kick/features/mixins/validation';


var generalFeature = component( withFocus, withSelect, withToggle, withValidation, function() {
    this.attributes({
        'fileNameField': '.general_file_name .field',
        'fileNameEventName': 'updateField_general_file_name_success'
    });

    this.after('initialize', function() {
        this.select('fileNameField').on( 'keyup keypress blur', utils.throttle( fileNameSave.bind(this), 250 ) );

        // this.on( document, this.attr.fileNameEventName, function(event) {
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

generalFeature.attachTo( '.feature.general' );