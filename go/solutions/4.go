package solutions

import ( 
	"strconv"
	"sort"
)

func Palindigits() int{
	var matches []int
	
	for n := 100; n <= 999; n++ {
		for j := 100; j <= 999; j++ {
			product := n * j
			if strconv.Itoa(product) == reverse(strconv.Itoa(product)) {
				matches = append(matches, product)
			}
		}	
	}
	
	sort.Ints(matches)
	return matches[len(matches) - 1]
}

func reverse(s string) string {
  runes := []rune(s)
  for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
    runes[i], runes[j] = runes[j], runes[i]
  }
  return string(runes)
}