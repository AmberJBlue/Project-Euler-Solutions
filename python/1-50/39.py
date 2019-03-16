def solution():
	result = max(range(1, 1001), key=max_solutions)
	return str(result)


def max_solutions(p):
	result = 0
	for a in range(1, p + 1):
		for b in range(a, (p - a) // 2 + 1):
			c = p - a - b  # c >= b
			if a * a + b * b == c * c:
				result += 1
	return result


if __name__ == "__main__":
	print(solution())
