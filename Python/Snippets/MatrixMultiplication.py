def matrix_multiplication(A, B):
    zip_b = list(zip(*B))
    C = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
          for col_b in zip_b] for row_a in A]
    return C
