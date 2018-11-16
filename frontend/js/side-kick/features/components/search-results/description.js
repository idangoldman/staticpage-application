import $ from 'jquery';
import { component } from 'flightjs';

import textFieldComponent from 'side-kick/features/components/text-field';


export default textFieldComponent.mixin( function searchPreview() {
    this.attributes({
        'changedContentSubTitleEvent': null
    });

    this.after('initialize', function() {
        this.on( document, this.attr.changedContentSubTitleEvent, this.changeDescriptionPlaceholder.bind(this) );
    });

    this.changeDescriptionPlaceholder = function( event, { value } ) {
        this.select('field').attr( 'placeholder', value );

        if ( ! this.select('field').val().length ) {
            this.trigger( document, 'placeholderChanged_' + this.attr.fieldName, { placeholder: value } )
        }
    };
});
