package main

import "fmt"

func main() {
	f, _ := GetSportsFactory("adidas")

	// f, _ := GetSportsFactory("nike")
	// just the above line is sufficient to get nike products, without changing any of the code following it.
	// This is the power of Abstract Factory pattern

	shoe := f.makeShoe()
	shirt := f.makeShirt()

	fmt.Printf("shoe logo: %s, shoe size: %d\n", shoe.getLogo(), shoe.getSize())
	fmt.Printf("shirt logo: %s, shirt size: %d\n", shirt.getLogo(), shirt.getSize())

}
