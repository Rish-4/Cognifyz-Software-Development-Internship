def right_triangle(a):
    print()
    for i in range(1,a+1):
        for j in range(i):
            print(i,end="")
        print()
    print()

def pyramid(a):
    print()
    for i in range(1,a+1):
        for j in range(a,i,-1):
            print(" ",end="")
        for j in range(i):
            print(i,end="")
        for j in range(i-1):
            print(i,end="")
        print()
    print()

while True:
    a = int(input("Enter number of rows: "))
    print("Type 1 for Pyramid pattern!")
    print("Type 2 for Right Triangle pattern!")
    print("Type 3 to exit!")
    choice = int(input())
    if choice == 1:
        pyramid(a)
    elif choice == 2:
        right_triangle(a)
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")