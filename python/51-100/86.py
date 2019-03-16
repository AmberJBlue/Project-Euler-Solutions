import fractions, itertools


def solution():
	paths = []
	
	
	def find_paths():
		for s in itertools.count(3, 2):
			for t in range(s - 2, 0, -2):
				if s * s // 2 >= ceiling * 3:
					return
				
				if fractions.gcd(s, t) == 1:
					for k in itertools.count(1):
						a = s * t * k
						b = (s * s - t * t) // 2 * k
						c = (s * s + t * t) // 2 * k
						if a >= ceiling and b >= ceiling:
							break
						find_splits(a, b, c)
						find_splits(b, a, c)
	
	
	def find_splits(a, b, c):
		z = b
		for x in range(1, a):
			y = a - x
			if y < x:
				break
			if c * c == min(
					(x + y) * (x + y) + z * z,
					(y + z) * (y + z) + x * x,
					(z + x) * (z + x) + y * y):
				temp = max(x, y, z)
				if temp < ceiling:
					# Add canonical solution
					item = tuple(sorted((x, y, z)))
					paths[temp].add(item)
	
	
	cumulativepaths = [0]
	
	ceiling = 1
	while True:
		while len(paths) < ceiling:
			paths.append(set())
		
		find_paths()
		
		for i in range(len(cumulativepaths), ceiling):
			sum = cumulativepaths[i - 1] + len(paths[i])
			cumulativepaths.append(sum)
			if sum > 1000000:
				return str(i)
		
		ceiling *= 2


if __name__ == "__main__":
	print(solution())
