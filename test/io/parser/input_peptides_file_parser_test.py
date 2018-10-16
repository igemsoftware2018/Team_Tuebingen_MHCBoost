import os
import unittest

from src.io.parser.input_peptides_file_parser import parse_peptides
from test_util.path_util import pf

WD = os.path.dirname(__file__)
PATH_MINIMAL_FILE = pf(WD, "../../data/input/peptides_list")


class InputPeptidesFileParserTest(unittest.TestCase):

    def test_minimal_input(self):
        expected_peptides = ["CSDAFYPFY",
                             "CSDETTLYY",
                             "DSDDWLNKY",
                             "EADATWWLY",
                             "ESDMEVFDY",
                             "ESENISEPY",
                             "ETDQMDTIY",
                             "FSAVGNICY",
                             "FTDISMSLY",
                             "GTEYRLTLY",
                             "ISDEFMWRY",
                             "ITDFNIDTY"]

        self.assertEqual(expected_peptides, parse_peptides(PATH_MINIMAL_FILE))
