#!/usr/bin/env python
import os
import unittest

from src.io.parser.iedb_training_data_parser import read_iedb_training_data
from test_util.path_util import pf

WD = os.path.dirname(__file__)
PATH_MINIMAL_FILE = pf(WD, "../../data/training_data/iedb/A*01:01_9_only_minimal.txt")


class TestIedbTrainingDataParser(unittest.TestCase):
    read_peptides = read_iedb_training_data(PATH_MINIMAL_FILE)

    def test_quantity(self):
        """ Check if the number of peptides matches

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        self.assertEqual(12, len(TestIedbTrainingDataParser.read_peptides))

    def test_species(self):
        """ Check if all peptides are of human HLA

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        for peptide in TestIedbTrainingDataParser.read_peptides:
            self.assertEqual("human", peptide.species)

    def test_allele(self):
        """ Check if all peptides are HLA-A*01:01

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        for peptide in TestIedbTrainingDataParser.read_peptides:
            self.assertEqual("HLA-A*01:01", peptide.mhc_allele)

    def test_length(self):
        """ Check if length of all peptide is 9

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        for peptide in TestIedbTrainingDataParser.read_peptides:
            self.assertEqual(9, peptide.length)

    def test_sequence(self):
        """ Checks a limited amount of peptides for sequence

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        self.assertEqual("QSDTVFDYY", TestIedbTrainingDataParser.read_peptides[0].sequence)
        self.assertEqual("FLDQWWTEY", TestIedbTrainingDataParser.read_peptides[2].sequence)
        self.assertEqual("TQIGCTLNF", TestIedbTrainingDataParser.read_peptides[8].sequence)
        self.assertEqual("VDINLIPLI", TestIedbTrainingDataParser.read_peptides[11].sequence)

    def test_inequality(self):
        """ Checks for inequality values

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        for peptide in TestIedbTrainingDataParser.read_peptides:
            self.assertEqual("=", peptide.inequality)

    def test_meas(self):
        """ Checks a limited amount of peptides for their meas values

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        self.assertEqual(1.033949707, TestIedbTrainingDataParser.read_peptides[0].meas)
        self.assertEqual(1.1, TestIedbTrainingDataParser.read_peptides[2].meas)
        self.assertEqual(19087.69156, TestIedbTrainingDataParser.read_peptides[8].meas)
        self.assertEqual(19552.7431, TestIedbTrainingDataParser.read_peptides[11].meas)

    def test_binding(self):
        """ Checks a limited amount of peptides whether or not they're labeled binders

                    Fails if not present: Nothing
                    Warns if not present: Nothing
        """
        self.assertEqual(True, TestIedbTrainingDataParser.read_peptides[0].binding)
        self.assertEqual(True, TestIedbTrainingDataParser.read_peptides[2].binding)
        self.assertEqual(False, TestIedbTrainingDataParser.read_peptides[8].binding)
        self.assertEqual(False, TestIedbTrainingDataParser.read_peptides[11].binding)





