#Part 5 of a Python/Spyder Tutorial

#based on a tutorial at
#https://www.youtube.com/watch?v=1qeKsuhww8g&index=5&list=PLi0JA8iXJGFAaViSS3lFo1A4SM_tDjL9b

#######
#Lists#
#######

#Vector is a column of like things
    #essentially the same thing as in R
    #need to be the same class
    
#Matrix
    #has a number of rows and columns
    #generally referred to in rows by columns

#List
    #a lot like a vector
    #the entries don't have to be the same type
    #can include functions
    
# Vectors and Matrix in Python
    #unless you use additional software, Python doesn't use Vectors or Matrix
    #Does use lists
    
#how to create a list
x = ["Dog", 3, 7.123, "House"] 
    #lists can include all types of items, even functions!
    #the square brackets [] indicate to python that this is a list
    
################
#Indexing Lists#
################

#done exactly in the same way as strings
x[0]
x[3]
x[-2]


#slicing works the same way as strings too
x[1:3]
x[2:]
x[:4]

#####################
#Properties of Lists#
#####################

#lists can have an unexpected behavior
y = x   #now y will give you exactly what you get with x
y

#now lets reassign one of the elements of x
x[2] = "Hello"
 
#now we see what our list's values are:
x
y
     #so y isn't set as what x is at the time you run the code
     #y is stored AS x 
     #need to be careful when doing assignments
 
#what if we did want a copy of this list
    #not to always equalling x, but as a snapshot of x at the time
y = list(x)

#now if we do a reassignment
x[2] = "Goodbye"

x   #has the new value "Goodbye"
y   #has the new value "Hello"

##########################
#More Properties of Lists#
##########################

#when indexing, we have to use square brackets
    #if we use circular brackets then Python will think we calling a function
    
#if we try call on values of a function that are out of range
x[3]   #is in range
x[4]   #is out of range

###################
#Strings vs. Lists# 
###################

#we have seen that we can change the various items in a list at will
    #this means that lists are MUTABLE
    
    #in contrast, strings are immutable
s = "Hello" #we have the string "Hello"
s[1]   #we can call any part of the string to look at it
s[1] = 'b'   #but we CAN'T change the items inside the string 
 #Strings do not support assignment
 #Strings are immutable
 
#but we can turn a string into a list
list(s)

#you'd have to store it though
h = list(s)
h 
h[1] = 'b'   #now we can do assignment

#however, we cannot move from a list to a string
str(list(s))   #still a list

   
