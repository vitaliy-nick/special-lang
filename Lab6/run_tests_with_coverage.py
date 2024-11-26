import coverage
import unittest

def main():
    cov = coverage.Coverage()
    cov.start()

    loader = unittest.TestLoader()
    tests = loader.discover('.')
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(tests)

    cov.stop()
    cov.save()

    print("\n--- Code Coverage Report ---")
    cov.report()

if __name__ == "__main__":
    main()
