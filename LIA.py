def probability(k, N):

  # Probability of AaBb offspring from a single AaBb parent mating with AaBb
  probability_AaBb = 0.25

  # Calculate the total number of organisms in the k-th generation
  total_organisms = 2**k

  # Calculate the probability of getting exactly i AaBb organisms using binomial distribution
  def binomial_probability(n, p, i):
    if i < 0 or i > n:
      return 0
    if i == 0:
      return (1 - p) ** n
    if i == n:
      return p ** n

    dp = [[0 for _ in range(i + 1)] for _ in range(n + 1)]

    for j in range(n + 1):
      for x in range(min(j, i) + 1):
        if x == 0 and j == 0:
          dp[j][x] = 1
        elif x == 0:
          dp[j][x] = dp[j - 1][x] * (1 - p)
        elif x == j:
          dp[j][x] = dp[j - 1][x - 1] * p
        else:
          dp[j][x] = dp[j - 1][x - 1] * p + dp[j - 1][x] * (1 - p)

    return dp[n][i]


  probability_at_least_N = 0
  for i in range(N, total_organisms + 1):
    probability_at_least_N += binomial_probability(total_organisms, probability_AaBb, i)

  return ("%.4f" % probability_at_least_N)

k = 2  
N = 1  
print(probability(k, N))