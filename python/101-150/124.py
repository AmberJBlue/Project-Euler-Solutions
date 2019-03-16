
def solve():
	ceiling = 100000

	radians = [0] + [1] * ceiling
	for i in range(2, len(radians)):
		if radians[i] == 1:
			for j in range(i, len(radians), i):
				radians[j] *= i
	
	data = sorted((radian, i) for (i, radian) in enumerate(radians))
	return str(data[10000][1])


if __name__ == "__main__":
	print(solve())
