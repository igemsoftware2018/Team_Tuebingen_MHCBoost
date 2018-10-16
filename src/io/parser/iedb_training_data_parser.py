import csv
import logging

from src.model.peptide import Peptide

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("iedb Training Data Parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def read_iedb_training_data(file_path):
    """
    parses iedb files
    :param file_path: path pointing towards the iedb file
    :return: list of peptides, not yet encoded
    """
    LOG.info("Reading in training data")
    peptides = []

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        next(file)  # skip the header
        for row in csv_reader:
            species = row[0]
            mhc_allele = row[1]
            length = row[2]
            sequence = row[3]
            inequality = row[4]
            meas = row[5]
            peptide = Peptide(species, mhc_allele, int(length), sequence, inequality, float(meas))

            peptides.append(peptide)

    LOG.info("Successfully read in training data")
    return peptides
