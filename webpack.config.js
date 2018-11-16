var path = require("path");

export default = {
  watch: false,
  cache: false,
  debug: true,
  devtool: 'source-map',
  entry: {
    'page-intervention': './frontend/js/page/intervention.js',
    'side-kick': './frontend/js/side-kick/index.js',
    'home': './frontend/js/home.js'
  },
  output: {
    filename: '[name].js'
  },
  resolve: {
    root: path.resolve(__dirname, 'frontend/js'),
    modulesDirectories: [
      'web_modules',
      'node_modules',
      'bower_components'
    ],
    alias: {
      jquery: "jquery/dist/jquery.min"
    }
  module: {
},
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel',
        query: {
          presets: ['es2015']
        }
      },
      {
        test: /\.(njk|nunjucks)$/,
        loader: 'nunjucks-loader'
      }
    ]
  }
}
