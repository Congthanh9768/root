class Hinhchunhat(object):
    def __init__(self, l, w):
       self.dai = l
       self.rong = w

    def dt(self):
       return self.dai*self.rong
    
    def cv(self):
        return (self.dai + self.rong)/2

aHinhchunhat = Hinhchunhat(10,2)
print (aHinhchunhat.dt())
print (aHinhchunhat.cv())

