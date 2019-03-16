def solution():
	numer = 1
	denom = 0
	for i in reversed(range(100)):
		numer, denom = e_contfrac_term(i) * numer + denom, numer
	result = sum(int(c) for c in str(numer))
	return str(result)


def e_contfrac_term(i):
	if i == 0:
		return 2
	elif i % 3 == 2:
		return i // 3 * 2 + 2
	else:
		return 1


if __name__ == "__main__":
	print(solution())
