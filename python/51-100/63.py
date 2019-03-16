def solution():
	result = sum(1
		for i in range(1, 10)
		for j in range(1, 22)
		if len(str(i**j)) == j)
	return str(result)


if __name__ == "__main__":
	print(solution())
