import logging

from src.evaluation.stats import stats_evaluation

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Random Dataset Validator")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def random_dataset_split_eval(classifier, peptides_test, classification_test, test_size_percent):
    """
    starts stats evaluation of predictions compared to known results,
    and starts auc-plot, tree-plot, feature-importance-plot
    :param classifier:
    :param peptides_test:
    :param classification_test:
    :param test_size_percent: size of test dataset in percent/100
    :return:
    """
    LOG.info("Evaluating a random subset of size: " + str(test_size_percent) + " of the training data")

    classification_pred = classifier.predict(peptides_test)
    LOG.info("Successfully evaluated a random subset of the training data")

    # plot_auc_curve(classifier)
    # plot_learning_tree(classifier)
    # plot_feature_importance(classifier)

    stats_evaluation(classification_test, classification_pred)
