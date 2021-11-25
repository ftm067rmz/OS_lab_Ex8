class Time:
    def __init__(self , h=0 , m=0 , s=0):
        self.hour = h
        self.minute = m
        self.second = s
        self.fix()

    def show(self):
        print(self.hour, ":" , self.minute, ":" , self.second)
    
    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        
        if self.hour >= 24:
            self.day = 1
        
        if self.second < 0:
            self.second =0

        if self.minute < 0:
            self.minute =0

    def sum(self , other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second
        result.fix()
        return result

    def sub(self , other):
        res = Time()
        res.hour = self.hour - other.hour
        res.minute = self.minute - other.minute
        res.second = self.second - other.second
        res.fix()
        return res
    
    def time_To_second(self):
        res = self.hour*3600 + self.minute*60 + self.second
        print("Time to seconds : " , res)

    def second_To_time(self , other):
        self.hour = int(other/3600)
        other = other % 3600
        self.minute = int(other/60)
        self.second = other % 60
        print ("Time in H,M,S is : " , self.hour , ":" , self.minute , ":" , self.second)
       
print('Please enter 2 time for sum & sub :')
h1=int(input('hour 1 : '))
m1=int(input('minute 1 : '))
s1=int(input('second 1 : '))
h2=int(input('hour 2 : '))
m2=int(input('minute 2 : '))
s2=int(input('second 2 : '))

t1 = Time(h1,m1,s1)
t2 = Time(h2,m2,s2)

a = t1.sum(t2)
print("sum is : " , end='')
a.show()

b = t1.sub(t2)
print("sub is : ", end='')
b.show()

time = input("Enter the time in 12 hours (hh:mm:ss) :  ")
strT = time.split(":")
t3 = Time(int(strT[0]) , int(strT[1]) , int(strT[2]))
t3.time_To_second()

time = int(input("Please enter the time in seconds :  " ))
t4 = Time()
t4.second_To_time(time)