import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Labeled Peptides Writer")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def write_labeled_outputfile(peptides, predicted_peptides_output_path, prediction):
    """
    writes labeled peptides to the passed path
    :param peptides: list of peptides
    :param predicted_peptides_output_path: path to write labeled output to
    :param prediction: predicted values
    :return:
    """
    LOG.info("Writing labeled output file to: " + predicted_peptides_output_path)

    output_file = open(predicted_peptides_output_path, "w+")
    for peptide in range(len(peptides)):
        output_file.write(peptides[peptide] + "\t" + str(prediction[peptide]) + "\n")

    LOG.info("Successfully wrote labeled output file to: " + predicted_peptides_output_path)
