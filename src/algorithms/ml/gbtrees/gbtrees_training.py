import logging
import warnings

from src.algorithms.ml.encoder import encode_training_data
from src.model.encoding.extended_blomap import extended_blomap_dict

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Gradient Boosted Trees Training")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def gbtrees_train(peptides):
    # see: https://stackoverflow.com/questions/49545947/sklearn-deprecationwarning-truth-value-of-an-array
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)

    encoded_aminoacids, binding_values = encode_training_data(peptides, extended_blomap_dict, "extended blomap")
