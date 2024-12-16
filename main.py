print("Welcom to table generator".center(80))

game = True
def table():
    global game
    num = int(input("Enter your numbe: "))
    range_num = int(input("Enter the range upto 10 or 20: "))
    
    for i in range(range_num + 1):
        print(f"{num} * {i} = {num*i}")
    
    ask = input("Do you want to continue? Type 'y' or 'n' ")
    if ask == 'n':
        game = False
        print("Thank You")
    elif ask == 'y':
        table()
    else:
        game = False
        print("Invalid Typooo")
generator = input("Enter 's' to start or 'e' to exist: ")



if generator == 's':
    table()
elif generator == 'e':
    game = False
    print("Thank You".center(30))
else:
    game = False
    print("Invalid Typo".center(30))