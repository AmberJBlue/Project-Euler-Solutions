import common


def solution():
	ceiling = 10000
	isprime = common.prime_check(ceiling - 1)
	for base in range(1000, ceiling):
		if isprime[base]:
			for step in range(1, ceiling):
				a = base + step
				b = a + step
				if     a < ceiling and isprime[a] and identical_digits(a, base) \
				   and b < ceiling and isprime[b] and identical_digits(b, base) \
				   and (base != 1487 or a != 4817):
					return str(base) + str(a) + str(b)
	raise RuntimeError("Not found")


def identical_digits(x, y):
	return sorted(str(x)) == sorted(str(y))


if __name__ == "__main__":
	print(solution())
