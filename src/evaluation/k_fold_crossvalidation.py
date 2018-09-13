import logging

import numpy as np
from sklearn.model_selection import cross_val_score

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("K Fold Validator")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def k_fold_crossvalidation(peptides, predictions, classifier, splits):
    """
    performs k-fold-cross-validation

    Parameters
    ----------
    peptides : numpy-array containing Floats
        in blomap encoded oneletterCode of aminoacids for peptides
    predictions : numpy-array containing Integers
        0 for nonbinder 1 for binder
    classifier : classifier of choice
        project's classifier model (gradient boosted tree)
    splits : Integer
        number of subsets created by k-fold

    Returns
    -------
    -

    """
    LOG.info("Performing " + str(splits) + "-fold validation")
    k_fold_results = cross_val_score(classifier, np.asarray(peptides), np.asarray(predictions), cv=splits, scoring="roc_auc")
    LOG.info("KFold ROC_AUC: %.2f%% Standard deviation: %.2f%%" % (k_fold_results.mean() * 100, k_fold_results.std()))
    LOG.info("Successfully finished performing kfold validation")
