import itertools

def solve():
	INDEX = 30  # 1-based
	limit = 1
	while True:
		numbers = set()
		x = 2
		while (1 << x) < limit:
			for n in itertools.count(2):
				power = n**x
				if power >= limit and len(str(power)) * 9 < n:
					break
				if power >= 10 and validate(power):
					numbers.add(power)
			x += 1
		if len(numbers) >= INDEX:
			return str(sorted(numbers)[INDEX - 1])
		limit <<= 8


def validate(x):
	total = sum(int(c) for c in str(x))
	if total == 1:
		return False
	power = total
	while power < x:
		power *= total
	return power == x


if __name__ == "__main__":
	print(solve())
