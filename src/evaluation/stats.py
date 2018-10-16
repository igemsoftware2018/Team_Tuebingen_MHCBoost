import logging

from sklearn.metrics import confusion_matrix, roc_auc_score

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Stats Evaluator")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def stats_evaluation(set_tested, set_predicted):
    """
    evaluates predictions compared to known results by creating a confusion matrix
    calculates various different statistical properties
    :param set_tested: known classification
    :param set_predicted: predicted classification
    :return:
    """
    LOG.info("Creating confusion matrix")
    cm = confusion_matrix(set_tested, set_predicted)
    sum_tp = cm[1][1]
    LOG.info("TP = " + str(sum_tp))
    sum_tn = cm[0][0]
    LOG.info("TN = " + str(sum_tn))
    sum_fp = cm[0][1]
    LOG.info("FP = " + str(sum_fp))
    sum_fn = cm[1][0]
    LOG.info("FN = " + str(sum_fn))
    LOG.info("All = " + str(sum_tn + sum_tp + sum_fn + sum_fp))
    LOG.info("SP = " + str(sum_tn / (sum_tn + sum_fp)))
    recall = sum_tp / (sum_tp + sum_fn)
    LOG.info("SE = " + str(recall))
    precision = sum_tp / (sum_tp + sum_fp)
    LOG.info("PPV = " + str(precision))
    LOG.info("NPV = " + str(sum_tn / (sum_tn + sum_fn)))
    LOG.info("MCC = " + str((sum_tp * sum_tn - sum_fp * sum_fn) / (
                (sum_tn + sum_fn) * (sum_tn + sum_fp) * (sum_tp + sum_fn) * (sum_tp + sum_fp)) ** (1 / 2)))
    LOG.info("F-Score = " + str(2 * ((precision * recall) / (precision + recall))))
    LOG.info("ACC = " + str((sum_tn + sum_tp) / (sum_tn + sum_tp + sum_fn + sum_fp)))
    LOG.info("AUROC = " + str(roc_auc_score(set_tested, set_predicted)))