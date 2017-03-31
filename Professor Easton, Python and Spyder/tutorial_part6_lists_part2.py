#Part 6 of a Python/Spyder Tutorial

#based on a tutorial at
#https://www.youtube.com/watch?v=Ghb4wMW0YX4&list=PLi0JA8iXJGFAaViSS3lFo1A4SM_tDjL9b&index=6

#Lists Part 2

#####################
#Properties of Lists#
#####################

#lists can contain as their element any type of object

def fn(x,y):
    out = 3*x**2 + 4*y**3
    return out

#this list contatins int, flaots, strings, functions, and other lists
x = [1, 2.36, "Dog", fn, [3, 6, 2, 9, "Anything"], list("Hello")]

#you can also make a list on multiple lines
x = [1, 2.36, "Dog", fn, 
     [3, 6, 2, 9, "Anything"], 
     list("Hello")]

#how can you reference these?
x[0]
x[1]
type(x[1]) #now we get the type of the 2nd element
x[2][1] #this gives us the 2nd element of the third element of the list
x[3] #refers to the function
x[4] #shows the whole list that you had inside of the list
 
#we can run a function nested inside of a list like so
x[3](2,3) 
 
#saw we forgot the list, we can view the whole thing like so
x

#say we want to capture a slice of the list in the 5th element of our list 'x'
x[4] #list we are targeting
x[4][2:5] #you can use a second index to refer to 

     #you can also have lists inside of lists inside of lists, etc.

####################
#Functions of Lists#
####################

#lets create a string
x = 'string'

#and some functions to manipulate our string
x.upper() #make everything upper case in the string
x.capitalize() #capitalize first element of the string

#now lets try some functions in a list
x = [4, 6.7, "a", 10, "an", "bat", 5.6, "and", 6, 8, "4.5", "cat"]
x #to check your list
type(x) #check the type

x.reverse() #now the elements are exactly in the reverse order that they were in
x

x.sort() #this doesn't work, might be because using python 3.x and video 2.x
 #sorted list of the elements in x

x.sort(reverse=True) #still breaks, probably for whatever reason as above does
x 
 #if this had worked it would display a sorted version of x that was reversed


      