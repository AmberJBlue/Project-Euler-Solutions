package solutions

import (
	"math"
)

func NumberLetterCounts() int{
	var result int
	for i := 0; i < 1001; i++ {
		result += len(getNumberString(i))
	}

	return result
}

func getNumberString(i int) string{
	var concatStr string
	integers := [21]string{"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
	multsOfTen := [10]string{"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}

		if (0 <= i && i < 20) {
			concatStr += integers[i]
			return concatStr
		} else if 20 <= i && i < 100 {
			concatStr += multsOfTen[int(math.Floor(float64(i/10)))]
			if i % 10 != 0 {
				concatStr += integers[(i % 10)]
			}
			return concatStr
		} else if 100 <= i && i < 1000 {
			concatStr += integers[int(math.Floor(float64(i/100)))] + "hundred" 
			if (i % 100 != 0) {
				remainder := i % 100
				concatStr += ("and" + getNumberString(remainder))
			}
			return concatStr
		} else if 1000 <= i && i < 100000 {
			concatStr += getNumberString(int(math.Floor(float64(i/1000)))) + "thousand"
			if(i % 1000 != 0) {
				getNumberString(i % 1000)
			}
			return concatStr
		}
	return concatStr
}