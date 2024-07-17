class student:
    def set_name(sel,name):
        sel.name = name
    def get_name(sel):
        return sel.name
    
student1 = student()
student1.set_name("pial hasan")
print(student1.get_name())

student2 = student() 
student2.set_name("piyas hasan")
print(student2.get_name())
    