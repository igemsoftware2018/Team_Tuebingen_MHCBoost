import logging

from src.util.string_util import generate_k_mer

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Input Protein Parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def parse_protein(protein, peptide_length):
    """
    generates a list of k-mers using either a file containing a protein or a passed protein as string
    :param protein: either file containing a protein or a protein as string
    :param peptide_length: k-mer value
    :return: list of peptides of length k
    """
    LOG.info("Parsing full protein")
    try:
        with open(protein, 'r') as file:
            full_protein = file.read()
            LOG.info("Successfully parsed protein")
            return generate_k_mer(full_protein, peptide_length)
    except FileNotFoundError:
        LOG.debug("Input protein was not a file. Handling it as a string")
        return generate_k_mer(protein, peptide_length)


