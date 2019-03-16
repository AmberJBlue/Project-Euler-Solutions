import sys
if sys.version_info.major == 2:
	range = xrange


def solution():
	result = sum(1
		for i in range(1, 10000000)
		if get_chain(i) == 89)
	return str(result)


chain = (1, 89)

def get_chain(n):
	while n not in chain:
		n = square_digit_chain(n)
	return n


def square_digit_chain(n):
	result = 0
	while n > 0:
		result += total[n % 1000]
		n //= 1000
	return result

total = [sum(int(c)**2 for c in str(i)) for i in range(1000)]


if __name__ == "__main__":
	print(solution())
