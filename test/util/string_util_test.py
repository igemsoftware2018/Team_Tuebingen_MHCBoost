import unittest


from src.util.string_util import generate_k_mer


class StringUtilTest(unittest.TestCase):

    def test_2_mer(self):
        """ Check if the generated 2-mer match

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        input_string = "ACGT"
        k_mers = ["AC", "CG", "GT"]
        self.assertEqual(k_mers, generate_k_mer(input_string, 2))

    def test_9_mer(self):
        """ Check if the generated 9-mer match

            Fails if not present: Nothing
            Warns if not present: Nothing
        """
        input_string = "CSDETTLYYLTGHMLDMY"
        k_mers = ["CSDETTLYY",
                  "SDETTLYYL",
                  "DETTLYYLT",
                  "ETTLYYLTG",
                  "TTLYYLTGH",
                  "TLYYLTGHM",
                  "LYYLTGHML",
                  "YYLTGHMLD",
                  "YLTGHMLDM",
                  "LTGHMLDMY"]
        self.assertEqual(k_mers, generate_k_mer(input_string, 9))

