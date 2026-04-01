numbers = list(map(int, input("Enter list of numbers: ").split()))

index = len(numbers) - 1

while index < len(numbers):
    print(numbers[index])
    index -= 1