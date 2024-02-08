class student:
    def __init__(self,n,p):
        self.name=n
        self.per=p
        
        #magic method
        
    def __gt__(self,other):
        if self.per > other.per:
            return True
        else:
            return False
        
s1 =student("yadnesh",100)
s2 =student("harsh",35)

if(s1>s2):
    print(f"{s1.name} has grater percentage compare to {s2.name}")
else:
    print(f"{s2.name} has grater percentage compare to {s1.name}")