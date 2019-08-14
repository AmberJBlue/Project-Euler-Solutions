package solutions

import (
	"assets/library"
)

func SumofPrimes() int {
	primes := assets.SieveOfEratosthenes(2000000)

	var sum int
	for _, prime := range primes {
		sum += prime
	}
	return sum
}