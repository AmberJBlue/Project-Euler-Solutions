
def solve():
	shots = [i * j for i in range(1, 21) for j in range(1, 4)] + [25, 50]
	twopointer = [i * 2 for i in range(1, 21)] + [25 * 2]
	
	possibilities = [[[None] * len(shots) for j in range(101)] for i in range(3)]
	
	def possibilities(plays, total, maxindex):
		if possibilities[plays][total][maxindex] is None:
			if plays == 0:
				result = 1 if total == 0 else 0
			else:
				result = 0
				if maxindex > 0:
					result += possibilities(plays, total, maxindex - 1)
				if shots[maxindex] <= total:
					result += possibilities(plays - 1, total - shots[maxindex], maxindex)
			possibilities[plays][total][maxindex] = result
		return possibilities[plays][total][maxindex]
	
	outs = 0
	for remainingshots in range(1, 100):
		for plays in range(3):
			for p in twopointer:
				if p <= remainingshots:
					outs += possibilities(plays, remainingshots - p, len(shots) - 1)
	return str(outs)


if __name__ == "__main__":
	print(solve())
