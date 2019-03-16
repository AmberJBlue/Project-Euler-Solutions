import sys
if sys.version_info.major == 2:
	range = xrange


def solution():
	string = "".join(str(i) for i in range(1, 1000000))
	result = 1
	for i in range(7):
		result *= int(string[10**i - 1])
	return str(result)


if __name__ == "__main__":
	print(solution())
