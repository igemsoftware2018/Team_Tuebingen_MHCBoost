import logging

from src.io.parser.input_peptides_file_parser import parse_peptides
from src.io.parser.input_protein_parser import parse_protein

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Input Protein Parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def convert_input_to_peptides(input_peptides, peptide_length):
    """
    converts any CLI input to peptides -> can deal with files and strings
    :param input_peptides: either a file or a full string
    :param peptide_length: required if a full protein was specified and has to be cut into k-mers
    :return:
    """
    try:
        with open(input_peptides, 'r') as file:
            content = file.readline()
            if len(content) > 15:  # length of read content longer than 15 -> full protein as input
                peptides = parse_protein(input_peptides, peptide_length)
                return peptides
            else:
                peptides = parse_peptides(input_peptides)
                return peptides
    except FileNotFoundError:
        LOG.debug("Input protein was not a file. Handling it as a string")
        peptides = parse_protein(input_peptides, peptide_length)
        return peptides
