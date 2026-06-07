age=18
height=5.6
complex_num=1+2j
b=input("base of triangle: ")
h=input("height of triangle: ")
print("area of triangle:",0.5*float(b)*float(h))
x=input("Enter a side of a triangle: ")
y=input("Enter another side of a triangle: ")
z=input("Enter the last side of a triangle: ")
primeter_of_triangle=float(x)+float(y)+float(z)
print("primeter of triangle:",primeter_of_triangle)
l=input("Enter length of rectangle: ")
w=input("Enter width of rectangle: ")
print("area of rectangle:",float(l)*float(w))
print("perimeter of rectangle:",2*(float(l)+float(w)))
pi=3.14
r=input("Enter radius of a circle: ")  
area_of_circle=pi*float(r)**2
circum_of_circle=2*pi*float(r)
print("area of circle:",area_of_circle)
print("circumference of circle:",circum_of_circle)

def calculate_slope(m, c):
    return m
def x_intercept(m, c):
    return -c / m
def y_intercept(m, c):
    return c
m = 2
c = -2
for x in range(-10,11):
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"The equation has a root at x = {x}")
py=len("python")
jargon=len("jargon")
print("Is 'on' found in both 'python' and 'jargon'? ", "on" in "python" and "on" in "jargon")