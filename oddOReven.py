num = int(input ("Insert any odd or even numbers : "))
check = int(input("Insert number to divide by : "))
dividedNum = num / check


if num % 4 == 0:
    print("The number you put are the multiple of four")

elif num % 2 == 0:
    print("The number you put is even")

else:
    print("The number you put is odd")
    

if dividedNum % 2 == 0 :
    print("The sum numbers you divided are even : ",dividedNum)

else:
    print("The sum numbers you divided are odd : ",dividedNum)