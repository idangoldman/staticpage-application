import $ from 'jquery';
import { component } from 'flightjs';


export default component( function searchPreview() {

    this.attributes({
        'titleEl': '.link-title',
        'descriptionEl': '.description',

        'changedTitleEvent': null,
        'changedDescriptionEvent': null,
        'changedPlaceholderTitleEvent': null,
        'changedPlaceholderDescriptionEvent': null
    });

    this.after('initialize', function() {
        this.on( document, this.attr.changedTitleEvent, this.changeTitle.bind(this) );
        this.on( document, this.attr.changedDescriptionEvent, this.changeDescription.bind(this) );
        this.on( document, this.attr.changedPlaceholderTitleEvent, this.changeTitle.bind(this) );
        this.on( document, this.attr.changedPlaceholderDescriptionEvent, this.changeDescription.bind(this) );
    });

    this.changeTitle = function( event, { value, placeholder } ) {
        this.select('titleEl').html( value || placeholder );
    };

    this.changeDescription = function( event, { value, placeholder } ) {
        this.select('descriptionEl').html( value || placeholder );
    };
});
