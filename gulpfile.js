var gulp = require('gulp'),
    del = require('del'),
    sequence = require('gulp-sequence'),
    sourcemaps = require('gulp-sourcemaps'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    notify = require('gulp-notify'),
    minifyCss = require('gulp-minify-css'),
    browserify = require('gulp-browserify'),
    rename = require('gulp-rename'),
    rev = require('gulp-rev'),
    gulpif = require('gulp-if'),
    gutil = require('gulp-util'),
    livereload = require('gulp-livereload'),
    autoprefixer = require('gulp-autoprefixer'),
    plumber = require('gulp-plumber');

var publicPath = './public',
    resourcePath = './resource',
    buildPath = publicPath + '/build',
    distPath = publicPath + '/dist',
    fontsPath = publicPath + '/fonts',
    assetsPath = resourcePath + '/assets';

gulp.task('clean', function(callback) {
    del([buildPath, distPath, fontsPath]).then(function(paths) {
        callback(null);
    });
});

gulp.task('browserify', function(callback) {
    return gulp
        .src(assetsPath + '/js/app.js')
        .pipe(plumber({
            errorHandler: notify.onError({
                sound  : true,
                sticky : false,
                message: "ERROR: <%= error.message %>"
            })
        }))
        .pipe(browserify({
            insertGlobals: true,
            transform: ['partialify', 'babelify', 'vueify'],
            debug : !gutil.env.production
        }).on('error', function(error) {
            gutil.beep('*-****-*-*--');
            gutil.log("============================");
            gutil.log("==> Plugin : " + error.plugin);
            gutil.log("==> Name   : " + error.name);
            gutil.log("============================");
            gutil.log(error.stack);
        }))
        .pipe(rename('app.scope.js'))
        .pipe(gulp.dest(buildPath))
        .pipe(notify('Browserify'));
});

gulp.task('scripts', function(callback) {
    return gulp
        .src([
            'bower_components/jquery/dist/jquery.js',
            'bower_components/bootstrap/dist/js/bootstrap.js',
            'bower_components/toastr/toastr.js',
            'bower_components/socket.io-client/socket.io.js',
            buildPath + '/app.scope.js'
        ])
        .pipe(sourcemaps.init())
        .pipe(concat(buildPath + '/app.all.js'))
        .pipe(gulpif(gutil.env.production, uglify().on('error', gutil.log)))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(__dirname))
        .pipe(notify('Scripts'));
});

gulp.task('styles', function(callback) {
    return gulp
        .src([
            'bower_components/bootstrap/dist/css/bootstrap.css',
            'bower_components/animate.css/animate.css',
            'bower_components/toastr/toastr.css',
            assetsPath + '/css/simple-sidebar.css'
        ])
        .pipe(sourcemaps.init())
        .pipe(autoprefixer())
        .pipe(concat(buildPath + '/app.all.css'))
        .pipe(gulpif(gutil.env.production, minifyCss({ keepSpecialComments: 0 })))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(__dirname))
        .pipe(notify('Styles'));
});

gulp.task('version:assets', function(callback) {
    return gulp
        .src([
            buildPath + '/app.all.js',
            buildPath + '/app.all.css'
        ])
        .pipe(rev())
        .pipe(gulp.dest(distPath))
        .pipe(rev.manifest())
        .pipe(gulp.dest(distPath))
        .pipe(livereload())
        .pipe(notify('Version:assets'));
});

gulp.task('fonts', function(callback) {
    return gulp
        .src('bower_components/bootstrap/fonts/*')
        .pipe(gulp.dest(fontsPath));
});

gulp.task('develop', function(callback) {
    sequence('browserify', 'scripts', 'styles', 'version:assets', 'fonts')(callback)
});

gulp.task('dist', function(callback) {
    sequence('clean', 'develop')(callback)
});

gulp.task('watch', function(callback) {
    livereload.listen({
        basePath: distPath
    });

    gulp.watch("./resource/**/*", ['dist']);
});
