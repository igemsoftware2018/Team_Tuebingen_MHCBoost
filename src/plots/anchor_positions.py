import matplotlib.pyplot as plt

from src.model.encoding import extended_blomap


def plot_anchor_positions_scatter(peptides, predictions):
    """
    creates plots of anchor positions (aminoacid no.2, 9) of peptides
    :param peptides:
    :param predictions:
    :return:
    """
    peptides = peptides.tolist()
    predictions = predictions.tolist()

    # to be plotted positions (2, 9 = anchor positions)
    positions = [2, 9]

    for i in range(len(peptides)):
        peptides[i].append(predictions[i])

    # compute informations for non-/binder peptide at positions
    scatter_point_datas = []
    for position in positions:
        collected_acids = collect_acids_at_positions(peptides, position)
        for element in collected_acids:
            scatter_point_datas.append(collect_scatter_point_information(element))

    create_plots(scatter_point_datas)


def collect_acids_at_positions(samples, position):
    """
    collect acids at anchor positions

    Parameters
    ----------
    samples : list of Strings
        one letter Code of aminoacids for peptides
    position : list of Integers
        list of positions to be plotted

    Returns
    -------
    list
        contains two lists, both contain their given position,
        wether they belong to binder or nonbinder peptide, and
        all aminoacids at this position

    """
    # save position and binderclass
    binder_acids_at_position = [position, True]
    nonbinder_acids_at_position = [position, False]
    position -= 1

    # add acid at position for binder and nonbinder
    for sample in samples:
        if sample[len(sample) - 1] == 1:
            binder_acids_at_position.append(sample[position])
        else:
            nonbinder_acids_at_position.append(sample[position])

    return [binder_acids_at_position, nonbinder_acids_at_position]


def collect_scatter_point_information(collected_acids):
    """
    extracts information for aminoacids from blomap,
    computes quantities of each aminoacid

    Parameters
    ----------
    collected_acids : list
        contains position in peptide,
        wether it belongs to binder or nonbinder peptide, and
        all aminoacids at it's position

    Returns
    -------
    list
        contains position in peptide,
        wether it belongs to binder or nonbinder peptide,
        iep, hydrophobicity, and quantity of each aminoacid

    """
    # save position and binderclass
    scatter_point_information = [collected_acids[0], collected_acids[1]]

    # gather scatter informations: iep, hydrophobicity, quantity
    oneLetterCodes = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                      'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

    isoelectric_point, hydrophobicity = extract_information_from_blomap(oneLetterCodes)
    scatter_point_information.append(isoelectric_point)
    scatter_point_information.append(hydrophobicity)

    quantity_of_acids = compute_quantity_of_acids(oneLetterCodes, collected_acids)
    scatter_point_information.append(quantity_of_acids)

    return scatter_point_information


def extract_information_from_blomap(oneLetterCodes):
    """
    extracts isoelectric point (iep) and
    hydrophobicity from blomap for each aminoacid

    Parameters
    ----------
    oneLetterCodes : list of Strings/Chars
        contains oneLetterCode for each aminoacid

    Returns
    -------
    float, float
        iep, hydrophobicity

    """
    letter_encodings = []
    for x in oneLetterCodes:
        letter_encodings.append(extended_blomap[x.upper()])

    isoelectric_point = []
    hydrophobicity = []
    for element in letter_encodings:
        isoelectric_point.append([element[7]])
        hydrophobicity.append([element[8]])

    return isoelectric_point, hydrophobicity


def compute_quantity_of_acids(oneLetterCodes, collected_acids):
    """
    computes quantity for each aminoacid

    Parameters
    ----------
    oneLetterCodes : list of Strings/Chars
        contains oneLetterCode for each aminoacid
    collected_acids : list
        contains position in peptide,
        wether it belongs to binder or nonbinder peptide, and
        all aminoacids at it's position

    Returns
    -------
    list of Integer
        quantity of each aminoacid sorted after oneLetterCode

    """
    quantity_of_acids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(2, len(collected_acids)):
        for letter in oneLetterCodes:
            if collected_acids[i] == letter:
                quantity_of_acids[oneLetterCodes.index(letter)] += 1

    return quantity_of_acids


def create_plots(data):
    """
    draws scatter plots

    Parameters
    ----------
    data : list
        contains position in peptide,
        whether it belongs to binder or nonbinder peptide,
        iep, hydrophobicity, and quantity of each aminoacid

    Returns
    -------
    -

    """
    for scatter_data in data:
        position = scatter_data[0]
        if scatter_data[1]:
            binder = "binder"
            color = "red"
        else:
            binder = "nonbinder"
            color = "blue"

        plt.clf()
        plt.title(binder + " sequences at position " + str(position))
        plt.xlabel("Isoelectric point")
        plt.ylabel("Hydrophobicity")

        # increase s (=scaling) of plot-points 20 times
        plt.scatter(scatter_data[2], scatter_data[3], s=[y * 20 for y in scatter_data[4]], c=color)
        # plt.savefig('data/plots/' + binder + "_pos0" + str(position) + '.png')
        plt.show()
