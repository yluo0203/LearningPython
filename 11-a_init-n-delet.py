# Object / init & delet
class Car:
    state = "New"
    def __init__(self, brand):
        self.brand = brand
    def im(self):
        print ("My brand is "  + self.brand)
    def drive(self):
        print ("I'm driving", self.brand)
        self.state = "Used"
    def __del__(self):
        print ("You delete the object", self.brand)

BMW = Car("BMW")
BMW.im()
print ("State is", BMW.state)
BMW.drive()
print ("State is", BMW.state)
BMW = None


# Output:
# -My brand is BMW
# -State is New
# -I'm driving BMW
# -State is Used
# -You delete the object BMW