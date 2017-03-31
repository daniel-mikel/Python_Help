#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:45:44 2017

@author: dan
"""

#this is part 3 of a tutorial from youtube
#https://www.youtube.com/watch?v=GT1UfkLIeZ4

###########
#Functions#
###########

#we are going to define a function
#the function will define y as the squared value of x
#we then tell python what to return after the function is finished
#there needs to be a blank line after the function(?)
def myfun(x):
    y = x**2
    return y

#now we run the function with a certain input
print(myfun(5))

#PROPERTY OF FUNCTION
#the variables inside of a function are local. Say we already had a variable x
x = 10

#and we had a function using a variable x
def myfun(x):
    y = x**2
    return y

print(myfun(5))

#it still returns the function for 5 and not 10!
#this is called SCOPE!
#there is a defined range in which they have (and don't have) meaning

#so the scope of variables in functions stays local to functions
#the scope of variables outside of functions stays outside of functions

#now we want to use variables defined outside of the function inside a function

z = 15
def myfun(x):
    y = x**2 + z
    return y

print(myfun(5))

#above, we told python to use what we defined for x in myfunction
#each time we run the function, we told python we will redifine x
#for z, there is no local definition
#so when python hits the variable z
    #it first checks to see if there is a local definition
    #if there isn't a local definition
    #python then will look for a globally defined value
    
#what if our function already had a definted z...
z = 15
def myfun(x):
    y = x**2 + z
    z = 27
    return y

print(myfun(5))

#we get an error because we set a local z after the global z was used

#we can tell Python that to use the global value in a function like so

z = 15
def myfun(x):
    global z
    y = x**2 + z
    z = 27
    return y

print(myfun(5))

#now when we ran the function, we didn't get the syntax error
#Python doesn't mind the unused local z, and the global z, we resolved it.
#the local z is still unused, to be clear

#now we have three variables, and we have a funciton that processes all of them
x = 1
y = 2
z = 3
     
def f(x,y,z):
    out = x**2 + y**2 + z**2
    return out

print("f =", f(x,y,z))

#what if we tell python to print the f(), but we forget one of the arguments
x = 1
y = 2
z = 3
     
def f(x,y,z):
    out = x**2 + y**2 + z**2
    return out

print("f =", f(x,y))

#python gives you an error!

#we can make arguments optional, by doing the following in the f() statement
x = 1
y = 2
z = 3
     
def f(x,y,z=0):
    out = x**2 + y**2 + z**2
    return out
print("f =", f(x,y,z))
print("f =", f(x,y))

#above, python will use a default value for a varaible, if value not give
#you could make all of the variables have default values if you want
x = 1
y = 2
z = 3
     
def f(x=0,y=0,z=0):
    out = x**2 + y**2 + z**2
    return out
print("f =", f(x,y,z))
print("f =", f(x,y))

#we can also switch up the variables, 
    #to show python which values to take when running the function
x = 1
y = 2
z = 3
     
def f(x=0,y=0,z=0):
    out = x**2 + y**2 + z**2
    return out
print("f =", f(x,y))
print("f =", f(x=x, y=y))
print("f =", f(x=y, y=z)) 
#the first print is normal
#the second print asserts that x is global x, and y is global y
#the third print asserts that x is global y, and y is global z    

                                   