import common


def solution():
	result = sum(i for i in range(1, 10000) if pandigital_prod_check(i))
	return str(result)


def pandigital_prod_check(n):
	for i in range(1, common.root(n) + 1):
		if n % i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False


if __name__ == "__main__":
	print(solution())
