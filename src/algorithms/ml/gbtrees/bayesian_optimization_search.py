import logging

import numpy as np
from sklearn.model_selection import cross_val_score

from xgboost import XGBClassifier
from bayes_opt import BayesianOptimization

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Bayesian Optimization Search")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def xgboostcv(max_depth,
              learning_rate,
              n_estimators,
              gamma,
              min_child_weight,
              max_delta_step,
              subsample,
              colsample_bytree,
              train,
              labels,
              silent=True,
              nthread=-1,
              seed=1234):
    return cross_val_score(XGBClassifier(max_depth=int(max_depth),
                                         learning_rate=learning_rate,
                                         n_estimators=int(n_estimators),
                                         silent=silent,
                                         nthread=nthread,
                                         gamma=gamma,
                                         min_child_weight=min_child_weight,
                                         max_delta_step=max_delta_step,
                                         subsample=subsample,
                                         colsample_bytree=colsample_bytree,
                                         seed=seed,
                                         objective="multi:softprob"),
                                         train,
                                         labels,
                                         "log_loss",
                                         cv=5).mean()


def perform_bayesian_optimization(training_data, training_label):
    # Load data set and target values

    train, labels = np.array(training_data, dtype=float), np.array(training_label, dtype=object)

    xgboostBO = BayesianOptimization(xgboostcv,
                                     {'max_depth': (5, 10),
                                      'learning_rate': (0.01, 0.3),
                                      'n_estimators': (50, 1000),
                                      'gamma': (1., 0.01),
                                      'min_child_weight': (2, 10),
                                      'max_delta_step': (0, 0.1),
                                      'subsample': (0.7, 0.8),
                                      'colsample_bytree': (0.5, 0.99),
                                      'train': training_data,
                                      'labels': training_label
                                      })

    xgboostBO.maximize()
    print('-' * 53)

    print('Final Results')
    print('XGBOOST: %f' % xgboostBO.res['max']['max_val'])
