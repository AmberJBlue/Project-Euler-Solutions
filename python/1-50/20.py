import math

def solution():
	n = math.factorial(100)
	result = sum(int(c) for c in str(n))
	return str(result)


if __name__ == "__main__":
	print(solution())
