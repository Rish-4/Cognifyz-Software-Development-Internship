def FahrenheitToCelcius(temp):
    return round((temp-32) * 5/9, 3)

def CelciusToFahrenheit(temp):
    return round((temp*9/5) +32, 3)


def menu():
    while 1:
        print("Choose an option:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Exit Menu")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            F = float(input("Enter temperature in Fahrenheit : "))
            C = FahrenheitToCelcius(F)
            print(F,"°F = ",C,"°C")
        elif choice == 2:
            C = float(input("Enter temperature in Celsius : "))
            F = CelciusToFahrenheit(C)
            print(C,"°C = ",F,"°F",)
        elif choice == 3:
            print("Exiting Program!!")
            break
        else:
            print("Invalid Choice!!!")


menu()
