import common


def solution():
	result = sum(1
		for n in range(1, 101)
		for k in range(0, n + 1)
		if common.binomial(n, k) > 1000000)
	return str(result)


if __name__ == "__main__":
	print(solution())
