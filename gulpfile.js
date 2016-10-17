var elixir = require('laravel-elixir');

require('laravel-elixir-images');
require('laravel-elixir-svg-symbols');
require('laravel-elixir-webpack');

var webpackConfig = {
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
};

/*
 |--------------------------------------------------------------------------
 | Elixir Asset Management
 |--------------------------------------------------------------------------
 |
 | Elixir provides a clean, fluent API for defining some basic Gulp tasks
 | for your Laravel application. By default, we are compiling the Sass
 | file for our application, as well as publishing vendor resources.
 |
 */

elixir(function( mix ) {


    // front page
    mix
        .images( null, null, {
            sizes: [ 1440, [ 1200, 630 ], [ 280, 150 ] ],
            webp: false
        } )
        .sass('app.scss')
        .webpack('app.js', webpackConfig);

    // side kick
    mix
        .sass('side-kick.scss')
        .svgSprite()
        .webpack('side-kick.js', webpackConfig);
});
