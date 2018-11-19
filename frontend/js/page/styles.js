// var css = new StyleSheet();
// var css = StyleSheet('additional');

// console.log( 'find a rule:', css('.background') );
// console.log( 'find rule\'s property:', css('.background', 'backgroundImage') );
// console.log( 'delete rule\'s property:', css('.background', 'backgroundImage', '') );
// console.log( 'set rule\'s property:', css('.background', 'backgroundImage',
// 'url("/static/images/backgrounds/001.jpeg")') );
// console.log( 'delete a rule:', css('.background', '') );
// console.log( 'set a rule with properties object:', css('.background', {
//     'backgroundColor': '#fff',
//     'color': '#000'
// }) );

function StyleSheet(stylesheetTitle) {
  this.CSSOM = this.findStyle(stylesheetTitle);

  return this.select.bind(this);
}

StyleSheet.prototype.CSSOM = null;
StyleSheet.prototype.findStyle = function findStyle(cssClass) {
  let CSSOM = null;


  const prefix = 'css-';

  for (let index = 0; index < document.styleSheets.length; index += 1) {
    const styleSheet = document.styleSheets[index];

    if (styleSheet.ownerNode.className === prefix + cssClass) {
      CSSOM = styleSheet;
      break;
    }
  }

  if (CSSOM === null) {
    const newStyleSheet = document.createElement('style');
    newStyleSheet.className = prefix + cssClass;
    document.getElementsByTagName('head')[0].appendChild(newStyleSheet);
    CSSOM = document.styleSheets[document.styleSheets.length - 1];
  }

  return CSSOM;
};

StyleSheet.prototype.findRuleIndex = function findRuleIndex(selector) {
  const rules = this.CSSOM.cssRules;


  let ruleIndex = null;

  for (let index = 0; index < rules.length; index += 1) {
    if (rules[index].selectorText === selector) {
      ruleIndex = index;
    }
  }

  return ruleIndex;
};

StyleSheet.prototype.addRule = function addRule(selector, property, value) {
  let newRule;


  let ruleIndex = this.CSSOM.cssRules.length;

  switch (typeof property) {
    case 'string':
      newRule = [selector, '{', property, ':', value, ';', '}'];
      break;

    case 'object':
      newRule = [selector, '{'];

      Object.keys(property).forEach((key) => {
        newRule.push(key, ':', property[key], ';');
      });

      newRule.push('}');
      break;

    case 'undefined':
      if (selector.length) {
        newRule = [selector];
        ruleIndex = 0;
      }
      break;
    default: break;
  }

  ruleIndex = this.CSSOM.insertRule(newRule.join(''), ruleIndex);

  return this.CSSOM.cssRules[ruleIndex];
};

StyleSheet.prototype.select = function select(selector, property, value) {
  const ruleIndex = this.findRuleIndex(selector);


  let output = null;

  if (ruleIndex === null) {
    output = this.addRule(selector, property, value);
  } else {
    const rule = this.CSSOM.cssRules[ruleIndex];

    switch (typeof property) {
      case 'undefined':
        output = rule;
        break;

      case 'string':
        if (property === '') {
          this.CSSOM.deleteRule(ruleIndex);
          output = this.CSSOM;
        } else if (undefined === value) {
          output = rule.style[property];
        } else {
          rule.style[property] = value;
          output = rule;
        }
        break;

      case 'object':
        Object.keys(property).forEach((key) => {
          rule.style[key] = property[key];
        });

        output = rule;
        break;
      default: break;
    }
  }

  return output;
};

export default StyleSheet;
