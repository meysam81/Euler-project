n = 21
count = 0
mat = [[0 for x in range(0, n)] for y in range(0, n)]
for i in range(0, n):
	for j in range(0, n):
		if i == 0 or j == 0:
			mat [i][j] = 1
		else:
			mat[i][j] = mat[i][j - 1] + mat[i - 1][j]
#for i in range(0, n):
#	print(mat[i][:])
print(mat[n - 1][n - 1])