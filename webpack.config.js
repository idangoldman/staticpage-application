var path = require('path');

module.exports = {
  watch: false,
  cache: false,
  debug: false,
  devtool: 'none',
  entry: {
    'page-intervention': './frontend/js/page/intervention.js',
    'side-kick': './frontend/js/side-kick/index.js',
    'home': './frontend/js/home.js'
  },
  output: {
    filename: '[name].js'
  },
  resolve: {
    root: path.resolve(__dirname, 'frontend/js')
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: 'babel',
        query: {
          presets: ['es2015']
        }
      },
      {
        test: /(node_modules\/flightjs)/,
        loader: 'imports-loader?$=jquery'
      },
      {
        test: /(node_modules\/air-datepicker\/dist\/js)/,
        loader: 'imports-loader?jQuery=jquery'
      },
      {
        test: /\.(njk|nunjucks)$/,
        loader: 'nunjucks-loader'
      }
    ]
  }
};
