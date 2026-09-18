numbers = [1, 2, 3, 4]

short_doubled_numbers = [
    number * 2
    for number in numbers
]

print(short_doubled_numbers)
large_numbers = []

for number in numbers:
    if number >= 3:
        large_numbers.append(number)

print(large_numbers)
short_large_numbers = [
    number
    for number in numbers
    if number >= 3
]

print(short_large_numbers)
priorities = ["low", "high", "low", "critical", "high"]

unique_priorities = set(priorities)

print(unique_priorities)
print(sorted(unique_priorities))
uppercase_priorities = {
    priority.upper()
    for priority in priorities
}

print(sorted(uppercase_priorities))
priority_lengths = {
    priority.upper(): len(priority)
    for priority in sorted(unique_priorities)
}

print(priority_lengths)