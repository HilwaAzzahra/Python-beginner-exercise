# Name

name = input("What is your name : ")

age = int(input("How old are you : "))

print ('Your name is ' + name)
if (age > 0 and age <= 100):
    print ("You are" , age,'\n')

else :
    print ("Please input numbers and something that is higher than 0 and lesser than a hundred")


sumAge = ((2020 - age )+ 100)

print(name + " will be 100 year old in year" , sumAge )