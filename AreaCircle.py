pi = 3.14159

def calc_area(radius) :
    return radius * radius * pi

while True:
    radius = int(input("Please Enter a value for the radius: "))

    if radius < 1 :
        print("Invalid Input! Radius must be a positive value!")

    else :
        print(calc_area(radius))
        choice = input("Do you want to continue? (yes/no): ")

        if choice.lower() == 'yes' :
            continue

        else :
            print("Good Bye!!")
            break