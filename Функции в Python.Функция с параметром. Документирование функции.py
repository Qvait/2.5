def get_matrix(n, m, value):
  matrix = []
  for _ in range(n):
    row = [value] * m
    matrix.append(row)
  return matrix

matrix = get_matrix(3, 4, 2)
print(matrix)