package solutions

import (
	"math/big"
)

func FactorialSum() int{
	var factorial = new(big.Int)
	factorial.MulRange(1, 100)

	str := factorial.String()
	sum := 0
	for _, val := range str {
		sum += int(val - '0')
	}
	return sum
}
