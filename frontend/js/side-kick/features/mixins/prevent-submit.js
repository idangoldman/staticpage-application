export default function withPreventSubmit() {
  this.attributes({
    form: 'form',
  });

  this.after('initialize', function initialize() {
    this.select('form').on('submit', (event) => {
      event.preventDefault();
    });
  });
}
