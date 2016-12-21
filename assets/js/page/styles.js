// var css = new StyleSheet();
// var css = StyleSheet('additional');

// console.log( 'find a rule:', css('.background') );
// console.log( 'find rule\'s property:', css('.background', 'backgroundImage') );
// console.log( 'delete rule\'s property:', css('.background', 'backgroundImage', '') );
// console.log( 'set rule\'s property:', css('.background', 'backgroundImage', 'url("/static/images/backgrounds/001.jpeg")') );
// console.log( 'delete a rule:', css('.background', '') );
// console.log( 'set a rule with properties object:', css('.background', {
//     'backgroundColor': '#fff',
//     'color': '#000'
// }) );

function StyleSheet( stylesheetTitle ) {
    this.CSSOM = this.findStyle( stylesheetTitle );

    return this.select.bind(this);
}

StyleSheet.prototype.CSSOM = null;
StyleSheet.prototype.findStyle = function( cssClass ) {
    for ( var index = 0; index < document.styleSheets.length; index++ ) {

        var cssom = document.styleSheets[ index ];

        if ( cssom.ownerNode.className === 'css-' + cssClass ) {
            return cssom;
        }
    }
};
StyleSheet.prototype.findRuleIndex = function( selector ) {
    var rules = this.CSSOM.cssRules,
        ruleIndex = null;

    for ( var index = 0; index < rules.length; index++ ) {
        if ( rules[ index ].selectorText === selector ) {
            ruleIndex = index;
        }
    }

    return ruleIndex;

};
StyleSheet.prototype.select = function( selector, property, value ) {
    var ruleIndex = this.findRuleIndex( selector );

    if ( null !== ruleIndex ) {
        var rule = this.CSSOM.cssRules[ ruleIndex ];

        switch ( typeof property ) {
            case 'undefined':
                return rule;
                break;
            case 'string':
                if ( '' === property ) {
                    this.CSSOM.deleteRule( ruleIndex );
                    return this.CSSOM;
                } else if ( undefined === value ) {
                    return rule.style[ property ];
                } else {
                    rule.style[ property ] = value;
                    return rule;
                }
                break;
            case 'object':
                for ( var key in property ) {
                    rule.style[ key ] = property[ key ];
                }
                return rule;
                break;
        }
    }
};

export default StyleSheet;