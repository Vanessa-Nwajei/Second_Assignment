def generate_permutations(n):
  if n == 0:
    return [[]]
  else:
    permutations = []
    for previous_permutation in generate_permutations(n - 1):
      for i in range(n):
        new_permutation = previous_permutation[:]
        new_permutation.insert(i, n)
        permutations.append(new_permutation)
    return permutations
  
#a funtion to return the lenght of permutation
def permution_output(n):
  permutation = generate_permutations(n)
  print(len(permutation))
  for p in permutation:
    print(*p)
  
n = 3
print(permution_output(n))