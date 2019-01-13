class Fraction:
    tuso = 0
    mauso = 1
    def __init__(self,tuso,mauso):
        self.tuso = tuso
        self.mauso = mauso
        
    def __add__(self,other):
        tuso  = self.tuso*other.mauso + self.mauso*other.tuso
        mauso = self.mauso*other.mauso
        return Fraction(tuso,mauso)
    
    def __sub__(self,other):
        tuso  = self.tuso*other.mauso - self.mauso*other.tuso
        mauso = self.mauso*other.mauso
        return Fraction(tuso,mauso)
    
    def __mul__(self,other):
        tuso  = self.tuso*other.tuso
        mauso = self.mauso*other.mauso
        return Fraction(tuso,mauso)
    
    def GCD(self,a,b):
        while(b>0):
            r = a%b
            a=b
            b=r
        return a

    def __str__(self):
        a = self.GCD(self.tuso,self.mauso)
        self.tuso//=a
        self.mauso//=a
        print(self.tuso,"/",self.mauso)
        
a = Fraction(3,4)
b = Fraction(5,4)
print(a+b)
