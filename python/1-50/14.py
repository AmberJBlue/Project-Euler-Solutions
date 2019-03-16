import common, sys
if sys.version_info.major == 2:
	range = xrange

def solution():
	sys.setrecursionlimit(3000)
	result = max(range(1, 1000000), key=longest_collatz)
	return str(result)


@common.memoize
def longest_collatz(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		y = x // 2
	else:
		y = x * 3 + 1
	return longest_collatz(y) + 1


if __name__ == "__main__":
	print(solution())
