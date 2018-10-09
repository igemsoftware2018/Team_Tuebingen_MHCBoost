import logging
import warnings

import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from src.algorithms.ml.gbtrees.bayesian_optimization_search import perform_bayesian_optimization
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

    classifier = XGBClassifier(silent=silent,
                               n_estimators=1200,
                               learning_rate=0.2,
                               max_depth=6,
                               subsample=1,
                               gamma=3,
                               min_child_weight=1,
                               colsample_bytree=0.7)

    # setup training and evaluation datasets
    peptides_train, peptides_test, classification_train, classification_test = train_test_split(encoded_amino_acids,
                                                                                                binding_values,
                                                                                                test_size=0.2,
                                                                                                random_state=0)
    eval_set = [(peptides_train, classification_train), (peptides_test, classification_test)]

    # train the classifier on the subset of the data
    classifier.fit(np.array(peptides_train), np.array(classification_train),
                   eval_metric=['auc'],
                   eval_set=eval_set,
                   early_stopping_rounds=40)

    # evaluate the data classifier using a random dataset
    random_dataset_split_eval(classifier, peptides_test, classification_test, 0.2)

    k_fold_cross_validation(encoded_amino_acids, binding_values, classifier, 5)

    # perform_grid_search(encoded_amino_acids, binding_values, classifier, silent)
    # perform_randomized_search(encoded_amino_acids, binding_values, classifier, silent)
    # perform_bayesian_optimization(encoded_amino_acids, binding_values)

    return classifier
