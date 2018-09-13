import logging
import matplotlib.pyplot as plt

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("AUC plot")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def plot_auc_curve(model):
    """
    plots auc-curve of model's eval-metric

    Parameters
    ----------
    model : XGBClassifier()
        project's classifier model (gradient boosted tree)

    Returns
    -------
    -

    """
    LOG.info("Setting up AUC plot")
    # retrieve performance metrics
    results = model.evals_result()
    epochs = len(results['validation_0']['auc'])
    x_axis = range(0, epochs)

    # plot auc
    plt.clf()
    fig, ax = plt.subplots()
    ax.plot(x_axis, results['validation_0']['auc'], label='Train')
    ax.plot(x_axis, results['validation_1']['auc'], label='Test')
    ax.legend()
    plt.ylabel('AUC')
    plt.xlabel('epoch')
    plt.title('XGBoost AUC')

    LOG.info("Successfully finished setting up AUC plot -> Displaying")

    # plt.savefig('data/plots/auc_plot.png')
    plt.show()