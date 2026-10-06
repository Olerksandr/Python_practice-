Num = int(input("Number: "))

Original_num = Num
digit_sum = 0

Num = abs(Num)

while Num > 0:
    digit = Num % 10
    digit_sum += digit
    Num = Num // 10

max_sum = digit_sum
best_number = Original_num

for i in range(2):
    Num = int(input("Число: "))

    Original_num = Num
    digit_sum = 0

    Num = abs(Num)

    while Num > 0:
        digit = Num % 10
        digit_sum += digit
        Num = Num // 10

    if digit_sum > max_sum:
        max_sum = digit_sum
        best_number = Original_num

print(best_number)