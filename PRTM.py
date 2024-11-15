def calculate_protein_mass(P):
    # Monoisotopic mass table for amino acids
    monoisotopic_mass_table = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
        'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
        'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
        'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
        'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
    }
    total_mass = 0
    for letter in P:
        total_mass += monoisotopic_mass_table[letter]
    return ("%.4f" % total_mass) # to reduce the number after the decimal point

protein_string = 'SKADYEK'
print(calculate_protein_mass(protein_string))