def solution():
	ceiling = 51
	result = sum(1
		for x1 in range(ceiling)
		for y1 in range(ceiling)
		for x2 in range(ceiling)
		for y2 in range(ceiling)
		if y2 * x1 < y1 * x2 and right_triangle_check(x1, y1, x2, y2))
	return str(result)


def right_triangle_check(x1, y1, x2, y2):
	a = x1**2 + y1**2
	b = x2**2 + y2**2
	c = (x2 - x1)**2 + (y2 - y1)**2
	return (a + b == c) or (b + c == a) or (c + a == b)


if __name__ == "__main__":
	print(solution())
