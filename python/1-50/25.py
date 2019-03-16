import itertools

def solution():
	length = 1000
	previous = 1
	current = 0
	for i in itertools.count():
		if len(str(current)) > length:
			raise RuntimeError("Not found")
		elif len(str(current)) == length:
			return str(i)
		
		# Advance the Fibonacci sequence by one step
		previous, current = current, previous + current


if __name__ == "__main__":
	print(solution())
