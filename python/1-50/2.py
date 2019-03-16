
def solution():
	result = 0
	current = 1
	nextNum = 2
	while current <= 4000000:
		if current % 2 == 0:
			result += current
		current, nextNum = nextNum, current + nextNum
	return str(result)


if __name__ == "__main__":
	print(solution())
