def generate_k_mer(k, input_string):
    k_mers = []
    limit = len(input_string) - k + 1

    for index, item in zip(range(limit), input_string):
        k_mers.append(input_string[index] + input_string[index + 1])

    return k_mers


