var elixir = require('laravel-elixir');
var path = require('path');

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

    // front page
    mix
        .images( null, null, {
            sizes: [[ 1440 ]],
            webp: false
        } )
        .sass('app.scss')
        .webpack('app.js');

    // side kick
    mix
        .sass('side-kick.scss')
        .webpack('side-kick.js');
});
