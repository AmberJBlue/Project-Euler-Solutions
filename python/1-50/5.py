
import fractions

def solution():
	result = 1
	for i in range(1, 21):
		result *= i // fractions.gcd(i, result)
	return str(result)


if __name__ == "__main__":
	print(solution())
