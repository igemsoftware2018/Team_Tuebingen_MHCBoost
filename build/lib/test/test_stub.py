#!/usr/bin/env python
import os
import unittest

from test_util.path_util import pf

WD = os.path.dirname(__file__)
PATH_MINIMAL_WORKING_EXAMPLE = pf(WD, "data/test.txt")


class TestLint(unittest.TestCase):
    def test_read_dir_content_and_pass(self):
        """ Check if the content of the file matches

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        with open(PATH_MINIMAL_WORKING_EXAMPLE, 'r') as f:
            data = f.read()
            self.assertEqual(data, "blub")
