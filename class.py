class second:
    def __init__(self,teach,subject):
        super().__init__()
        self.teacher = teach
        self.subject = subject

    def printer(self):
        print("name:%s\nsubject:%d" %(self.teacher,self.subject))

class first(second):
    def __init__(self,name,roll,teach,subject):
        super().__init__(teach,subject)
        self.name=name
        self.roll=roll

    def printer(self):
        print("name:%s\nroll:%d" %(self.name,self.roll))

std1 = first("Bibek",1,"Murari","Math")
std1.super().printer()