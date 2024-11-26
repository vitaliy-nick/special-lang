import coverage
import unittest
import os

def run_tests():
    cov = coverage.Coverage(source=['Classes', 'UI'])
    cov.start()

    loader = unittest.TestLoader()
    test_folder = os.path.abspath('/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Lab7/Tests')
    tests = loader.discover(test_folder)

    test_runner = unittest.TextTestRunner()
    test_runner.run(tests)

    cov.stop()
    cov.save()

    print("\n--- Coverage Report ---")
    cov.report(show_missing=True)


if __name__ == "__main__":
    run_tests()