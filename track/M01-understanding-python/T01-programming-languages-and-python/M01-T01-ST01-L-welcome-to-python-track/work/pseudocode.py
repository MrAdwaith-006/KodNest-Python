# To print Hello World

#start
#print "hello world"
#end
print("Hello World")

# To find wheather number (n) is even or odd

#start
#read the value of n
#if n%2 == 0 then
#print "even"
#else
#print "odd"
#end
print("Enter a number")
n = int(input())
if n%2 == 0:
    print("Even")
else:
    print("Odd")

# To find the number is positive or negative or zero

#start 
#print "Enter a Number"
#read n
#if n>=0
#then print "positive"
#else if n<0
#then print "negative"
#else
#print "zero"
#end
n = 0
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

# To find the largest number among the 3 numbers a, b, c

#start
#print "Enter 3 numbers"
#read a,b,c
#if a>=b and a>=c
#then print a
#else if b>=a and b>=c
#then print b
#else
#print c
#end
print("Enter 3 numbers")
a = int(input())
b = int(input())
c = int(input())
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
