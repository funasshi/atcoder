# from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**9)


# n = int(input())
a, b = list(map(int, input().split()))

c=a+b

ans=0
while True:
    if ans!=c:
        print(ans)
        break
    ans+=1

# a_list = list(map(int, input().split()))

# n, m = list(map(int, input().split()))


# row = []
# col = []

# for i in range(m):
#     u, v = list(map(int, input().split()))
#     row.append(u-1)
#     col.append(v-1)

# data = [1]*len(row)

# matrix = csr_matrix((data, (row, col)), (n, n))
