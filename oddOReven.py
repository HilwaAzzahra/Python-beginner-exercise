""" Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
        Hint: how does an even / odd number react differently when divided by 2?

    Extras:
    
        If the number is a multiple of 4, print out a different message.
        Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, 
        tell that to the user. If not, print a different appropriate message."""

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
