import { component } from 'flightjs';

export default component(function searchPreview() {
  this.attributes({
    titleEl: '.link-title',
    descriptionEl: '.description',

    changedTitle: null,
    changedDescription: null,
    changedPlaceholderTitle: null,
    changedPlaceholderDescription: null,
  });

  this.after('initialize', () => {
    this.on(document, this.attr.changedTitle, this.changeTitle.bind(this));
    this.on(document, this.attr.changedDescription, this.changeDescription.bind(this));
    this.on(document, this.attr.changedPlaceholderTitle, this.changeTitle.bind(this));
    this.on(document, this.attr.changedPlaceholderDescription, this.changeDescription.bind(this));
  });

  this.changeTitle = (event, { value, placeholder }) => {
    this.select('titleEl').html(value || placeholder);
  };

  this.changeDescription = (event, { value, placeholder }) => {
    this.select('descriptionEl').html(value || placeholder);
  };
});
