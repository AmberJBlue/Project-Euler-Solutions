def solution():
	ceiling = 28124
	total = [0] * ceiling
	for i in range(1, ceiling):
		for j in range(i * 2, ceiling, i):
			total[j] += i
	abundant = [i for (i, x) in enumerate(total) if x > i]
	
	perfectNum = [False] * ceiling
	for i in abundant:
		for j in abundant:
			if i + j < ceiling:
				perfectNum[i + j] = True
			else:
				break
	
	result = sum(i for (i, x) in enumerate(perfectNum) if not x)
	return str(result)


if __name__ == "__main__":
	print(solution())
