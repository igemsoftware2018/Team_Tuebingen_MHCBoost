import logging

from sklearn.model_selection import GridSearchCV

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Grid search")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def perform_grid_search(peptides, predictions, classifier, silent):
    """
    performs grid-search on trained classifier

    Parameters
    ----------
    peptides : numpy-array containing Floats
        in blomap encoded oneletterCode of aminoacids for peptides
    predictions : numpy-array containing Integers
        0 for nonbinder 1 for binder
    classifier : XGBClassifier()
        project's classifier model (gradient boosted tree)
    silent : boolean
        boolean to decide wether or not model processing should be hidden

    Returns
    -------
    -

    """
    LOG.info("Performing grid search")
    parameters = {
        'min_child_weight': [1, 2, 3, 4],
        'colsample_bytree': [0.5, 0.6, 0.7],
        'gamma': [0, 1, 2, 3, 4, 5],
        'n_estimators': [75, 80, 85, 90, 95, 100]
    }

    LOG.info("Grid search parameters: " + str(parameters))

    verbose_level = 0
    if not silent:
        verbose_level = 2

    grid = GridSearchCV(classifier, parameters, cv=3, verbose=verbose_level)
    grid.fit(peptides, predictions, eval_metric="auc")
    LOG.info("Best: %f using %s" % (grid.best_score_, grid.best_params_))
    means = grid.cv_results_['mean_test_score']
    stds = grid.cv_results_['std_test_score']
    params = grid.cv_results_['params']

    for mean, stdev, param in zip(means, stds, params):
        LOG.info("%f (%f) with: %r" % (mean, stdev, param))

    LOG.info("Successfully finished performing grid search")
