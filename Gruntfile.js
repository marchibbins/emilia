module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        requirejs: {
            compile: {
                options: {
                    baseUrl: 'emilia/static/js',
                    name: 'amd/app',
                    include: 'lib/require.js',
                    out: 'emilia/static/js/app.min.js',
                    optimize: 'uglify2',
                    preserveLicenseComments: false
                }
            }
        },
        sass: {
            dist: {
                options: {
                    style: 'compressed'
                },
                files: {
                    'emilia/static/css/style.css': 'emilia/static/sass/style.scss'
                }
            }
        },
        watch: {
            css: {
                files: 'emilia/static/sass/*.scss',
                tasks: ['sass']
            },
            js: {
                files: [
                    'emilia/static/js/amd/*.js',
                    'emilia/static/js/lib/*.js'
                ],
                tasks: ['requirejs']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('compile', ['requirejs', 'sass']);
};
