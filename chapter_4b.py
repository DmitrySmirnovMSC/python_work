#for value in range(1, 11):
#  print(f"Перед вами число {value}.")

#numbers = list(range(2,23,2))
#print(numbers)

# squares = []

# for value in range(1, 11):
#  squares.append(value/2)

# print(squares)

# numbers = [12, 15, 4, 9, 27, 22, 16, 3, 44, 2, 51, 27, 52]
# print(f"{min(numbers)} is minimal value")
# print(f"{max(numbers)} is maximum vulue")
# print(f"{sum(numbers)} is sum of all values")

squares = [value**2 for value in range(1,11)]
print(squares)