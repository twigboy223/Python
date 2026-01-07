print("this is my calculator its not very good have fun")
print("this is a product of julian.v")
import time
time.sleep(4)
addition = input("Do you want to add:         ")
if addition == 'yes':
    first = float(input("first: "))
    second = float(input("second: "))
    sum = first + second
    print("the sum is: " + str(sum))
    quit()
elif addition == 'no':
        subtract = input("do you want to subtract:    ")
        if subtract == 'yes':
            first = float(input("first: "))
            second = float(input("second: "))
            sum = first - second
            print("the sum is: " + str(sum))
            quit()
        elif subtract == 'no':
            multiply = input("do you want to multiply: ")
            if multiply == 'yes':
                first = float(input("first: "))
                second = float(input("second: "))
                sum = first * second 
                print("the sum is: " + str(sum))
                quit()
            elif multiply == 'no':
                divid = input("do you wan to divid: ")
                if divid == 'yes':
                    first = float(input("first: "))
                    second = float(input("second: "))
                    sum = first / second
                    print("the sum is: " + str(sum))
                    quit()
                elif divid == 'no':
                    squared = input("do you want to square: ")
                    if squared == 'yes':
                        first = float(input("first"))
                        sum = first * first
                        print("the sum is: " + str(sum))
                        quit()
                    elif squared == 'no':
                        print("i cant do square root")
                        time.sleep(2)
                        print("im to lazy code it")
                        

