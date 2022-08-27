temp = '' 

initialValue = int(input("Enter the largest number initialy : "))
temp = initialValue

# while true -  below code
while True:
    number = input("Enter a number to check wheather it is  largest  or not : ")
   
   
    try:
        
        if number == "done" :  break
        number = int(number)

        if temp > number :
            print("Largest number is", + temp )
        elif temp < number :
            temp = number
            print("Largest number is", + temp) 
    except:
        print("Invalid input")
        continue
