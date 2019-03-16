def solution():
	x = set(a**b for a in range(2, 101) for b in range(2, 101))
	return str(len(x))


if __name__ == "__main__":
	print(solution())
