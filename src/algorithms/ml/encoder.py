import logging
import pandas as pd

from numpy import array

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Encoder")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def encode_training_peptides(amino_acids, encoding, encoding_name):
    """
    encodes given oneLetterCode of aminoacids into the passed encoding
    suitable for training datasets
    :param amino_acids: 
    :param encoding: dict -> encoding
    :param encoding_name: 
    :return: 
    """
    LOG.info("Encoding training datasets into " + encoding_name + " values")
    nd_peptides, nd_bindings = training_data_to_nd_arrays(amino_acids)

    encoded_aminoacids = []
    for peptide_seq in nd_peptides:
        properties = []
        for aminoacid in peptide_seq:
            if isinstance(aminoacid, str):
                properties.extend(encoding[aminoacid.upper()])
            else:
                properties.append(aminoacid)
        encoded_aminoacids.append(properties)

    df_encoded_aminoacids = pd.DataFrame(encoded_aminoacids)
    encoded_aminoacids = df_encoded_aminoacids.iloc[:, :].values

    LOG.info("Successfully encoded training datasets into " + encoding_name + " values")

    return encoded_aminoacids, nd_bindings


def training_data_to_nd_arrays(peptides):
    """
    transforms the given peptides into lists of single letter amino acids
    appends binding values
    :param peptides:
    :return: peptides split into single letter amino acids, binding values
    """
    # separate all sequences of the peptides into single letters
    peptides_listed = []
    all_bindings = []
    for peptide in peptides:
        peptides_listed.append(list(peptide.sequence))
        if peptide.binding:
            all_bindings.append(1)
        else:
            all_bindings.append(0)

    nd_peptides = array(peptides_listed)

    df_bindings = pd.DataFrame(all_bindings)
    nd_bindings = df_bindings.iloc[:, 0].values

    return nd_peptides, nd_bindings


def encode_peptides_to_predict(peptides, encoding, encoding_name):
    """
    encodes given oneLetterCode of aminoacids into the passed encoding
    suitable for datasets on which predictions are performed
    :param peptides:
    :param encoding: usually blomap
    :param encoding_name:
    :return:
    """
    LOG.info("Encoding peptides to predict into " + encoding_name + " features")

    encoded_aminoacids = []
    for peptide_seq in peptides:
        properties = []
        for aminoacid in peptide_seq:
            if isinstance(aminoacid, str):
                properties.extend(encoding[aminoacid.upper()])
            else:
                properties.append(aminoacid)
        encoded_aminoacids.append(properties)

    df_encoded_aminoacids = pd.DataFrame(encoded_aminoacids)
    encoded_aminoacids = df_encoded_aminoacids.iloc[:, :].values

    LOG.info("Successfully encoded peptides to predict into " + encoding_name + " features")

    return encoded_aminoacids
