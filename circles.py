from math import pi

def circle_area(r):
    if type(r) not in [float, int]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The radius cannot be nagative.");
    return pi*(r**2)