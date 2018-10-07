import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Labeled Peptides Writer")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def write_labeled_outputfile(prediction_data, predicted_peptides_output_path, prediction):
    """
    writes labeled peptides to the passed path

    """
    LOG.info("Writing labeled output file to: " + predicted_peptides_output_path)

    output_file = open(predicted_peptides_output_path, "w+")
    for peptide in range(len(prediction_data)):
        output_file.write(prediction_data[peptide] + "\t" + str(prediction[peptide]) + "\n")

    LOG.info("Successfully wrote labeled output file to: " + predicted_peptides_output_path)
