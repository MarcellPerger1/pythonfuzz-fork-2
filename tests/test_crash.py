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
            pythonfuzz.fuzzer.Fuzzer(_fuzz).start()
            self.assertTrue(mock.called_once)
