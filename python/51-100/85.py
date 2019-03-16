import common


def solution():
	goal = 2000000
	end = common.sqrt(goal) + 1
	gen = ((w, h) for w in range(1, end) for h in range(1, end))
	func = lambda wh: abs(num_rectangles(*wh) - goal)
	result = min(gen, key=func)
	return str(result[0] * result[1])


def num_rectangles(m, n):
	return (m + 1) * m * (n + 1) * n // 4  # A bit more than m^2 n^2 / 4


if __name__ == "__main__":
	print(solution())
