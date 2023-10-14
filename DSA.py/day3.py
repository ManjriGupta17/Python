class Test:
     def __init__(self,a,b):
         self.a=a
         self.b=b
    def f1(self):
        pass
    @staticmethod
t1=Test(3,4)
t2=Test(5,6)
print(t1.a,t1.b)
print(t2.a,t2.b)    
