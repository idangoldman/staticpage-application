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

    return this.select.bind( this );
}

StyleSheet.prototype.CSSOM = null;
StyleSheet.prototype.findStyle = function( cssClass ) {
    var CSSOM = null,
        prefix = 'css-';

    for ( var index = 0; index < document.styleSheets.length; index++ ) {

        var styleSheet = document.styleSheets[ index ];

        if ( styleSheet.ownerNode.className === prefix + cssClass ) {
            CSSOM = styleSheet;
            break;
        }
    }

    if ( null === CSSOM ) {
        var newStyleSheet = document.createElement('style');
        newStyleSheet.className = prefix + cssClass;
        document.getElementsByTagName('head')[ 0 ].appendChild( newStyleSheet );
        CSSOM = document.styleSheets[ document.styleSheets.length - 1 ];
    }

    return CSSOM
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

StyleSheet.prototype.addRule = function( selector, property, value ) {
    var newRule, ruleIndex;

    switch( typeof property ) {
        case 'string':
            newRule = [ selector, '{', property, ':', value, ';', '}' ];
            break;

        case 'object':
            newRule = [ selector, '{' ];

            for ( var key in property ) {
                newRule.push( key, ':', property[ key ], ';' );
            }

            newRule.push('}');
            break;
    }

    ruleIndex = this.CSSOM.insertRule( newRule.join(''), this.CSSOM.cssRules.length );

    return this.CSSOM.cssRules[ ruleIndex ];
};

StyleSheet.prototype.select = function( selector, property, value ) {
    var ruleIndex = this.findRuleIndex( selector ),
        output = null;

    if ( null === ruleIndex ) {
        output = this.addRule( selector, property, value );
    } else {
        var rule = this.CSSOM.cssRules[ ruleIndex ];

        switch ( typeof property ) {
            case 'undefined':
                output = rule;
                break;

            case 'string':
                if ( '' === property ) {
                    this.CSSOM.deleteRule( ruleIndex );
                    output = this.CSSOM;
                } else if ( undefined === value ) {
                    output = rule.style[ property ];
                } else {
                    rule.style[ property ] = value;
                    output = rule;
                }
                break;

            case 'object':
                for ( var key in property ) {
                    rule.style[ key ] = property[ key ];
                }

                output = rule;
                break;
        }
    }

    return output;
};

export default StyleSheet;
