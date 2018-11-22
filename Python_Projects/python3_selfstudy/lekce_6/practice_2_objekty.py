import math

class Point:
    name = ''
    z = -2

    def __init__(self, x, y=0):
        self.x = x
        self.y = y
    
    def add_point(self, other_point):
        self.x = self.x + other_point.x
        self.y = self.y + other_point.y

    def print_me(self):
        print("bod {2}: [{0};{1};{3}]".format(self.x,self.y, self.name, self.z))


    # def get_x(self):
    #    return self.x

    @property
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
#instance objektu typu point predepsany tridou point
point_1 = Point(2,3)
point_1.print_me()
point_2 = Point(4,2)
point_2.print_me()
point_1.add_point(point_2)
point_1.print_me()


class MujPoint(Point):
    def sub_point(self, other_point):
        self.x = self.x - other_point.x 
        self.y = self.y - other_point.y


point_3 = MujPoint(3,3)
point_3.name = "muj super point"
point_3.print_me()
point_3.sub_point(Point(1,1))
point_3.print_me()

print(point_3.distance_from_origin)



class Person:
    first_name = 'Jana'
    last_name = 'Fana'

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name_to_set):
        self.first_name = full_name_to_set.split()[0]
        self.last_name = full_name_to_set.split()[1]

    def print_me(self):
        print("F:{0} L:{1}".format(self.first_name, self.last_name))


ja = Person()
ja.print_me()
print(ja.full_name)

ja.full_name = "Sandra Novak"
ja.print_me()

class Ctverec:
    def __init__(self, strana):
         self.strana = strana

    @property
    def obsah(self):
        return self.strana**2

    @obsah.setter
    def obsah(self, obsah):
        self.strana = math.sqrt(obsah)

ctverec1 = Ctverec(5)

print(ctverec1.obsah)

ctverec1.obsah = 81
print(ctverec1.strana)
