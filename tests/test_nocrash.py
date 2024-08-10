import unittest
from unittest.mock import patch

import pythonfuzz


def _fuzz(_buf):
    return True


class TestFindCrash(unittest.TestCase):
    def test_find_crash(self):
        with patch('logging.Logger.info') as mock:
            try:
                pythonfuzz.fuzzer.Fuzzer(_fuzz, runs=100).start()
            except SystemExit as e:
                self.assertEqual(0, e.code)
            mock.assert_called_with('did %d runs, stopping now.', 100)
