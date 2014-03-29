from coverage import coverage
import unittest


def start_coverage():
    """ Starts measuring code coverage. """
    cov = coverage(branch=True, omit=['*/site-packages/*', 'test.py'])
    cov.start()
    return cov


def stop_coverage(cov):
    """ Stops measuring code coverage. """
    # cov.report()
    cov.html_report(directory='coverage')
    cov.erase()


def run():
    """ Runs unittest runner and coverage. """
    coverage = start_coverage()
    suite = unittest.TestLoader().discover('tests')
    unittest.runner.TextTestRunner(verbosity=2).run(suite)
    stop_coverage(coverage)


if __name__ == '__main__':
    run()
