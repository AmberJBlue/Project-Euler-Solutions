package solutions

func sum_sq_diff (start, end int) int{ 
	var sumOfSq, sqOfSum int = 0, 0
	for i := start; i <= end; i++ {
		sumOfSq += i*i
		sqOfSum += i
	}

	result := ((sqOfSum*sqOfSum) - sumOfSq)
	return result

}

func SumSqDiff() int{
	var x, y int = 1, 100
	return sum_sq_diff(x, y)
}