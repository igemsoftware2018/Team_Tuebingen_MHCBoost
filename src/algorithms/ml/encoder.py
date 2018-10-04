import logging
import pandas as pd

from numpy import array

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Encoder")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def encode_training_data(peptides, encoding, encoding_name):
    LOG.info("Encoding training datasets into " + encoding_name + " values")
    nd_peptides, nd_bindings = training_data_to_nd_arrays(peptides)

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
    encodes given oneLetterCode of aminoacids in the encodingfunction given
    """
    LOG.info("Encoding aminoacids into " + encoding_name + " features")

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

    LOG.info("Successfully encoded aminoacids into " + encoding_name + " features")

    return encoded_aminoacids
