import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Input Peptides Files")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def parse_peptides(input_file):
    all_peptides = [line.rstrip() for line in open(input_file)]

    return all_peptides

