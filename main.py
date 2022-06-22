customers = {1234: 'ali', 2345: 'ahmed', 3456: 'safer', 4567: 'jhon', 5678: 'loly'}


def isexist(x):
    if (x in customers):
        print("hi agent")
        k = input("would you like to print your information ? ")
        if k == 'yes':
            customers[6] = 'ella'
            l = customers.get(x)
            print("hi agent \"%s\" glad to see you " % l)
        elif k == "no":
            print("thanks")
        else:
            print("please either enter yes or no")
    else:
        print("Access denied,")


result = int
while result != 'x':
    try:
        v = "enter your password :"
        m = v.capitalize()
        y = int(input(m))
        isexist(y)

    except:
        print("this is not integer\n")

    result = input("\nenter x to leave or press any number to con : ")
print("thanks for using the program")



