number = input("Number:")
num_of_digit = len(number)
number = int(number)
digit = 0
total = 0

temp_number = number

while (temp_number > 0):
    
    digit = temp_number % 10
    
    total += digit ** num_of_digit
    
    temp_number //= 10
    

if (total == number):
    print(number,"is a armstrong number")
else:
    print(number,"not a armstrong number")






















