import logging

import numpy as np
from sklearn.model_selection import cross_val_score

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("K Fold Validator")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def k_fold_cross_validation(encoded_amino_acids, binding_values, classifier, folds):
    """
    performs k-fold-cross-validation
    :param encoded_amino_acids:
    :param binding_values: 0 for non binding, 1 for binding
    :param classifier:
    :param folds: basically the k -> how many folds
    :return:
    """

    LOG.info("Performing " + str(folds) + "-fold validation")
    k_fold_results = cross_val_score(classifier,
                                     np.asarray(encoded_amino_acids),
                                     np.asarray(binding_values),
                                     cv=folds,
                                     scoring="roc_auc")
    LOG.info("KFold ROC_AUC: %.2f%% Standard deviation: %.2f%%" % (k_fold_results.mean() * 100, k_fold_results.std()))
    LOG.info("Successfully finished performing kfold validation")
