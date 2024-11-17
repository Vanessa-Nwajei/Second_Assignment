def transition_transversion_ratio(s1, s2):

  transitions = 0
  transversions = 0

  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if (s1[i] == 'A' and s2[i] == 'G') or (s1[i] == 'G' and s2[i] == 'A') or \
         (s1[i] == 'C' and s2[i] == 'T') or (s1[i] == 'T' and s2[i] == 'C'):
        transitions += 1
      else:
        transversions += 1

  if transversions == 0:
    return 0.0
  else:
    return ("%.11f" % (transitions / transversions))


s1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
s2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

ratio = transition_transversion_ratio(s1, s2)
print(ratio)