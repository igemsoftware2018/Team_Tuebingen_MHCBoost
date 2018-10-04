def generate_k_mer(k, input_string):
    k_mers = []
    limit = len(input_string) - k + 1

    k_mer = ""
    for k_mer_start in range(0, limit):
        for AA in range(k_mer_start, k_mer_start + k):
            k_mer += input_string[AA]

        k_mers.append(k_mer)  # we finished a k-mer -> add it
        k_mer = ""  # reset k-mer to begin another one

    return k_mers


