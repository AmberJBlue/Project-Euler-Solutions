import itertools


def solution():
	result = sum(int("".join(map(str, num)))
		for num in itertools.permutations(list(range(10)))
		if divisible_check(num))
	return str(result)


pandigital_divisors = [2, 3, 5, 7, 11, 13, 17]

def divisible_check(num):
	return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0
		for (i, p) in enumerate(pandigital_divisors))


if __name__ == "__main__":
	print(solution())
