Num = int(input("Будь-яке ціле число? "))

Num = abs(Num)

max_digit = 0
count_digit = 0

while Num > 0:
    digit = Num % 10

    if digit > max_digit:
        max_digit = digit
        count_digit = 1

    elif digit == max_digit:
        count_digit += 1

    Num //= 10

print(f"Найбільша цифра: {max_digit}")
print(f"Кількість: {count_digit}")