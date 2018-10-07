import logging

from sklearn.model_selection import RandomizedSearchCV

from src.algorithms.ml.gbtrees.search_parameters import search_parameters_dict

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Randomized Search")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def perform_randomized_search(encoded_amino_acids, binding_values, classifier, silent):
    """
    performs randomized-search on trained classifier
    :param encoded_amino_acids: numpy-array -> blomap encoded AAs
    :param binding_values: numpy-array -> predictions (1 or 0)
    :param classifier: the classifier
    :param silent: boolean to decide whether or not model processing should be hidden 
    :return: 
    """

    LOG.info("Performing randomized search")

    LOG.info("Randomized search parameters: " + str(search_parameters_dict))

    verbose_level = 0
    if not silent:
        verbose_level = 2

    grid = RandomizedSearchCV(classifier,  cv=3, verbose=verbose_level, param_distributions=search_parameters_dict)
    grid.fit(encoded_amino_acids, binding_values)
    LOG.info("Best: %f using %s" % (grid.best_score_, grid.best_params_))

    LOG.info("Successfully finished performing randomized search")
