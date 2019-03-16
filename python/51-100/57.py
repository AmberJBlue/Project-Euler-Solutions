def solution():
	ceiling = 1000
	result = 0
	numer = 0
	denom = 1
	for _ in range(ceiling):
		numer, denom = denom, denom * 2 + numer
		# Now numer/denom is the i'th (0-based) continued fraction approximation of sqrt(2) - 1
		if len(str(numer + denom)) > len(str(denom)):
			result += 1
	return str(result)


if __name__ == "__main__":
	print(solution())
