class Rectangle:
  def __init__(self, width=1, height=1):
    self.width = width
    self.height = height

  def __str__(self):
    squareRep = "Square(side=" + str(self.width) + ")"
    recRep = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    if (self.width == self.height):
      return squareRep
    else:
      return recRep

  def set_width(self, width):
    if (self.width == self.height):
      self.width = width
      self.height = self.width
    self.width = width

  def set_height(self, height):
    if (self.height == self.width):
      self.width = self.height
    self.height = height

  def get_area(self):
    area = self.height * self.width
    return area

  def get_perimeter(self):
    perimeter = (2 * self.width) + (2 * self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return diagonal

  def get_picture(self):
    if (self.width > 50) or (self.height > 50):
      return "Too big for picture."
    x = self.width
    y = self.height
    picture = ""
    a = 0
    b = 0
    while (a < y):
      while (b < x):
        picture+= "*"
        b += 1
      picture += "\n"
      a += 1
      b = 0
    return picture

  def get_amount_inside(self, otherObj):
    if (self.width < otherObj.width) or (self.height < otherObj.height):
      return 0
    outerW = self.width
    outerH = self.height
    objW = otherObj.width
    objH = otherObj.height
    amountInside = 0
    while (outerW >= objW):
      while (outerH >= objH):
        outerH -= objH
        amountInside += 1
      outerW -= objW
      outerH = self.height
    return amountInside



    
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
  def set_side(self, side):
    self.width = side
    self.height = side