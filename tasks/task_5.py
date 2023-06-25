weight_in_grams: int = 350000

weight_in_kilograms: float = weight_in_grams / 1E3
weight_in_tons: float = weight_in_grams / 1000000

# weight_in_tons: float = weight_in_grams / 1E6
# weight_in_tons: float = weight_in_grams / 1_000_000
# weight_in_tons: float = weight_in_kilograms / 1000

print('Вес в килограммах:', weight_in_kilograms)
print('Вес в тоннах:', weight_in_tons)
