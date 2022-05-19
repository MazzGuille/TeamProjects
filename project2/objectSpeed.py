import math

#Prompts
mass = float(input("Enter the mass of the object in kg.: "))

print()

gravity = float(input("Enter the acceleration of gravity in m/s^2, for earth is 9.8 and for Jupiter is 24.0: "))
#Ciclo WHILE para validar que el usuario ingrese un valor válido
while gravity != 9.8 and gravity != 24.0:
    gravity = float(input("You have entered an invalid number, please enter the acceleration of gravity in m/s^2, for earth is 9.8 and for Jupiter is 24.0: "))
    if gravity == 9.8 or gravity == 24.0:
        print("You have entered a valid gravity.")
        break

print()

time_taken = float(input("Enter the time taken in seconds: "))

print()

density = float(input("Enter the density of the object in kg/m^3. If the object is in the air the density is of 1.3, in water is of 1000: "))
#Ciclo WHILE para validar que el usuario ingrese un valor válido
while density != 1.3 and density != 1000:
    density = float(input("You have entered an invalid number, please enter the density of the object in kg/m^3. If the object is in the air the density is of 1.3, in water is of 1000: "))
    if density == 1.3 or density == 1000:
        print("You have entered a valid density.")
        break

print()

cross_sectional_area = float(input("Enter the cross-sectional area of the object in m^2: "))

print()

drag_constant = float(input("Enter the drag constant (0.5 for sphere, 1.1 for cylinder): "))
#Ciclo WHILE para validar que el usuario ingrese un valor válido
while drag_constant != 0.5 and drag_constant != 1.1 and drag_constant != 0.04:
    drag_constant = float(input("You have entered an invalid number, please enter the drag constant (0.5 for sphere, 1.1 for cylinder): "))
    if drag_constant == 0.5 or drag_constant == 1.1 or drag_constant == 0.04:
        print("You have entered a valid drag constant.")
        break
    
print()
print()

#VARIABLES

#Mass (in kg)
m = mass

#acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)
g = gravity

#time (in seconds)
t = time_taken

#density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)
p = density

#cross sectional area of projectile (in square meters)
A = cross_sectional_area

#drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)
C= drag_constant

c = (1/2) * p * A * C

#the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).
exp = 0

#he square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).
sqrt = 0


#results
print(f"The inner value of c is: {c:.3f}")
velocity = math.sqrt(m*g/c)*(1-math.exp((-math.sqrt(m*g*c)/m)*t))
print(F"The speed at 10 seconds is: {velocity:.3f} m/s")



a = 3.14*10**2
print(a)

#985.96
