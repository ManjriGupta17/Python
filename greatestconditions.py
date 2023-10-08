num = int(input("Enter a Positive Number: "))

#checking whether it is divisible by 15
if num % 15 == 0:
    print("number is divisible by 15")
else:
    if num % 3 == 0 or num % 5 == 0:
        print("Number is not divisible by 15 but divisible by 3 or 5")
    else:
        print("number is either divisible by 3 or 5")
