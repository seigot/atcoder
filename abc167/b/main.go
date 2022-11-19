package main

import (
	"fmt"
	"os"
)

func main() {
	var A, B, C, K int
	fmt.Scan(&A, &B, &C, &K)
	//fmt.Println(A, B, C, K)

	remain := K
	sum := 0

	// A
	remain = remain - A
	if remain < 0 {
		fmt.Println(K*1)
		os.Exit(0)
	} else {
		sum += A * 1
	}

	// B 
	remain = remain - B
	if remain < 0 {
		fmt.Println(sum)
		os.Exit(0)
	} else {
		sum += B * 0
	}

	// C
	fmt.Println(sum + (remain * -1))
}
