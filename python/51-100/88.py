def solution():
	ceiling = 12000
	minsumproduct = [None] * (ceiling + 1)
	
	def factorize(n, remain, maxfactor, sum, terms):
		if remain == 1:
			if sum > n:  # Without using factors of 1, the sum never exceeds the product
				raise AssertionError()
			terms += n - sum
			if terms <= ceiling and (minsumproduct[terms] is None or n < minsumproduct[terms]):
				minsumproduct[terms] = n
		else:
			for i in range(2, maxfactor + 1):
				if remain % i == 0:
					factor = i
					factorize(n, remain // factor, min(factor, maxfactor), sum + factor, terms + 1)
	
	for i in range(2, ceiling * 2 + 1):
		factorize(i, i, i, 0, 0)
	
	result = sum(set(minsumproduct[2 : ]))
	return str(result)


if __name__ == "__main__":
	print(solution())
