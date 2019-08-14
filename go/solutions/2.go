package solutions 

func FibSeq() int {
	result := 0
	current := 1
	next := 2
	
	for current <= 4000000 {
		if current % 2 == 0 {
			result += current
		}
		current, next = next, current + next
	}
	return result
}