print ("Single Quotes")
print ("Double Quotes")
print('single'+ 'Quote')
print('Single','Quote')
print("Single"+"Quote")
print("Single","Quote")
print("Single",'Quote')

b = ‘Quote’
print (‘Single %s’ %b) or print(“Single %s” %b)
a = “Single”
print (‘%a %a’ %(a, b) )

c = 5
print(c)
print('There are', c ,'apple in the fridge') or
print('There are %d' %c, 'apple in the fridge')

name = input ("Please enter your name")
print(name) # you will see the name you type in the console

a = 10
b = 20
x = a + b
print(a+b) or print(x)

a = [1,2,3]
b = [1,2,3]
print('a is equal to b:', a == b)

2**4
19%5
a = True
b = False

print(f"combine result of {a and b} is False")
a = [1,2,3]
b = [1,2,3]
c = b

print(a is b)
print(b is c)