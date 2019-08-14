package solutions

func PythagoreanTriple() int{
	sum := 1000
	var a , b, c int
	for a = 1; a < (sum + 1); a++ {
		for b =1; b < (sum+1); b++ {
			c = sum - a - b
			if (a*a) + (b*b) == (c*c){
				return (a*b*c)
			}
		}
	}
	
	return 0
}