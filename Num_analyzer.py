Number = int(input("Введіть ціле число "))
Original_num = Number

Number = abs(Number)

digit_count = 0
max_digit = 0
digit_sum = 0

if Original_num > 0:
    print("Число додатне")

elif Original_num == 0:
    print("Це 0")
else:
    print("Число відємне") 
if Original_num % 2 ==0:
    print("Число парне")
else:
    print("Число не парне")

if Number ==0:
    digit_count= 1
    

while Number > 0 :
    digit = Number % 10 
    digit_sum = digit_sum + digit
    digit_count = digit_count + 1  

    if digit > max_digit:
        max_digit = digit
    Number = Number //10 

    
print(digit_sum)
print(digit_count)
print(max_digit)
  