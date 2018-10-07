import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Input Peptides Files")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def parse_peptides(input_file):
    """
    parses peptides
    :param input_file: required: new line seperated list of peptides
    :return: list of peptides
    """
    all_peptides = [line.rstrip() for line in open(input_file, encoding='utf-8-sig')]

    return all_peptides

