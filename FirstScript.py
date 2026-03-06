import random

count = int(input("Сколько чисел: "))
start = int(input("От: "))
end = int(input("До: "))

numbers = []
for i in range(count):
    random_number = random.randint(start, end)
    numbers.append(random_number)

print("Числа:", numbers)

average = sum(numbers) / len(numbers)
print("Среднее:", average)