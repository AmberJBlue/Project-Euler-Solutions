
import itertools

def solve():
	ceiling = 10**6
	for n in itertools.count(ceiling):
		if smallest_result(n) > ceiling:
			return str(n)


def smallest_result(n):
	if n % 2 == 0 or n % 5 == 0:
		return 0
	k = 1
	s = 1
	p = 1
	while s % n != 0:
		k += 1
		p = p * 10 % n
		s = (s + p) % n
	return k


if __name__ == "__main__":
	print(solve())
