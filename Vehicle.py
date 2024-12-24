class vehicle:
    def __init__(self,name,max,mile):
        self.name=name
        self.max=max
        self.mile=mile
class bus(vehicle):
    pass
school=bus("School Volvo",180,12)
print("Vehicle name:",school.name,"Speed :",school.max,"Mileage : ",school.mile)