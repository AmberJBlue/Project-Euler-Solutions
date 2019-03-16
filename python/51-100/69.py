import common, fractions


def solution():
	totients = common.list_totients(10**6)
	result = max(range(2, len(totients)), key=(lambda i: fractions.Fraction(i, totients[i])))
	return str(result)


if __name__ == "__main__":
	print(solution())
