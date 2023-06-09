"""
Unit testing
"""

import unittest

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(testsuite)
