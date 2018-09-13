import logging

import numpy as np
from sklearn.model_selection import train_test_split

from src.evaluation.stats import stats_evaluation
from src.plots.auc import plot_auc_curve
from src.plots.gbtree_classifier import plot_learning_tree, plot_feature_importance

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Random Dataset Validator")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def random_dataset_split_eval(peptides, predictions, classifier, early_stopping_rounds, test_size_percent):
    """
    randomly splits training set and trains classifier (ic50 regression may or may not be included here),
    starts stats evaluation of predictions compared to known results,
    and starts auc-plot, tree-plot, feature-importance-plot

    Parameters
    ----------
    peptides : numpy-array containing Floats
        in blomap encoded oneletterCode of aminoacids for peptides
    predictions : numpy-array containing Integers
        0 for nonbinder 1 for binder
    peptides_balanced : numpy-array containing Floats
        in blomap encoded oneletterCode of aminoacids for peptides after subsampling
    predictions_balanced : numpy-array containing Integers
        0 for nonbinder 1 for binder after subsampling
    classifier : XGBClassifier()
        project's classifier model (gradient boosted tree)
    regression : XGBRegressor()
        regression to compute ic50-values
    check_use_ic50s : boolean
        boolean to decide wether to use ic50s or not
    early_stopping_rounds : Integer
        early-stopping parameter
    test_size_percent : Float
        value between 0 and 1, decides on the percentage size
        of the test set


    Returns
    -------
    -

    """
    LOG.info("Evaluating a random subset of size: " + str(test_size_percent) + " of the training data")
    peptides_train, peptides_test, classification_train, classification_test = train_test_split(peptides, predictions,
                                                                                                test_size=test_size_percent)

    eval_set = [(peptides_train, classification_train), (peptides_test, classification_test)]

    classifier.fit(np.array(peptides_train), np.array(classification_train), eval_metric=['auc'], eval_set=eval_set)

    classification_pred = classifier.predict(peptides_test)
    LOG.info("Successfully evaluated a random subset of the training data")

    # plot_auc_curve(classifier)
    # plot_learning_tree(classifier)
    # plot_feature_importance(classifier)

    stats_evaluation(classification_test, classification_pred)
