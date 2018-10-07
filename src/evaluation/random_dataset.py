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


def random_dataset_split_eval(encoded_amino_acids, binding_values, classifier, early_stopping_rounds, test_size_percent):
    """
    randomly splits training set and trains classifier
    starts stats evaluation of predictions compared to known results,
    and starts auc-plot, tree-plot, feature-importance-plot
    :param encoded_amino_acids:
    :param binding_values:
    :param classifier:
    :param early_stopping_rounds: early stopping value passed to the classifier
    :param test_size_percent:
    :return:
    """
    LOG.info("Evaluating a random subset of size: " + str(test_size_percent) + " of the training data")
    peptides_train, peptides_test, classification_train, classification_test = train_test_split(encoded_amino_acids, binding_values,
                                                                                                test_size=test_size_percent)

    eval_set = [(peptides_train, classification_train), (peptides_test, classification_test)]

    classifier.fit(np.array(peptides_train), np.array(classification_train), eval_metric=['auc'], eval_set=eval_set)

    classification_pred = classifier.predict(peptides_test)
    LOG.info("Successfully evaluated a random subset of the training data")

    # plot_auc_curve(classifier)
    # plot_learning_tree(classifier)
    # plot_feature_importance(classifier)

    stats_evaluation(classification_test, classification_pred)
