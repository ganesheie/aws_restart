pi = 22/7

def calculate_circle_area(radius):
    return pi * radius ** 2
def calculate_circle_circumference(radius):
    return pi * 2 * radius
def descripton():
   print ("This code would calculate the area and circumference of a circle with radius {}".format(r) )

while True:
    try:
        r = int(input("Enter the radius of the circle: "))
        if r > 0:
            descripton()
            print("The area of the circle is:", calculate_circle_area(r), " & circumference is " , calculate_circle_circumference(r) )
            break
        else:
            print("Radius must be positive. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
