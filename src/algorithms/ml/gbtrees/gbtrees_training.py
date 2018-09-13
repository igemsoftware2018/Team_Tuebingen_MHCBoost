import logging
import warnings

from xgboost import XGBClassifier

from src.algorithms.evaluation.k_fold_crossvalidation import k_fold_cross_validation

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Gradient Boosted Trees Training")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def gbtrees_train(encoded_aminoacids, binding_values):
    # see: https://stackoverflow.com/questions/49545947/sklearn-deprecationwarning-truth-value-of-an-array
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)

    classifier = XGBClassifier()
    k_fold_cross_validation(encoded_aminoacids, binding_values, classifier, 10)



