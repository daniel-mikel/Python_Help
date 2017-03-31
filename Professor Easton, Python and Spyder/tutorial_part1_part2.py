#this is being taken from a series of youtube videos at:
    #https://www.youtube.com/watch?v=J5GevIHNctM

##########
##PART 1##
##########

#definitely remember to name your files .py
    #otherwise you won't be able to execute commands from the editor!

print ("Hello, World!")

##########
##PART 2##
##########
    #https://www.youtube.com/watch?v=OPuDjdRjtyY
    
#python can do basic arithmetic like R
3+4

#flaoting numbers are made by adding a decimal point after them. 
#this is required sometimes for operations, Python may 
3/4 

#to be 0

#doing the operation thusly: 
3./4. 

#will give 0.75


#this may be unique to Python 2 and not to Python 3

#you can find the type of a number (or variable) by using the type() command
type(3)
type(3.)

###########
#Variables#
###########

#you can assing a variable by executing
a = 4

#you can reassign a variable freely and it will overwrite
a = 3.

#syntax matters, running the following command will give you an error
5 = a

#you can use the type() and print() functions with variables too
type(a)
print(a)

#this will also print the variable's value
a

#you can do arithmetic with variables too
a/4

#you can also do arithmetic with exclusevily variables
b = 4
c = 5

b/c

float(b)/c

###############
#math packages#
###############

#this will allow us to import different commands from the package "math"

import math

#now we can use a function ,like exp, by calling it like:
math.exp(2)     

#"math" also gives us access to some constants, like pi
math.pi     
     
#you can clear the consol screen with ctrl + L     

#we can also call funtions on stored constants
math.cos(math.pi)

#if you want to see all the functions that you have access to with a package
dir(math)

##########
#Logicals#
##########

#must have a capital first lettor or it will yield an error message
True
False

#Booleans!

#The or operator is simply typed "or"
#The "or" operator will return True if one of the things is True
True or False

#The "and" function will return False below
#"and" only returns True if both parts of it are True
True and False

#you can also use "not"
#below, >True or False< will yield "True" but "not" will flip it to "False"
not (True or False)     

#Can also do comparisons
#This asks if 3 is less than 4, will come back as True
3 < 4

#you can ask if 3 is equal to 4
3 == 4

#or test an expression
3 == 4 - 1

#see if 4 is less than  or equal to 3
4 <= 3 

#can also test not equal
3 != 3
4 != 3

#you can also use the isinstance() function, to test if your example is a type
isinstance(3, int)
isinstance(3., int)
                   
             
                                