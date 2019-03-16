
def solution():
	result = max((n for n in range(2, 1001) if (not common.is_square(n))),
		key=smallest_solution_x)
	return str(result)


# Returns the smallest x such that x > 0 and there exists some y such that x^2 - n y^2 = 1.
# Requires n to not be a perfect square.
def smallest_solution_x(n):
	contfrac = sqrt_to_continued_fraction(n)
	temp = contfrac[0] + contfrac[1][ : -1]
	
	val = fractions.Fraction(temp[-1], 1)
	for term in reversed(temp[ : -1]):
		val = 1 / val + term
	
	if len(contfrac[1]) % 2 == 0:
		return val.numerator
	else:
		return val.numerator**2 + val.denominator**2 * n


# Returns the periodic continued fraction of sqrt(n). Requires n to not be a perfect square.
# result[0] is the minimal non-periodic prefix, and result[1] is the minimal periodic tail.
def sqrt_to_continued_fraction(n):
	terms = []
	seen = {}
	val = QuadraticSurd(0, 1, 1, n)
	while True:
		seen[val] = len(seen)
		flr = val.floor()
		terms.append(flr)
		val = (val - QuadraticSurd(flr, 0, 1, val.d)).reciprocal()
		if val in seen:
			break
	split = seen[val]
	return (terms[ : split], terms[split : ])



# Represents (a + b * sqrt(d)) / c. d must not be a perfect square.
class QuadraticSurd(object):
	
	def __init__(self, a, b, c, d):
		if c == 0:
			raise ValueError()
		
		# Simplify
		if c < 0:
			a = -a
			b = -b
			c = -c
		gcd = fractions.gcd(fractions.gcd(a, b), c)
		if gcd != 1:
			a //= gcd
			b //= gcd
			c //= gcd
		
		self.a = a
		self.b = b
		self.c = c
		self.d = d
	
	
	def __sub__(self, other):
		if self.d != other.d:
			raise ValueError()
		return QuadraticSurd(
			self.a * other.c - other.a * self.c,
			self.b * other.c - other.b * self.c,
			self.c * other.c,
			self.d)
	
	
	def reciprocal(self):
		return QuadraticSurd(
			-self.a * self.c,
			self.b * self.c,
			self.b * self.b * self.d - self.a * self.a,
			self.d)
	
	
	def floor(self):
		temp = common.sqrt(self.b * self.b * self.d)
		if self.b < 0:
			temp = -(temp + 1)
		temp += self.a
		if temp < 0:
			temp -= self.c - 1
		return temp // self.c
	
	
	def __eq__(self, other):
		return self.a == other.a and self.b == other.b \
		   and self.c == other.c and self.d == other.d
	
	def __ne__(self, other):
		return not (self == other)
	
	
	def __hash__(self):
		return hash(self.a) + hash(self.b) + hash(self.c) + hash(self.d)



if __name__ == "__main__":
	print(solution())
