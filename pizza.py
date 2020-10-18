#!/usr/bin/env python3
from math import pi
from sys import argv


p1_size = int(argv[1])
p1_price = int(argv[2])
p2_size = int(argv[3])
p2_price = int(argv[4])


def pizza(size, price):
    stats = {}
    radius = size / 2
    radius_squared = radius*radius
    area = radius_squared * pi
    stats['size'] = size
    stats['price'] = price
    stats['area'] = area
    stats['price_per_unit'] = price / area
    return stats


def compare(p1, p2):
    more_expensive, less_expensive = (p1, p2) if p1['price_per_unit'] > p2['price_per_unit'] else (p2, p1)
    ratio = more_expensive['price_per_unit'] / less_expensive['price_per_unit']
    print("Best deal")
    print(f"{less_expensive['size']} inch pizza for {less_expensive['price']}")
    print(f"Price per sq. inch {less_expensive['price_per_unit']}")
    print(f"{ratio} times more value by choosing this pizza")


p1 = pizza(p1_size, p1_price)
p2 = pizza(p2_size, p2_price)
compare(p1, p2)

