import datetime


def solution():
	result = sum(1
		for y in range(1901, 2001)
		for m in range(1, 13)
		if datetime.date(y, m, 1).weekday() == 6)
	return str(result)


if __name__ == "__main__":
	print(solution())
