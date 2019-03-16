import itertools


def solution():
	charsused = sorted(set().union(*seqs))
	base = len(charsused)

	for length in itertools.count(base):
		indices = [0] * length
		while True:
			guess = "".join(charsused[d] for d in indices)
			if is_consistent(guess):
				return guess
			
			i = 0
			while i < length and indices[i] == base - 1:
				indices[i] = 0
				i += 1
			if i == length:
				break
			indices[i] += 1


def is_consistent(guess):
	return all(subsequence_check(s, guess) for s in seqs)


def subsequence_check(shortstr, longstr):
	i = 0
	for c in longstr:
		if c == shortstr[i]:
			i += 1
			if i == len(shortstr):
				return True
	return False


seqs = ["319", "680", "180", "690", "129", "620", "762", "689", "762", "318", "368", "710", "720", "710", "629", "168", "160", "689", "716", "731", "736", "729", "316", "729", "729", "710", "769", "290", "719", "680", "318", "389", "162", "289", "162", "718", "729", "319", "790", "680", "890", "362", "319", "760", "316", "729", "380", "319", "728", "716"]


if __name__ == "__main__":
	print(solution())
