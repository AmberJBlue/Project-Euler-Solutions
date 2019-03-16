import itertools


modulo = 10**6

def solution():
	partitions = [1]
	for i in itertools.count(len(partitions)):
		item = 0
		for j in itertools.count(1):
			sign = -1 if j % 2 == 0 else +1
			index = (j * j * 3 - j) // 2
			if index > i:
				break
			item += partitions[i - index] * sign
			index += j  # index == (j * j * 3 + j) // 2
			if index > i:
				break
			item += partitions[i - index] * sign
			item %= modulo
		
		# Check or memoize the number
		if item == 0:
			return str(i)
		partitions.append(item)


if __name__ == "__main__":
	print(solution())
