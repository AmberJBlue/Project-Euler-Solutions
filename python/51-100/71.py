import sys
if sys.version_info.major == 2:
	range = xrange

def solution():
	ceiling = 1000000
	maxnumer = 0
	maxdenom = 1
	for d in range(1, ceiling + 1):
		n = d * 3 // 7
		if d % 7 == 0:
			n -= 1
		if n * maxdenom > d * maxnumer:  # n/d > maxdenom/maxnumer
			maxnumer = n
			maxdenom = d
	return str(maxnumer)


if __name__ == "__main__":
	print(solution())
