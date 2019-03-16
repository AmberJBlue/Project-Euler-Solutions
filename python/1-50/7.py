
import common, itertools, sys
if sys.version_info.major == 2:
	filter = itertools.ifilter

def solution():
	result = next(
		itertools.islice(
			filter(common.prime, itertools.count(2)),
				10000,
				None
		))
	return str(result)


if __name__ == "__main__":
	print(solution())
