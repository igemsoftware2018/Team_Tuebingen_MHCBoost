import logging
import warnings

from xgboost import XGBClassifier

from src.algorithms.ml.gbtrees.gbtrees_grid_search import perform_grid_search
from src.algorithms.ml.gbtrees.gbtrees_randomized_search import perform_randomized_search
from src.evaluation.k_fold_crossvalidation import k_fold_cross_validation
from src.evaluation.random_dataset import random_dataset_split_eval

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Gradient Boosted Trees Training")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def gbtrees_train(encoded_amino_acids, binding_values, silent):
    """
    trains an XGBoost classifier, evaluates the current performance and may run a searchCV algorithm
    :param encoded_amino_acids: encoded amino acids - usually blomap encoded
    :param binding_values: 0 if not binding, 1 if binding
    :param silent:
    :return: the trained classifier
    """
    # see: https://stackoverflow.com/questions/49545947/sklearn-deprecationwarning-truth-value-of-an-array
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)

    classifier = XGBClassifier(silent=silent, n_estimators=300, learning_rate=0.2, max_depth=6, min_child_weight=1, subsample=0.7)
    # also features the training step!
    random_dataset_split_eval(encoded_amino_acids, binding_values, classifier, 10, 0.2)

    k_fold_cross_validation(encoded_amino_acids, binding_values, classifier, 5)

    # perform_grid_search(encoded_amino_acids, binding_values, classifier, silent)
    # perform_randomized_search(encoded_amino_acids, binding_values, classifier, silent)

    return classifier



