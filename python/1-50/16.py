
def solution():
	n = 2**1000
	result = sum(int(c) for c in str(n))
	return str(result)


if __name__ == "__main__":
	print(solution())
