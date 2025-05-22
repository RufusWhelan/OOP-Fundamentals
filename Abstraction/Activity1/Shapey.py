from abc import ABC, abstractmethod
 
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass
	def volume(self):
		pass
	
class Circle(Shape):
	def __init__(self, radius: float):
		self.radius = radius
		
	def perimeter(self) -> float:
		return 2 * 3.14 * self.radius
	
	def area(self) -> float:
		return 3.14 * self.radius ** 2
	
	def volume(self) -> float:
		return (4/3) * 3.14 * self.radius ** 3
	
class Rectangle(Shape):
	def __init__(self, width: float, height: float, depth:float):
		self.width = width
		self.height = height
		self.depth = depth
		
	def perimeter(self) -> float:
		return 2 * (self.width + self.height)
	
	def area(self) -> float:
		return self.width * self.height
	def volume(self):
		return self.width * self.height * self.depth

class Square(Shape):
	def __init__(self, length):
		self.length = length
		
	def perimeter(self):
		return self.length * 4
	
	def area(self):
		return self.length ** 2
	
	def volume(self):
		return self.length ** 3