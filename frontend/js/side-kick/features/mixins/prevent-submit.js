export default function withPreventSubmit() {
  this.attributes({
    form: 'form',
  });

  this.after('initialize', () => {
    this.select('form').on('submit', (event) => {
      event.preventDefault();
    });
  });
}
