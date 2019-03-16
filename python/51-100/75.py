import common, fractions


def solution():
	ceiling = 1500000
	triples = set()
	for s in range(3, common.sqrt(ceiling) + 1, 2):
		for t in range(s - 2, 0, -2):
			if fractions.gcd(s, t) == 1:
				a = s * t
				b = (s * s - t * t) // 2
				c = (s * s + t * t) // 2
				if a + b + c <= ceiling:
					triples.add((a, b, c))
	
	ways = [0] * (ceiling + 1)
	for triple in triples:
		sigma = sum(triple)
		for i in range(sigma, len(ways), sigma):
			ways[i] += 1
	
	result = ways.count(1)
	return str(result)


if __name__ == "__main__":
	print(solution())
