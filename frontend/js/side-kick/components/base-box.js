import { component } from 'flightjs';

// mixins
import withChildComponents from 'flight-with-child-components';
import withToggle from 'side-kick/components/mixins/toggle';
import withPreventSubmit from 'side-kick/components/mixins/prevent-submit';

export default component(withChildComponents, withToggle, withPreventSubmit);
