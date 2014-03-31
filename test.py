from coverage import coverage
import sys
import unittest


def start_coverage():
    """ Starts measuring code coverage. """
    cov = coverage(branch=True, omit=['*/site-packages/*', 'test.py'])
    cov.start()
    return cov


def stop_coverage(cov):
    """ Stops measuring code coverage. """
    # cov.report()
    print 'Generating HTML Coverage report ...'
    cov.html_report(directory='coverage')
    cov.erase()


def run(pattern='*'):
    """ Runs unittest runner and coverage. """
    if len(sys.argv) > 1:
        pattern = sys.argv[1]

    # Only run Coverage (generating HTML report) if testing everything
    run_coverage = pattern == '*'
    if run_coverage:
        coverage = start_coverage()

    suite = unittest.TestLoader().discover('tests', pattern='test_%s.py' % pattern)
    unittest.runner.TextTestRunner(verbosity=2).run(suite)

    if run_coverage:
        stop_coverage(coverage)


if __name__ == '__main__':
    run()
