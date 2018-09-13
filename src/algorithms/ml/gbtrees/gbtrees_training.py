import logging
import warnings

from xgboost import XGBClassifier

from src.algorithms.ml.gbtrees.gbtrees_gridsearch import perform_grid_search
from src.evaluation.k_fold_crossvalidation import k_fold_crossvalidation
from src.evaluation.random_dataset import random_dataset_split_eval

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Gradient Boosted Trees Training")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def gbtrees_train(encoded_aminoacids, binding_values, silent):
    # see: https://stackoverflow.com/questions/49545947/sklearn-deprecationwarning-truth-value-of-an-array
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)

    classifier = XGBClassifier(silent=silent)
    random_dataset_split_eval(encoded_aminoacids, binding_values, classifier, 10, 0.2)

    k_fold_crossvalidation(encoded_aminoacids, binding_values, classifier, 5)

    # perform_grid_search(encoded_aminoacids, binding_values, classifier, silent)



