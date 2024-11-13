def reverse_complement(dna):
    #complement the strand, replaceing A with t, T with a, C with g and G with c
    dna = dna.replace('A', 't').replace('G', 'c').replace('T', 'a').replace('C', 'g')
    dna =dna.upper() 
    #reverse the strand
    dna = dna[::-1]

    return dna

def find_restriction_sites(dna):
  sites = []
  for i in range(len(dna)):
    for j in range(i + 4, min(i + 13, len(dna))):  # Length 4-12
      substring = dna[i:j]
      if substring == reverse_complement(substring):
        sites.append((i + 1, j - i))
  return sites

dna_string = "TCAATGCATGCGGGTCTATATGCAT"  

results = find_restriction_sites(dna_string)

for position, length in results:
  print(position, length)