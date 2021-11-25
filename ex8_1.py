from math import gcd 
from math import lcm

class fraction:
    def __init__(self,s1=0,s2=0,m1=None,m2=None):
        self.s1 = s1
        self.s2 = s2
        self.m1 = m1
        self.m2 = m2

    def Sum(self):
        if self.m1 == self.m2:
            self.soorat = self.s1 + self.s2
            self.makhraj = self.m1 + self.m2
        else:
            kmm = lcm(self.m1 , self.m2)
            zarib1 = kmm // self.m1
            zarib2 = kmm // self.m2

            self.soorat = self.s1*zarib1 + self.s2*zarib2    
            self.makhraj = kmm
        
        simp = gcd(self.soorat, self.makhraj)
        self.soorat = self.soorat // simp
        self.makhraj = self.makhraj //  simp

        print('Sum is : ' , self.soorat , '/' , self.makhraj)

    def Sub(self):
        if self.m1 == self.m2:
            if self.s1 > self.s2:
                self.soorat = self.s1 - self.s2
            else:
                self.soorat = self.s2 - self.s1
            
        else:
            kmm = lcm(self.m1 , self.m2)
            zarib1 = kmm // self.m1
            zarib2 = kmm // self.m2
            
            self.makhraj = kmm
            self.s1 = self.s1*zarib1 
            self.z2 = self.s2*zarib2  
            if self.s1 > self.s2:
                self.soorat = self.s1 - self.s2
            else:
                self.soorat = self.s2 - self.s1
        
        simp = gcd(self.soorat, self.makhraj)
        self.soorat = self.soorat // simp
        self.makhraj = self.makhraj //  simp
        print('Sub is : ' , self.soorat , '/',  self.makhraj)

    def Mul(self):
        self.soorat = self.s1 * self.s2
        self.makhraj = self.m1 * self.m2
        
        simp = gcd(self.soorat, self.makhraj)
        self.soorat = self.soorat // simp
        self.makhraj = self.makhraj //  simp
        print('Mul is : ' , self.soorat , '/' , self.makhraj)

    def Div(self):
        self.soorat = self.s1 * self.m2
        self.makhraj = self.m1 * self.s2
        
        simp = gcd(self.soorat, self.makhraj)
        self.soorat = self.soorat // simp
        self.makhraj = self.makhraj //  simp
        print('Div is : ' , self.soorat , '/' , self.makhraj)

    

print('Please enter two fractions:')
s1=int(input('soorat 1 : '))
m1=int(input('makhraj 1 : '))
s2=int(input('soorat 2 : '))
m2=int(input('makhraj 2 : '))

userInp = fraction(s1 , s2 , m1 , m2)
userInp.Sum()
userInp.Sub()
userInp.Mul()
userInp.Div()