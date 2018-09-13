class Peptide:

    def __init__(self, species, mhc_allele, length, sequence, inequality, meas):
        self.species = species
        self.mhc_allele = mhc_allele
        self.length = length
        self.sequence = sequence
        self.inequality = inequality
        self.meas = meas
        self.binding = float(self.meas) <= 500

    def __str__(self):
        ret_str = ""

        ret_str += ("Species: " + self.species + "\n")
        ret_str += ("MHC Allele: " + self.mhc_allele + "\n")
        ret_str += ("Length: " + str(self.length) + "\n")
        ret_str += ("Sequence: " + self.sequence + "\n")
        ret_str += ("Inequality: " + self.inequality + "\n")
        ret_str += ("meas: " + str(self.meas) + "\n")
        ret_str += ("binding" + str(self.binding) + "\n")

        return ret_str

    def __repr__(self):
        return str(self)
