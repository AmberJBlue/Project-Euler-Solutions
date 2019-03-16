import common, itertools


def solution():
	totients = common.list_totients(10**6)
	result = sum(itertools.islice(totients, 2, None))
	return str(result)


if __name__ == "__main__":
	print(solution())
