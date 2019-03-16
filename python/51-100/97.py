def solution():
	modulo = 10**10
	result = (28433 * pow(2, 7830457, modulo) + 1) % modulo
	return str(result)


if __name__ == "__main__":
	print(solution())
