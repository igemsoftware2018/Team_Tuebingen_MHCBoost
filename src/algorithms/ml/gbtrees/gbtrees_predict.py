import logging
import numpy as np

from src.algorithms.ml.encoder import encode_peptides_to_predict
from src.io.writer.labeled_peptides_writer import write_labeled_outputfile
from src.model.encoding.extended_blomap import extended_blomap_dict

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Gradient Boosted Trees Predictor")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def predict_epitopes(classifier, prediction_data, predicted_peptides_output_path):
    """
    performs a prediction on a given dataset
    :param classifier:
    :param prediction_data:
    :param predicted_peptides_output_path:
    :return:
    """
    peptides = prepare_prediction_data(prediction_data)
    peptides = encode_peptides_to_predict(peptides, extended_blomap_dict, "blomap")

    LOG.info("Predicting data")
    prediction = classifier.predict(peptides)
    LOG.info("Successfully predicted data")

    write_labeled_outputfile(prediction_data, predicted_peptides_output_path, prediction)


def prepare_prediction_data(peptides):
    """
    prepares peptides for subsequent prediction -> np array of lists of single amino acids
    :param peptides:
    :return:
    """
    aminoacid_separated_peptides = []
    for peptide in peptides:
        aminoacid_separated_peptides.append(list(peptide))

    peptides_prepared = np.asarray(aminoacid_separated_peptides)

    return peptides_prepared
