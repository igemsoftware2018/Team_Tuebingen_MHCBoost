import os

import unittest

from src.io.parser.iedb_training_data_parser import read_iedb_training_data
from test_util.path_util import pf

WD = os.path.dirname(__file__)
PATH_MINIMAL_FILE = pf(WD, "../data/training_data/iedb/A*01:01_9_only_minimal.txt")


class TestEncoder(unittest.TestCase):
    peptides = read_iedb_training_data(PATH_MINIMAL_FILE)

    def test_training_data_to_nd_arrays(self):
        """ Check if the number of peptides matches

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        self.assertEqual(1, 1)

    def test_encode_training_data(self):
        """ Check if the number of peptides matches

                    Fails if not present: Nothing
                    Warns if not present: Nothing
                """
        self.assertEqual(1, 1)


        # TODO
