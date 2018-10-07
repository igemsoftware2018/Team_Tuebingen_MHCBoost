#!/usr/bin/env python
import os
import unittest

from src.io.parser.input_protein_parser import parse_protein
from test_util.path_util import pf

WD = os.path.dirname(__file__)
PATH_MINIMAL_FILE = pf(WD, "../../data/input/full_protein")


class InputProteinParserTest(unittest.TestCase):
    expected_peptides = ["CSDETTLYY", "SDETTLYYL", "DETTLYYLT", "ETTLYYLTG", "TTLYYLTGH", "TLYYLTGHM", "LYYLTGHML",
                         "YYLTGHMLD", "YLTGHMLDM", "LTGHMLDMY"]

    def test_non_file_input(self):
        self.assertEqual(self.expected_peptides, parse_protein("CSDETTLYYLTGHMLDMY", 9))

    def test_file_input(self):
        self.assertEqual(self.expected_peptides, parse_protein(PATH_MINIMAL_FILE, 9))

