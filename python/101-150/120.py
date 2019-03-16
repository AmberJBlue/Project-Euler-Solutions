def solve():
	result = sum(i * (i - (2 if i % 2 == 0 else 1)) for i in range(3, 1001))
	return str(result)


if __name__ == "__main__":
	print(solve())
