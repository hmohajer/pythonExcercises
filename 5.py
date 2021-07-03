# Exercise: Create a version of the Rectangle class that is safe by assuring that both width and height are positive values (how you do that is up to you). Expand it with methods that calculate its surface area and its circumference. Also, provide a method that returns the bottom-right corner of the rectangle as a Point. Finally, create a method that gets a second Rectangle object as a parameter, and returns the overlapping area of the two rectangles as a new Rectangle object (the last one is much harder than the other ones).
from datetime import datetime
#~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Rectangle():
    def __init__(self, x, y, width, height):
        self.width = abs(width)
        self.height = abs(height)
        a = x
        b = y
        if width < 0:
            a = x + width
        if height < 0:
            b = y + height
        self.start_point = (a, b)
        # self.r_points = [self.start_point[0],self.start_point[0]+self.width, self.start_point[1],self.start_point[1]+self.height]
        self.r_points = [a, a+self.width, b, b+self.height]

    def surface(self):
        return self.width * self.height

    def circumference(self):
        return (self.width + self.height) * 2

    def bottom_right(self):
        return (self.start_point[0]+self.width , self.start_point[1])

    def is_between(self, point, a, b):
        if point > a and point < b:
            return True
        else:
            return False

    def overlap(self, rctg):
        r1 = self.r_points.copy()
        r2 = rctg.r_points.copy()
        p = []
        for i in range(4):
            if i < 2:
                j = 0
            else:
                j = 2
            if(self.is_between(r1[i], r2[j], r2[j+1])):
                p.append(r1[i])
            elif (self.is_between(r2[i], r1[j], r1[j+1])):
                p.append(r2[i])
        
        return Rectangle(p[0],p[2], p[1]-p[0], p[3]-p[2])
        # return (p)


        # if(self.is_between(r2[0], r2[1], r1[0])):
        #     a = r1[0]
        # elif (self.is_between(r1[0], r1[1], r2[0])):
        #     a = r2[0]

        # if(self.is_between(r2[0], r2[1], r1[1])):
        #     b = r1[1]
        # elif (self.is_between(r1[0], r1[1], r2[1])):
        #     b = r2[1]

        # if(self.is_between(r2[2], r2[3], r1[2])):
        #     c = r1[2]
        # elif (self.is_between(r1[2], r1[3], r2[2])):
        #     c = r2[2]

        # if(self.is_between(r2[2], r2[3], r1[3])):
        #     d = r1[3]
        # elif (self.is_between(r1[2], r1[3], r2[3])):
        #     d = r2[3]
        # return (a, b, c, d)

rc = Rectangle(1,1,2,2)
rc2 = Rectangle(0,2,4, 3)
# rc2 = Rectangle(0,0,4, 5)
# rc2 = Rectangle(2,2,4, 5)
rc3 = rc.overlap(rc2)
print(rc3.r_points)
# print(rc.circumference())
# print(rc.bottom_right())
#~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise: A student has the last name, a first name, a date of birth (either a year, month, and day, or a datetime object if you took the liberty of studying the datetime module already), and an administration number. A course has a name and a number. Students can enroll in courses. Create a class Student and a class Course. Create several students and several courses. Enroll each student in some of the courses. Display a list of students, showing their number, first name, last name, and age, and per student which courses he or she is enrolled in.
class student():
    def __init__(self, first_name, last_name, birthdate = datetime(1995, 7, 6)):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = birthdate

#~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Square(Rectangle):
    def __init__(self, x, y, w):
        super().__init__(x, y, w, w)

sq = Square(1, 2, 3)
print(sq.r_points)
#~~4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise: Rectangle and a Square can be considered shapes. There are, of course, different kinds of shapes which are defined differently, but share with rectangles and squares that they have an area and circumference. Define an interface class Shape, of which Rectangle and Square are sub(sub)classes. Also define a class Circle that you derive from Shape.


