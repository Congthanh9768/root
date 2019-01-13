import math


class Circle2D(object):

    def __init__(self, x = 0, y = 0, r = 0):
        """Creates a circle with specified x, y, and radius."""
        self._x = x
        self._y = y
        self._r = r

    def __str__(self):
        """Returns the string representation."""
        return  ("Circle with center" + "(" + "%0.0f" % (self._x) + ", "
        + "%0.0f" % (self._y) + ")" + "and radius " + "%0.0f" % (self._r))

    def getX(self):
        """Returns the X value."""
        return self._x

    def getY(self):
        """Returns the Y value."""
        return self._y

    def getRadius(self):
        """Returns the value of the radius"""
        return self._r

    def setRadius(self):
        """Sets a new value for the radius."""
        pass

    def getArea(self):
        """Returns the area of the circle."""
        return math.pi * self._r * self._r

    def getPerimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self._r

    def containsPoint(x,y):
        """Returns True if the specified point (x, y) is inside this circle."""
        if (self._x)^2 + (self._y)^2 <= (self._r)^2:
            return True
        else:
            return False

    def contains(circle2D):
        pass

    def overlaps(circle2D):
        pass

    def main():
        x = float(input("Enter x coordinate for the center of circle 1: "))
        y = float(input("Enter y coordinate for the center of circle 1: "))
        r = float(input("Enter the radius of circle 1: "))
        c1 = Circle2D(x, y, r)
        print(c1)

        x = float(input("\nEnter x coordinate for the center of circle 2: "))
        y = float(input("Enter y coordinate for the center of circle 2: "))
        r = float(input("Enter the radius of circle 2: "))
        c2 = Circle2D(x, y, r)
        print(c2)

        #Test the getArea() and getPerimeter() methods
        print("\nArea of a %s is %0.2f" % (c1, c1.getArea()))
        print("Perimeter of a %s is %0.2f" % (c1, c1.getPerimeter()))

        print("\nArea of a %s is %0.2f" % (c2, c2.getArea()))
        print("Perimeter of a %s is %0.2f" % (c2, c2.getPerimeter()))
        #-------------------

        #Test containsPoint() method
        print("\nResult of c1.containsPoint(c2.getX( ), c2.getY( )) is",
              c1.containsPoint(c2.getX( ), c2.getY( )))

        #Test contains() method
        if c1.contains(c2):
            print("\n%s contains %s" % (c1, c2))
        else: 
            print("\n%s does not contain %s" % (c1, c2))

        print("\nResult of c2.contains(c1) is",
               c2.contains(c1))
        #----------------

        #Test overlap() method
        if c1.overlaps(c2):
            print("\n%s overlaps with %s" % (c1,c2))
        else: 
            print("\n%s does not overlap with %s" % (c1,c2))
        #--------------

        #Test overloaded in operator                                     
        print("\nResult of c2 in c1 is", c2 in c1)                     

        #Testing overloaded comparison and equality operators
        #Something similar to this
        print("\nTesting overloaded comparison operators...")
        print("c1 == c2?", c1 == c2)
        print("c1 != c2?", c1 != c2)
        print("c1 < c2?", c1 < c2)
        print("c1 <= c2?", c1 <= c2)
        print("c1 > c2?", c1 > c2)
        print("c1 >= c2?", c1 >= c2)
        print('c1 == "Hello"?', c1 == "Hello")
        print('c1 != "Hello"?', c1 != "Hello")

    main()
