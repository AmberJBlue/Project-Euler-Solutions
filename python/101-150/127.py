
import fractions

def solve():
	ceiling = 120000
	
	radians = [0] + [1] * (ceiling - 1)
	for i in range(2, len(radians)):
		if radians[i] == 1:
			for j in range(i, len(radians), i):
				radians[j] *= i
	
	ordered = sorted((rad, n) for (n, rad) in enumerate(radians))
	ordered = ordered[1 : ]  # Get rid of the (0, 0) entry
	
	ans = 0
	for c in range(2, ceiling):
		for (rad, a) in ordered:
			rad *= radians[c]
			if rad >= c:
				break
			b = c - a
			if a < b and rad * radians[b] < c and fractions.gcd(a, b) == 1:
				ans += c
	return str(ans)


if __name__ == "__main__":
	print(solve())
