def solution():
	sum = [0] * 10000
	for i in range(1, len(sum)):
		for j in range(i * 2, len(sum), i):
			sum[j] += i
	
	result = 0
	for i in range(1, len(sum)):
		j = sum[i]
		if j != i and j < len(sum) and sum[j] == i:
			result += i
	return str(result)


if __name__ == "__main__":
	print(solution())
