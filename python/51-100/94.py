import common, fractions, itertools

def solution():
	ceiling = 10**9
	result = 0
	for s in itertools.count(1, 2):
		if s * s > (ceiling + 1) // 3:
			break
		for t in range(s - 2, 0, -2):
			if fractions.gcd(s, t) == 1:
				a = s * t
				b = (s * s - t * t) // 2
				c = (s * s + t * t) // 2
				if a * 2 == c - 1:
					p = c * 3 - 1
					if p <= ceiling:
						result += p
				if a * 2 == c + 1:
					p = c * 3 + 1
					if p <= ceiling:
						result += p
				if b * 2 == c - 1:
					p = c * 3 - 1
					if p <= ceiling:
						result += p
				if b * 2 == c + 1:
					p = c * 3 + 1
					if p <= ceiling:
						result += p
	return str(result)


if __name__ == "__main__":
	print(solution())
