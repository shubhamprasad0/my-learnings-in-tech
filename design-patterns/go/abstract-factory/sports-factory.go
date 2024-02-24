package main

import "fmt"

type ISportsFactory interface {
	makeShoe() IShoe
	makeShirt() IShirt
}

func GetSportsFactory(brand string) (ISportsFactory, error) {
	if brand == "adidas" {
		return &AdidasFactory{}, nil
	}
	if brand == "nike" {
		return &NikeFactory{}, nil
	}
	return nil, fmt.Errorf("invalid brand %s", brand)
}
