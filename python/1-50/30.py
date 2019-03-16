import sys
if sys.version_info.major == 2:
	range = xrange


def solution():
	# As stated in the problem, 1 = 1^5 is excluded.
	# If a number has at least n >= 7 digits, then even if every digit is 9,
	# n * 9^5 is still less than the number (which is at least 10^n).
	result = sum(i for i in range(2, 1000000) if i == fifth_power(i))
	return str(result)


def fifth_power(n):
	return sum(int(c)**5 for c in str(n))


if __name__ == "__main__":
	print(solution())
