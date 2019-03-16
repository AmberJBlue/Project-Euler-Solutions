def solution():
	result = sum(len(getWord(i)) for i in range(1, 1001))
	return str(result)


def getWord(n):
	if 0 <= n < 20:
		return integers[n]
	elif 20 <= n < 100:
		return multsOfTen[n // 10] + (integers[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return integers[n // 100] + "hundred" + (("and" + getWord(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return getWord(n // 1000) + "thousand" + (getWord(n % 1000) if (n % 1000 != 0) else "")
	else:
		raise ValueError()


integers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
multsOfTen = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


if __name__ == "__main__":
	print(solution())
