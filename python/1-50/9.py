
def solution():
	outer = 1000
	for a in range(1, outer + 1):
		for b in range(a + 1, outer + 1):
			c = outer - a - b
			if a * a + b * b == c * c:
				return str(a * b * c)


if __name__ == "__main__":
	print(solution())
