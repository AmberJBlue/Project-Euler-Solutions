import itertools


def solution():
	cond = lambda i: all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7))
	result = next(i for i in itertools.count(1) if cond(i))
	return str(result)


if __name__ == "__main__":
	print(solution())
