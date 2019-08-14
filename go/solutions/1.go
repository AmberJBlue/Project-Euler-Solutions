package solutions 

func Mult3and5() int{
	return mult3and5(1000)
}

func mult3and5 (limit int) int{
	sum := 0;
	
	for i := 0; i < limit; i++ {
		if ( i % 3 == 0 || i % 5 == 0 ) {
			sum += i
		}
	}

	return sum
}