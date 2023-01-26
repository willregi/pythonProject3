# Regina Williams
# willregi
# 01/26/2023

num_1 = int(input("Please enter a positive integer: "))
print("The factors of", num_1, "are:")
for factor in range(2, num_1):
  if num_1 % factor == 0:
      print(factor)
