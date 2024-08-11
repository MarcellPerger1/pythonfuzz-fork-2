import unittest
import zipfile
import io
from unittest.mock import patch

import pythonfuzz


def _fuzz(buf):
    f = io.BytesIO(buf)
    z = zipfile.ZipFile(f)
    z.testzip()


class TestFindCrash(unittest.TestCase):
    def test_find_crash(self):
        with patch('logging.Logger.info') as mock:
            try:
                pythonfuzz.fuzzer.Fuzzer(_fuzz).start()
            except SystemExit as e:
                self.assertEqual(76, e.code)
            # TODO: this doesn't actually do anything as mock.called_once
            #  doesn't exist so isn't really asserting anything
            self.assertTrue(mock.called_once)
