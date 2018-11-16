import $ from 'jquery';
import { component } from 'flightjs';

// mixins
import withChildComponents from 'flight-with-child-components' ;
import withToggle from 'side-kick/features/mixins/toggle';
import withPreventSubmit from 'side-kick/features/mixins/prevent-submit';

export default component( withChildComponents, withToggle, withPreventSubmit );
