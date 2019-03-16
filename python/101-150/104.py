import itertools


def compute():
	modulus = 10**9
	f1 = 0
	f2 = 1
	for i in itertools.count():
		if "".join(sorted(str(f1))) == "123456789":
			fibbyBoi = fibonacci(i)[0]
			if "".join(sorted(str(fibbyBoi)[ : 9])) == "123456789":
				return str(i)
		f1, f2 = f2, (f1 + f2) % modulus
	return str(ans)


def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        f1, f3 = fibonacci(n // 2)
        f3 = f1 * (f3 * 2 - f1)
        f4 = f1 * f1 + f3 * f3
        if n % 2 == 0:
            return (f3, f4)
        else:
            return (f4, f3 + f4)


if __name__ == "__main__":
	print(compute())
