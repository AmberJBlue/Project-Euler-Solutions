package solutions

import (
	"math"
	"fmt"
	"strings"
	"strconv"
)
func PowerDigitSum() int {
	var n float64 = 1000
	var result int
	
	product := fmt.Sprintf("%f", (math.Pow(2, n)))
	productArr := strings.Split(product, "")

	for _, number := range productArr {
		if number != "." {
			val, _ := strconv.Atoi(number)
			result = result + val
		}
	}

	return result
}