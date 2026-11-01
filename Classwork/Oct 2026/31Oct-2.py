# Python program to calculate the factorial of each element in a list

# Get the number of elements from the user
num_elements = int(input("Enter the number of elements you want to enter in the list: "))

# Collect elements into the list
numbers = []
for _ in range(num_elements):
    element = int(input("Enter the elements: "))
    numbers.append(element)

# Calculate the factorial for each element
factorials = []
for num in numbers:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    factorials.append(fact)

# Display the resulting list of factorials
print(factorials)
