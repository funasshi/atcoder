# from scipy.sparse import csr_matrix
import sys

a, b = list(map(int, input().split()))

if b-a==1 and b not in [1,4,7]:
    print("Yes")
else:
    print("No")
# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
