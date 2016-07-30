import $ from 'jquery';
import flight, { component } from 'imports?$=jquery!flightjs';

var withSelectText = function mixin() {

    this.selectText = function( event ) {

        // event could be a dom element as well.
        var $element = $( event.currentTarget || event[0] );

        $element.parent().children('.selected-text').html(
            $element.find('option:selected').text()
        );
    }
};

export default withSelectText;