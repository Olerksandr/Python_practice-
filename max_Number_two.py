Num = int(input("Будь яке число "))

Max_two_digit = 0
old_max = 0
max_digit = 0

while Num > 0:
    digit = Num % 10

    if digit > max_digit:
        old_max = max_digit
        max_digit = digit
        Max_two_digit = old_max

    elif digit > Max_two_digit:
        Max_two_digit = digit

    Num = Num // 10

print(f"{max_digit}")
print(f"{Max_two_digit}")
