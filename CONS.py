def consensus_and_profile(dna_strings):

  string_length = len(dna_strings[0])
  profile = {'A': [0] * string_length, 'C': [0] * string_length,
             'G': [0] * string_length, 'T': [0] * string_length}

  for dna_string in dna_strings:
    for i, nucleotide in enumerate(dna_string):
      profile[nucleotide][i] += 1

  consensus = ""
  for i in range(string_length):
    max_count = 0
    consensus_nucleotide = ''
    for nucleotide in 'ACGT':
      if profile[nucleotide][i] > max_count:
        max_count = profile[nucleotide][i]
        consensus_nucleotide = nucleotide
    consensus += consensus_nucleotide

  return consensus, profile


dna_strings = [
    "ATCCAGCT",
    "GGGCAACT",
    "ATGGATCT",
    "AAGCAACC",
    "TTGGAACT",
    "ATGCCATT",
    "ATGGCACT"
]

consensus, profile = consensus_and_profile(dna_strings)

print(consensus)
for nucleotide in ['A', 'C', 'G', 'T']:
  print(nucleotide + ': ' + ' '.join(map(str, profile[nucleotide])))