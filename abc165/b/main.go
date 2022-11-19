package main

import (
	"fmt"
	"os"
)

func main() {
	var X int
	fmt.Scan(&X)

	var val int
	val = 100
	cnt := 0
	for { 
		if val >= X {
			fmt.Println(cnt)
			os.Exit(0)
		}
		val += int(val/100)
		cnt += 1
	}
}
