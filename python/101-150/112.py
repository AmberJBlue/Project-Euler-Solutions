import itertools

def solve():
	count = 0
	for i in itertools.count(1):
		x = str(i)
		y = "".join(sorted(x))
		if x != y and x[ : : -1] != y:
			count += 1  # i is bouncy
		if count * 100 == 99 * i:
			return str(i)


if __name__ == "__main__":
	print(solve())
