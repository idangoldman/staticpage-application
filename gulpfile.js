var argv = require('yargs').argv,
    autoprefixer = require('autoprefixer'),
    del = require('del'),
    gulp = require('gulp'),
    imageMin = require('gulp-imagemin'),
    imageMinMozjpeg = require('imagemin-mozjpeg'),
    imageResize = require('gulp-image-resize'),
    postcss = require('gulp-postcss'),
    rename = require('gulp-rename'),
    sass = require('gulp-sass'),
    size = require('gulp-size'),
    svgSprite = require('gulp-svg-sprite'),
    webpack = require('webpack-stream'),
    webpackConfig = require('./webpack.config.js');

var destFolder = !! argv.dist ? 'dist' : 'static';

// Default task with watch
gulp.task('default');

gulp.task('build', ['webpack', 'style', 'svg-sprite', 'background-images', 'images']);

gulp.task('w', ['build'], function() {
    gulp.watch('frontend/scss/**/*.scss', ['style']);
    gulp.watch('frontend/js/**/*.js', ['webpack']);
    gulp.watch('frontend/images/icons/**/*.svg', ['svg-sprite']);
});

// Move favicon and logo images to static/images folder
gulp.task('images', function() {
    return gulp.src('**/*.{png,jpg}', { cwd: 'frontend/images' })
        .pipe( gulp.dest( destFolder + '/images'  ) );
});

// SVG sprite from set of icons
gulp.task('svg-sprite', function() {
    var spriteConfig = {
        svg: {
            dimensionAttributes: false,
            doctypeDeclaration: false,
            namespaceClassnames: false,
            xmlDeclaration: false
        },
        mode: {
            symbol: true
        }
    };

    var spriteRename = ( path ) => {
        path.dirname = '';
        path.basename = 'side-kick-sprite';
    };

    return gulp.src('**/*.svg', { cwd: 'frontend/images/icons' })
        .pipe( svgSprite( spriteConfig ) )
        .pipe( rename( spriteRename ) )
        .pipe( gulp.dest( destFolder + '/images' ) );
});

//  Background images optimized
gulp.task('background-images', function() {
    var imageResizeConfig = {
        width: 2000
    };

    var imageMinPlugins = [
        imageMinMozjpeg()
    ];

    return gulp.src('*.jpeg', { cwd: 'frontend/images/backgrounds' })
        // .pipe( imageResize( imageResizeConfig ) )
        .pipe( imageMin( imageMinPlugins ) )
        .pipe( gulp.dest( destFolder + '/images/backgrounds') );
});

// Sass with autoprefixer :)
gulp.task('style', function() {
    var sassConfig = {
        outputStyle: 'compressed'
    };

    var postCssConfig = [
        autoprefixer( { browsers: ['last 2 versions'] } )
    ];

    return gulp.src('*.scss', { cwd: 'frontend/scss/' })
        .pipe( sass( sassConfig ).on('error', sass.logError) )
        .pipe( postcss( postCssConfig ) )
        .pipe( gulp.dest( destFolder + '/') )
});

gulp.task('clean', function() {
    return del( ['static/**/*', 'dist'] );
});

//  webpack side kick script
gulp.task('webpack', function() {
    if ( destFolder === 'dist' ) {
        webpackConfig.debug = false;
        webpackConfig.devtool = '';
    }
    return gulp.src('relevant-enteries-in-webpack-config')
        .pipe( webpack( webpackConfig ) )
        .pipe( gulp.dest( destFolder + '/') );
});
