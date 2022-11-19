package main

import (
	"fmt"
)

func main() {
	var n, k, d, in int
	fmt.Scan(&n, &k)
	a := make([]int, n)

	for i := 0; i < k; i++ {
		fmt.Scan(&d)
		for j := 0; j < d; j++ {
			fmt.Scan(&in)
			a[in-1]++
		}
	}
	ret := 0

	for i := 0; i < n; i++ {
		if a[i] == 0 {
			ret++
		}
	}
	fmt.Println(ret)
}

// https://atcoder.jp/contests/abc166/submissions/25475932
