import numpy as np

a = np.array([[5, 10], [9, 20]], dtype=np.uint8)
b = np.array([[10, 4], [6, 12]], dtype=np.uint8)

# * Soal 1: Penjumlahan matriks
result_sum_matriks = a + b
print(f"{"="*10} {"penjumlah matriks".upper()} {"="*10}")
print(result_sum_matriks)

# * Soal 2: Perkalian matriks (dot product)
result_dot_matriks = np.dot(a, b)
print(f"{"="*10} {"perkalian 2 matriks".upper()} {"="*10}")
print(result_dot_matriks)

# * Soal 3: Transpose dari matriks hasil perkalian tersebut.
result_transpose_matriks_a = np.transpose(a)
print(f"{"="*10} {"transpose matriks a".upper()} {"="*10}")
print(result_transpose_matriks_a)
    
result_transpose_matriks_b = np.transpose(b)
print(f"{"="*10} {"transpose matriks b".upper()} {"="*10}")
print(result_transpose_matriks_b)