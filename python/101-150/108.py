
import common, itertools
def solve():
	for n in itertools.count(1):
		if (divisorCount(n) + 1) // 2 > 1000:
			return str(n)


def divisorCount(n):
	count = 1
	end = common.sqrt(n)
	for i in itertools.count(2):
		if i > end:
			break
		if n % i == 0:
			j = 0
			while True:
				n //= i
				j += 1
				if n % i != 0:
					break
			count *= j * 2 + 1
			end = common.sqrt(n)
	if n != 1:
		count *= 3
	return count


if __name__ == "__main__":
	print(solve())
