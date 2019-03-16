from ... import common

def compute():
	SET_SIZE = 12
	
	def catalan(n):
		return common.binomial(n * 2, n) // (n + 1)
	
	ans = sum(common.binomial(SET_SIZE, i * 2) * (common.binomial(i * 2, i) // 2 - catalan(i))
		for i in range(2, SET_SIZE // 2 + 1))
	return str(ans)


if __name__ == "__main__":
	print(compute())
