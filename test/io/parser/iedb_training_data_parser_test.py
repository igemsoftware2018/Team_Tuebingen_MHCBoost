#!/usr/bin/env python
import os
import unittest

from src.io.parser.iedb_training_data_parser import read_training_data
from test_util.path_util import pf

WD = os.path.dirname(__file__)
PATH_MINIMAL_FILE = pf(WD, "data/training_data/iedb/A*01:01_9_only_minimal.txt")


class TestLint(unittest.TestCase):
    def test_number_of_peptides(self):
        """ Check if the number of peptides matches

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        read_peptides = read_training_data(PATH_MINIMAL_FILE)
        print(read_peptides)
        self.assertEqual(12, len(read_peptides) - 1)


