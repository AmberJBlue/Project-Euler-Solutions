def solution():
	spiral = 1001
	result = 1
	result += sum(4 * i * i - 6 * (i - 1) for i in range(3, spiral + 1, 2))
	return str(result)


if __name__ == "__main__":
	print(solution())
