numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

min_val = numbers[0]
max_val = numbers[0]
total = 0

for num in numbers:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    total += num

average = total / len(numbers)

print("Min:", min_val)
print("Max:", max_val)
print("Average:", average)
