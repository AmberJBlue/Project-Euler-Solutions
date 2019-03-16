def solution():
	result = ""
	for n in range(2, 10):
		for i in range(1, 10**(9 // n)):
			s = "".join(str(i * j) for j in range(1, n + 1))
			if "".join(sorted(s)) == "123456789":
				result = max(s, result)
	return result


if __name__ == "__main__":
	print(solution())
