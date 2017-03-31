#Part 4 of a Python/Spyder tutorial
#https://www.youtube.com/watch?v=OKelK8-NGg8&t=29s

#########
#Strings#
#########

#create string
x = "abcdefghijklmnopqrstuvwxyz"
 
#now we can find the length of our created string
len(x)

#now we'll create another string
    #you can also use single quotes when defining strings
y = 'Hello'

#The + operator concatenates strings
x + y

#strings can be indexed and referenced
x[1]

    #this gives 'b', suggesting that 'a' is at position 0
    #indexing is used with square brackets []
    #circular brackets are for functions
    
#indexing begins at zero, and then goes up 
x[0]
x[1]
x[2]
x[25]
    #returns a, b, c, and d
    
#if you go too far, the reference will be out of range
x[26]
    #this will give an error as 'string index out of range'
    #x[25] is 'z', not x[26].

#you can use negative indicies
    #then they wrap around
x[-1]  #z
x[-2]  #y  

x[-26]  #a
x[-27]  #out of range

 #######
 #Slice#
 #######
 
 #allows you to reference a range of things
x[0:3]  #gives us 'abc'

#now we want the first 5 numbers
x[0:5]  #here it seems like we call the first 6 numbers
        #but python really goes takes all the numbers up to 1 minus the last
        #this gives us the first 5 entries in the string
        
#if we want everything up until 'f'
x[:5]

#if we want everything after 'e'
x[4:]

#data in python can be classified as mutable and immutable
#mutable data is data that can be changed
#immutable data is data that cannot be changed

#stings are immutable
#cannot change the entries in the string

#for example, we cannot make the 2nd entry in string x a c
x[1] = 'c' #TypeError: 'str' object does not support item assignment

#we can't change assignment in the string, but we can do some transpositions
x.upper()

#split
z = "This is a test!"
z
z.split()

############################
#Converting between Strings#
############################

#we can convert between strings, intigers, and floating points
    #can reference index in strings, but not in int or floats
    
str('45.789') #45.789 would be a float, but we turned it into a string

str('45.789')[2] #this references the period in the string

#but if we were to try to reference the index with the number as a float
float("45.789")[2] #we get an error

#can also convert strings to integers
int("123")
