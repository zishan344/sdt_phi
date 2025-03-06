#  Pen class. create three object with different instance attribute

class Pen:
  origin='BD'

  def __init__(self,CompanyName,penColor):
    self.companyName = CompanyName
    self.penColor = penColor
  def __repr__(self):
    return f'companyOrigin {Pen.origin}, company Name {self.companyName}, Pen Color {self.penColor}.'
   
      

sadaPen = Pen('fresh','white',)
blackPen =Pen('matador','black',)
holodPen =Pen('Satlor','yellow',)

print(sadaPen)
