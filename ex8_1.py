from math import gcd 
class fraction:
    def __init__(self,s1=0,s2=0,m1=None,m2=None):
        self.s1 = s1
        self.s2 = s2
        self.m1 = m1
        self.m2 = m2

    def simp(soorat , makhraj):
        simp = gcd(soorat, makhraj)
        soorat = soorat // simp
        makhraj = makhraj //  simp
        return (soorat , makhraj)

    def Sum(a):
        if a.m1 == a.m2:
            a.soorat = a.s1 + a.s2
            a.makhraj = a.m1 + a.m2
        else:
            if a.m1 > a.m2:
                smaller = a.m2
            else:
                smaller = a.m1

            for i in range(1 , smaller+1):
                if ((a.m1 % i == 0) and (a.m2 % i == 0)):
                    bmm =i
            
            kmm = (a.m1*a.m2) / bmm
            zarib1 = kmm // a.m1
            zarib2 = kmm // a.m2

            a.soorat = a.s1*zarib1 + a.s2*zarib2    
            a.makhraj = kmm
        
        
        print('Sum is : ' , a.soorat , '/' , a.makhraj)

    def Sub(a):
        if a.m1 == a.m2:
            if a.s1 > a.s2:
                a.soorat = a.s1 - a.s2
            else:
                a.soorat = a.s2 - a.s1
            
        else:
            if a.m1 > a.m2:
                smaller = a.m2
            else:
                smaller = a.m1

            for i in range(1 , smaller+1):
                if ((a.m1 % i == 0) and (a.m2 % i == 0)):
                    bmm =i
            
            kmm = (a.m1*a.m2) / bmm
            zarib1 = kmm // a.m1
            zarib2 = kmm // a.m2
  
            a.makhraj = kmm
            a.s1 = a.s1*zarib1 
            a.z2 = a.s2*zarib2  
            if a.s1 > a.s2:
                a.soorat = a.s1 - a.s2
            else:
                a.soorat = a.s2 - a.s1
        
        print('Sub is : ' , a.soorat , '/',  a.makhraj)

    def Mul(self):
        self.soorat = self.s1 * self.s2
        self.makhraj = self.m1 * self.m2
        print('Mul is : ' , self.soorat , '/' , self.makhraj)

    def Div(self):
        self.soorat = self.s1 * self.m2
        self.makhraj = self.m1 * self.s2
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