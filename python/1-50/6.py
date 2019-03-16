
def solution():
	N = 100
	s = sum(i for i in range(1, N + 1))
	s2 = sum(i**2 for i in range(1, N + 1))
	return str(s**2 - s2)


if __name__ == "__main__":
	print(solution())
