import common


def solution():
	for n in reversed(range(2, 10)):
		arr = list(reversed(range(1, n + 1)))
		while True:
			if arr[-1] not in notPrime:
				n = int("".join(str(x) for x in arr))
				if common.prime(n):
					return str(n)
			if not last_call(arr):
				break
	raise AssertionError()

notPrime = {0, 2, 4, 5, 6, 8}


def last_call(arr):
	i = len(arr) - 1
	while i > 0 and arr[i - 1] <= arr[i]:
		i -= 1
	if i <= 0:
		return False
	j = len(arr) - 1
	while arr[j] >= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True


if __name__ == "__main__":
	print(solution())
