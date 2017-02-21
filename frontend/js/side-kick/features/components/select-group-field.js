import selectField from 'side-kick/features/components/select-field';

export default selectField.mixin( function selectGroupField() {

    this.after('initialize', function() {
        this.select('field').on( 'change', this.changeGroup.bind( this ) );

        if ( this.state.value ) {
            this.showGroup( this.state.value );
        }
    });

    this.changeGroup = function( event ) {
        this.showGroup( event.currentTarget.value );
    };

    this.showGroup = function( value ) {
        var groupClass = '';

        if ( value.length ) {
            groupClass = '.' + value;
        }

        this.$node
                .parents('form')
                .find('.group')
                    .slideUp()
                    .filter( groupClass )
                    .slideDown();
    };

});
