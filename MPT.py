def maximumPerimeterTriangle(sticks):
  sticks.sort()
  n = len(sticks)
  max_perimeter = -1
  result = [-1]
  for i in range(n - 2):
    a = sticks[i]
    b = sticks[i + 1]
    c = sticks[i + 2]
    if a + b > c:
      perimeter = a + b + c
      if perimeter > max_perimeter:
        max_perimeter = perimeter
        result = [a, b, c]
      elif perimeter == max_perimeter:
        if c > result[2]:
          result = [a, b, c]
        elif c == result[2] and a > result[0]:
          result = [a, b, c]
  return result

n = [1,1,1,2,3,5]
print(*maximumPerimeterTriangle(n))