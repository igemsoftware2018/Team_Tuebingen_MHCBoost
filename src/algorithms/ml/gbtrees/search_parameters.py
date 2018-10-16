search_parameters_dict = {
    'min_child_weight': [1, 2, 3, 4, 5],
    'colsample_bytree': [0.5, 0.6, 0.7, 0.8, 0.9, 1],
    'gamma': [0, 1, 2, 3, 4, 5],
    'n_estimators': [500, 700, 800, 900, 1000, 1100, 1200, 1300, 2000],
    'learning_rate': [0.1, 0.15,  0.18, 0.19, 0.2],
    'max_depth': [2, 3, 4, 5, 6, 7, 8, 9],
    'subsample': [0.5, 0.6, 0.7, 0.9, 1]
}

search_parameters_dict_fat = {
    'min_child_weight': [1, 2, 3, 4, 5],
    'colsample_bytree': [0.5, 0.6, 0.7, 0.8, 0.9, 1],
    'gamma': [0, 1, 2, 3, 4, 5],
    'n_estimators': [500, 700, 800, 900, 1000, 1100, 1200, 1300, 2000, 5000],
    'learning_rate': [0.01, 0.05, 0.1, 0.15,  0.18, 0.19, 0.2],
    'max_depth': [2, 3, 4, 5, 6, 7, 8, 9],
    'subsample': [0.5, 0.6, 0.7, 0.9, 1]
}