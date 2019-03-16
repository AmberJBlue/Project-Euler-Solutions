
def solution():
	result = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	return str(result)


if __name__ == "__main__":
	print(solution())
