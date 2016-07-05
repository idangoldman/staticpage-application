var elixir = require('laravel-elixir');

require('laravel-elixir-images');
require('laravel-elixir-webpack');

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
    mix
        .images( null, null, {
            sizes: [[1440]],
            webp: false
        } )
        .sass('app.scss')
        .webpack('app.js');
});
