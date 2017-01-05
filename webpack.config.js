var path = require("path");

module.exports = {
    watch: true,
    cache: false,
    debug: true,
    devtool: 'source-map',
    entry: {
        'page-intervention': './assets/js/page/intervention.js',
        'side-kick': './assets/js/side-kick/index.js',
        'home': './assets/js/home.js'
    },
    output: {
        filename: '[name].js'
    },
    resolve: {
        root: path.resolve( __dirname, 'assets/js' ),
        modulesDirectories: [
            'web_modules',
            'node_modules',
            'bower_components'
        ]
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel',
                query: {
                    presets: [ 'es2015' ]
                }
            },
            {
                test: /\.(njk|nunjucks)$/,
                loader: 'nunjucks-loader'
            }
        ]
    }
}
