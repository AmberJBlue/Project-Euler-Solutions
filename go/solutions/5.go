package solutions

import ( 
	"math"
)

func SmallestMult() float64{
	var result float64 = 1
	
	var i float64
	
	for i = 1 ; i < 21; i++ {
		gcd_float := float64(GCD(int(i),int(result)))
		result *= math.Floor(i / gcd_float)
	}
	return result
}

func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}