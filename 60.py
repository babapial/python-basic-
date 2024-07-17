class ractangle :
    
    def set_dimensions(self, widht, height):
        self.width = widht
        self.height = height
    def area(self):
        return (self.height)*(self.width)
    def parimeter(self):
        return 2*(self.width)*(self.height)
    

ractangle1 = ractangle()
ractangle1.set_dimensions(6,2)
print("area",ractangle1.area())
print("parimeter",ractangle1.parimeter())
        
        