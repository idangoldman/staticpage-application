import $ from 'jquery';

var withSelect = function mixin() {
    this.attributes({
        'optionSelected': 'option:selected',
        'selectField': '.select-wrap .field',
        'selectTextField': '.selected-text'
    });

    this.after('initialize', function() {
        // set a selected text
        this.select('selectField').on('change', selectText.bind(this) );
    });

    function selectText( event ) {
        // event could be a dom element as well.
        var $element = $( event.currentTarget || event[0] );

        $element
            .parent()
                .children( this.attr.selectTextField )
                    .html(
                        $element.find( this.attr.optionSelected ).text()
                    );
    }
};

export default withSelect;