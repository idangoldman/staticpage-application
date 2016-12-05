module.exports = {
    debug: true,
    devtool: 'source-map',
    entry: {
        'side-kick': './assets/js/side-kick.js',
        'home': './assets/js/home.js'
    },
    output: {
        filename: "[name].js"
    },
    resolve: {
        modulesDirectories: [
            "web_modules",
            "node_modules",
            "bower_components"
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