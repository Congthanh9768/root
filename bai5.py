class InputoutString(object):
    def __init__(self):
        self.s =""

    def getString(self):
        self.s =  input("nhap chuoi : ")

    def printString(self):
        print(self.s.upper())

    def Split(self):
        print(self.s.split(","))

strO = InputoutString()
strO.getString()
strO.printString()
str0.Split()
