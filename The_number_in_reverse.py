Num = int(input("Число "))
Original_num = Num
reversed_num = 0
while Num >0:
    digit = Num %10
    reversed_num = reversed_num *10 + digit
    Num //= 10 

if Original_num == reversed_num:
    print("Паліном")
else:
    print("Непаліном")

print(reversed_num)