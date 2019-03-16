def solution():
	modulo = 10**10
	result = sum(pow(i, i, modulo) for i in range(1, 1001)) % modulo
	return str(result)


if __name__ == "__main__":
	print(solution())
