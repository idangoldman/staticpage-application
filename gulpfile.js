var autoprefixer = require('autoprefixer'),
    gulp = require('gulp'),
    imageMin = require('gulp-imagemin'),
    imageMinMozjpeg = require('imagemin-mozjpeg'),
    imageResize = require('gulp-image-resize'),
    notify = require('gulp-notify'),
    postcss = require('gulp-postcss'),
    rename = require('gulp-rename'),
    sass = require('gulp-sass'),
    size = require('gulp-size'),
    svgSprite = require('gulp-svg-sprite'),
    uglify = require('gulp-uglify');

// Default task with watch
gulp.task('default', ['page-script', 'style', 'svg-sprite', 'background-images'], function() {
    gulp.watch('assets/scss/**/*.scss', ['style']);
    gulp.watch('assets/js/page.js', ['page-script']);
    gulp.watch('assets/images/icons/**/*.svg', ['svg-sprite']);
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
    }

    return gulp.src('**/*.svg', { cwd: 'assets/images/' })
        .pipe( svgSprite( spriteConfig ) )
        .pipe( rename( spriteRename ) )
        .pipe( gulp.dest('static/images') );
});

//  Background images optimized
gulp.task('background-images', function() {
    var imageResizeConfig = {
        width: 2000
    };
    
    var imageMinPlugins = [
        imageMinMozjpeg()
    ];

    return gulp.src('*.jpeg', { cwd: 'assets/images/backgrounds' })
        // .pipe( imageResize( imageResizeConfig ) )
        .pipe( imageMin( imageMinPlugins ) )
        .pipe( gulp.dest('static/images/backgrounds') );
});

// File stats
gulp.task('static-stats', function () {
    var sizeConfig = size({
        showFiles: true
    });

    gulp.src('static/**/*')
        .pipe( sizeConfig )
        .pipe( gulp.dest('static/') );
});

// Sass with autoprefixer :)
gulp.task('style', function() {
    var sassConfig = {
        outputStyle: 'compressed'
    };

    var postCssConfig = [
        autoprefixer( { browsers: ['last 2 versions'] } )
    ];

    return gulp.src('*.scss', { cwd: 'assets/scss/' })
        .pipe( sass( sassConfig ).on('error', sass.logError) )
        .pipe( postcss( postCssConfig ) )
        .pipe( gulp.dest('static/') )
});

// only uglify
gulp.task('page-script', function() {
    return gulp.src('page.js', { cwd: 'assets/js' })
        .pipe(uglify())
        .pipe( gulp.dest('static/') )
});