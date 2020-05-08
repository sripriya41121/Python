p1=int(input("Enter p1: "))
p2=int(input("Enter p2: "))


try:
    print("Running!")
    print(p1*p2)
    akku=int(input("Enter your Choice: "))
    print(akku)

except ValueError as e:
    print("Error Occured!",e)

except Exception as e:
    print("Hey, try again!")

finally:
    print("Terminated!")
    print("Hip Hip Hurrey!") 
    #added for subbranch1
