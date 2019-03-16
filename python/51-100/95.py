import itertools


def solution():
	ceiling = 10**6
	
	divisorsum = [0] * (ceiling + 1)
	for i in range(1, ceiling + 1):
		for j in range(i * 2, ceiling + 1, i):
			divisorsum[j] += i
	
	maxchainlen = 0
	result = -1
	for i in range(ceiling + 1):
		visited = set()
		cur = i
		for count in itertools.count(1):
			visited.add(cur)
			next = divisorsum[cur]
			if next == i:
				if count > maxchainlen:
					result = i
					maxchainlen = count
				break
			elif next > ceiling or next in visited:
				break
			else:
				cur = next
	
	return str(result)


if __name__ == "__main__":
	print(solution())
