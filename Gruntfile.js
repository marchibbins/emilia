module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            options: {
                separator: ';',
            },
            dist: {
                src: [
                    'emilia/static/js/lib/angular.js',
                    'emilia/static/js/lib/underscore.js',
                    'emilia/static/js/lib/angular-google-maps.js',
                    'emilia/static/js/modules/*.js'
                ],
                dest: 'emilia/static/js/app.js',
            },
        },
        uglify: {
            dist: {
                files: {
                    'emilia/static/js/app.min.js': ['emilia/static/js/app.js']
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
                    'emilia/static/js/modules/*.js',
                    'emilia/static/js/lib/*.js'
                ],
                tasks: ['concat', 'uglify']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('compile', ['concat', 'uglify', 'sass']);
};
