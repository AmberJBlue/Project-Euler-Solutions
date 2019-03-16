import common

def result():
	result = sum(common.findPrimes(1999999))
	return str(result)

if __name__ == "__main__":
	print(result())
