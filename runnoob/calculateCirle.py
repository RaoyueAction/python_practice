import cmath
def calculate_circle(radius):
    """
    Calculate the area and circumference of a circle given its radius.
    
    :param radius: The radius of the circle
    :return: A tuple containing the area and circumference of the circle
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = cmath.pi * (radius ** 2)
    circumference = 2 * cmath.pi * radius
    return area, circumference
# Example usage:
if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    area, circumference = calculate_circle(radius)
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
# The above code defines a function calculate_circle that calculates the area and circumference of a circle given its radius.
# It uses the cmath module to handle complex numbers, although in this case, it is not necessary since the radius is a real number.
    