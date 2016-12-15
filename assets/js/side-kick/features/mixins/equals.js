import $ from 'jquery';

var withEquals = function mixin() {
    this.equals = function( obj1, obj2 ) {
        function _equals( obj1, obj2 ) {
            var clone = $.extend( true, {}, obj1 ),
                cloneStr = JSON.stringify( clone );
            return cloneStr === JSON.stringify( $.extend( true, clone, obj2 ) );
        }

        return _equals( obj1, obj2 ) && _equals( obj2, obj1 );
    };
};

export default withEquals;