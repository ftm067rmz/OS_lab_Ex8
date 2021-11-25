class Complex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag
    
    def show(self):
        print(self.real ,'+ (' , self.imag ,'i )')

        
    def sum(self , other):
        res = Complex()
        res.real = self.real + other.real
        res.imag = self.imag + other.imag
        return res
    
    def sub(self , other):
        res = Complex()
        res.real = self.real - other.real
        res.imag = self.imag - other.imag
        return res

    def mul(self , other):
        res = Complex()
        res.real = (self.real * other.real) - (self.imag * other.imag)
        res.imag = (self.real * other.imag) + (self.imag * other.real)
        return res

print('please enter 2 number: \n')
r1 = int(input('Enter first real : '))
i1 = int(input('Enter first imaginary :'))

r2 = int(input('Enter second real : '))
i2 = int(input('Enter second imaginary : '))

a = Complex(r1 , i1)
b = Complex(r2 , i2)

A = a.sum(b)
print("sum is : " , end='')
A.show()

B = a.sub(b)
print("sub is : ", end='')
B.show()

C = a.mul(b)
print("mul is : ", end='')
C.show()
