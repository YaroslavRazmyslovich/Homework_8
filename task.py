from abc import ABC, abstractmethod

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point
   
    def length_line (self):
        x_1 = self.first_point.x
        x_2 = self.second_point.x
        y_1 = self.first_point.y
        y_2 = self.second_point.y
        return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
      
    @property
    def length (self):
        return self.length_line ()
            
    def info (self):
        return print (f'Длина линии с координатами {first_point.x, first_point.y} и {second_point.x, second_point.y} равна {line.length}')

class Shape ():
    @abstractmethod
    def area_s (self):
        pass 
    
    @abstractmethod
    def perimeter_s (self):
        pass 

class Square (Shape, Line):
    def __init__ (self):
        super().__init__ (first_point, second_point)
    
    def area_s (self):
        return line.length ** 2

    @property
    def area (self):
        return self.area_s ()
    
    def perimeter_s (self):
        return line.length * 4

    @property
    def perimeter (self):
        return self.perimeter_s () 
        
    def info (self):
        print (f'Квадрат со стороной {square.length} имеет площадь {square.area} и периметр {square.perimeter}')

class Cube(Square):
        
    def area_s (self):
        return 3 * line.length ** 2 
    
    @property
    def area (self):
        return self.area_s ()

    def perimeter_s (self):
        return line.length * 12
    
    @property
    def perimeter (self):
        return self.perimeter_s ()

    def volume_s (self):
        return line.length ** 3 
    
    @property
    def volume (self):
        return self.volume_s ()
       
    def info (self):
        print (f'Куб со стороной {cube.length} имеет площадь {cube.area}, периметр {cube.perimeter} и объем {cube.volume}')

class Rect (Shape):

    def __init__(self, line_a, line_b):
        self.line_a = line_a
        self.line_b = line_b

    def area_s (self):
        return line_a.length * line_b.length  
    
    @property
    def area (self):
        return self.area_s ()

    def perimeter_s (self):
        return line_a.length * 2 + line_b.length * 2
    
    @property
    def perimeter (self):
        return self.perimeter_s ()
    
    def info (self):
        print (f'Прямоугольник со сторонами {line_a.length} и {line_b.length} имеет площадь {rect.area} и периметр {rect.perimeter}')

        

first_point = Point (0, 3)
second_point = Point (4, 0)
line = Line (first_point, second_point)
print (f'длина линии = {line.length}')
line.info ()
square = Square ()
print (f'площадь квадрата = {square.area}')
print (f'периметр квадрата = {square.perimeter}')
square.info ()
cube = Cube ()
print (f'площадь куба = {cube.area}')
print (f'периметр куба = {cube.perimeter}')
print (f'объем куба = {cube.volume}')
cube.info ()
third_point = Point (0, 0)
line_a = Line (third_point, first_point)
line_b = Line (third_point, second_point)
rect = Rect (line_a, line_b)
print (f'площадь прямоугольника = {rect.area}')
print (f'периметр прямоугольника = {rect.perimeter}')
rect.info ()
