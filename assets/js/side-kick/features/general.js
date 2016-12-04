import flight, { component } from 'imports?$=jquery!flightjs';

// mixins
import withSelect from '../mixins/select';
import withToggle from '../mixins/toggle';
import withFocus from '../mixins/focus';


var featureGeneral = component( withFocus, withToggle, withSelect, function() {
    this.attributes({
        field: '.field',
    });

    this.after('initialize', function() {
    });
});

featureGeneral.attachTo( '.features .general' );