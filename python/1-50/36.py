import sys
if sys.version_info.major == 2:
	range = xrange


def solution():
	result = sum(i for i in range(1000000) if double_base_palindrome(i))
	return str(result)


def double_base_palindrome(n):
	string = str(n)
	if string != string[ : : -1]:
		return False
	binary = bin(n)[2 : ]
	return binary == binary[ : : -1]


if __name__ == "__main__":
	print(solution())
