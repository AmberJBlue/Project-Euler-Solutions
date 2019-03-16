def solution():
	ceiling = 100
	partitions = []
	for i in range(ceiling + 1):
		partitions.append([None] * (ceiling + 1))
		for j in reversed(range(ceiling + 1)):
			if j == i:
				val = 1
			elif j > i:
				val = 0
			elif j == 0:
				val = partitions[i][j + 1]
			else:
				val = partitions[i][j + 1] + partitions[i - j][j]
			partitions[i][j] = val
	
	result = partitions[ceiling][1] - 1
	return str(result)


if __name__ == "__main__":
	print(solution())
