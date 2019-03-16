import itertools


def solution():
	result = max(range(1, 1000), key=cycles)
	return str(result)


def cycles(n):
	seen = {}
	x = 1
	for i in itertools.count():
		if x in seen:
			return i - seen[x]
		else:
			seen[x] = i
			x = x * 10 % n


if __name__ == "__main__":
	print(solution())
