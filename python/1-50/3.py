import common

def solution():
	n = 600851475143
	while True:
		p = smallFactor(n)
		if p < n:
			n //= p
		else:
			return str(n)


def smallFactor(n):
	# the number must be greater than or equal to 2,
	# otherwise throw an error
	assert n >= 2
	for i in range(2, common.root(n) + 1):
		if n % i == 0:
			return i
	return n  


if __name__ == "__main__":
	print(solution())
