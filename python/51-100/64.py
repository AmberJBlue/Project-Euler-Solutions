import common, math


def solution():
	result = sum(1 for i in range(1, 10001) if (not common.is_square(i) and get_sqrt_continued_fraction_period(i) % 2 == 1))
	return str(result)


def get_sqrt_continued_fraction_period(n):
	seen = {}
	val = QuadraticSurd(0, 1, 1, n)
	while True:
		seen[val] = len(seen)
		val = (val - QuadraticSurd(val.floor(), 0, 1, val.d)).reciprocal()
		if val in seen:
			return len(seen) - seen[val]


class QuadraticSurd(object):
	
	def __init__(self, a, b, c, d):
		if c == 0:
			raise ValueError()
		
		# Simplify
		if c < 0:
			a = -a
			b = -b
			c = -c
		gcd = math.gcd(math.gcd(a, b), c)
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
