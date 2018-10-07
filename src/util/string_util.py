import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("String Util")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def generate_k_mer(input_string, k):
    """
    generates k-mers of a given input strings
    :param input_string: string which is split into k-mers
    :param k: length of the k-mers
    :return: list of generated k-mers
    """
    LOG.debug("Generating " + str(k) + "mer of " + input_string)
    k_mers = []
    k = int(k)
    limit = len(input_string) - k + 1

    k_mer = ""
    for k_mer_start in range(0, limit):
        for AA in range(k_mer_start, k_mer_start + k):
            k_mer += input_string[AA]

        k_mers.append(k_mer)  # we finished a k-mer -> add it
        k_mer = ""  # reset k-mer to begin another one

    LOG.debug("Successfully generated " + str(k) + "mer of " + input_string)

    return k_mers
