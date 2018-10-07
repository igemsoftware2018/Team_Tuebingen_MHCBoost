import logging

import matplotlib
import xgboost as xgb
import matplotlib.pyplot as plt

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Plot Gbtree Classifier")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def plot_feature_importance(classifier):
    """
    plots importance of most important features
    :param classifier:
    :return:
    """
    LOG.info("Setting up feature importance plot")
    plt.clf()
    xgb.plot_importance(classifier, max_num_features=5)
    LOG.info("Successfully finished setting up feature importance plot -> displaying")
    plt.show()
    # plt.savefig('data/plots/feature_importance.png')


def plot_learning_tree(classifier):
    """
    plots tree model of classifier
    :param classifier:
    :return:
    """
    LOG.info("Setting up learning tree plot")
    plt.clf()
    xgb.plot_tree(classifier, num_trees=0, rankdir='LR')
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(30, 20)
    # fig.savefig('data/plots/learning_trees.png')
    LOG.info("Successfully finished setting up learning tree plot -> displaying")
    plt.show()