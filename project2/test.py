drag_constant = float(input("Enter the drag constant (0.5 for sphere, 1.1 for cylinder): "))
while drag_constant != 0.5 and drag_constant != 1.1:
    drag_constant = float(input("You have entered an invalid number, please enter the drag constant (0.5 for sphere, 1.1 for cylinder): "))
    if drag_constant == 0.5 or drag_constant == 1.1:
        print("You have entered a valid drag constant.")
        break