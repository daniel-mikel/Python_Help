#Part 13 of a Python/Spyder Tutorial
#For Loops

#based on a tutorial at
#https://www.youtube.com/watch?v=w7sfSkQqdgw

#materials and further material available at:
    #http://datasciencesource.com/PythonWithSpyderMaterials/

#we pick up were we left off, part of the code for the last section is below

########################################
# Looping Using the For Loop in Python #
########################################

#for loops relate to program flow control
    #being able to go through a block of code repeatedly is a very powerful tool

#The for loop in Python:

#for Variable in Iterable:
    #code line 1
    #code line 2
    #etc.

#Iterable - think of it as a collection of things which the for statement can step through
#we end a for statement with a blank line

#In some other languages:

#for(i=0;i<n;i++) {
    #code line 1
    #code line 2
    #etc.
#}


#%%
# The 200 highest paid CEOs in 2014, in order, highest to lowest.
# Source: http://www.equilar.com/publications/51-200-highest-paid-CEO-rankings-2015.html

CEOs = ["David M. Zaslav","Michael T. Fries","Mario J. Gabelli",
        "Satya Nadella","Nicholas Woodman","Gregory B. Maffei",
        "Lawrence J. Ellison","Steven M. Mollenkopf","David T. Hamamoto",
        "Leslie Moonves","Philippe P. Dauman","Robert A. Iger",
        "Joseph W. Brown Jr.","Marissa A. Mayer","Leonard S. Schleifer",
        "Joshua W. Sapan","Marc Benioff","Jeffrey M. Leiden",
        "Herve Hoppenot","Jeffrey L. Bewkes","Gary W. Loveman",
        "Eric J. Foss","Zachary Nelson","Martine Rothblatt",
        "William J. McMorrow","W. Nicholas Howley","Steve Ells",
        "Howard M. Lorber","Rex W. Tillerson","Brian C. Cornell",
        "Montgomery F. Moran","James Dimon","Jonathan Oringer",
        "Paul M. Rady","Brian L. Roberts","Craig A. Leavitt",
        "Lamberto Andreotti","Ari Bousbib","Ronald N. Tutor",
        "Stephen A. Wynn","Thomas B. Barker","Stephen P. MacMillan",
        "Wayne T. Smith","Larry J. Merlo","Robert J. Hugin",
        "Michael J. Saylor","John D. Wren","Brian Harris",
        "K. Rupert Murdoch","Laurence D. Fink","Leslie H. Wexner",
        "James L. Dolan","W. James McNerney, Jr","Carol Meyrowitz",
        "James P. Gorman","Peter Liguori","David M. Cote",
        "A. Jayson Adair","Brian D. Jellison","James M. Cracchiolo",
        "Kenneth I. Chenault","Lloyd C. Blankfein","Barry D. Zyskind",
        "Darren R. Huston","Howard Schultz","Kenneth C. Frazier",
        "Randall L. Stephenson","Leonard Bell","Peter M. Carlino",
        "Alex Gorsky","David J. Lesar","Margaret C. Whitman",
        "Richard D. Fairbank","Jay S. Fishman","Andrew N. Liveris",
        "Alan G. Lafley","William R. Berkley","John G. Stumpf",
        "Michael F. Neidorff","Paul C. Saville","Indra K. Nooyi",
        "C. Douglas McMillon","Phebe N. Novakovic","John C. Martin",
        "Jeffrey R. Immelt","John S. Watson","John J. Legere",
        "George A. Scangos","Alan B. Miller","Lowell C. McAdam",
        "Muhtar Kent","Ian C. Read","Virginia M. Rometty",
        "Paul A. Ricci","Stuart A. Miller","Shantanu Narayen",
        "Marillyn A. Hewson","Alan H. Auerbach","Ryan M. Lance",
        "Richard H. Anderson","Richard E. Muncrief","Marc N. Casper",
        "Ronald F. Clarke","Thomas F. Farrell, II","John R. Strangfeld",
        "Samuel R. Allen","Kevin M. Sheehan","Richard A. Gonzalez",
        "Miles S. Nadal","Paal Kibsgaard","Gregory D. Wasson",
        "Brad D. Smith","Hamid R. Moghadam","John T. Chambers",
        "Scott A. McGregor","Dave Schaeffer","Gary E. Dickerson",
        "Alex A. Molinaroli","Marc Holliday","Patricia A. Woertz",
        "Miles D. White","Thomas M. Rutledge","Glenn K. Murphy",
        "Irene B. Rosenfeld","Gregory E. Johnson","Mary T. Barra",
        "John D. Finnegan","Jeffrey Weiner","Martin L. Flanagan",
        "Greg C. Garland","Robert A. Walker","Douglas R. Oberhelman",
        "Mark T. Bertolini","Martin B. Anstice","Fabrizio Freda",
        "Mark Fields","Wesley G. Bush","John Richels",
        "Jay T. Flatley","Stephen J. Hemsley","Richard K. Templeton",
        "Arne M. Sorenson","James T. Prokopanko","Gregory J. Goff",
        "Lorenzo Delpani","David Simon","John J. Koraleski",
        "Richard J. Kramer","Laura J. Alber","Mark G. Parker",
        "Robert D. Lawler","Martin S. Craighead","Brian T. Moynihan",
        "Steven A. Kandarian","Michael L. Corbat","Brian D. Goldner",
        "Mikkel Svane","David M. Cordani","John B. Hess",
        "Daniel S. Glaser","Inge G. Thulin","Robert A. Niblock",
        "Frederick W. Smith, III","Paul L. Berns","Stephen P. Holmes",
        "Joseph L. Hooley","John J. Donahoe","Robert A. Bradway",
        "William P. Sullivan","Kent J. Thiry","Charles E. Bunch",
        "Michael S. Burke","Robert J. Willett","Klaus Kleinfeld",
        "David G. DeWalt","Joseph R. Swedish","Gary R. Heminger",
        "Ajay Banga","Trevor Fetter","Mario Longhi",
        "Ellen J. Kullman","Eric C. Wiseman","Ian M. Cook",
        "Thomas J. Wilson","G. Frederick Wilkinson","Hubert Joly",
        "George Paz","William A. Cooper","Michael I. Roth",
        "Jeff M. Fettig","Donald E. Washkewicz","Robert L. Parkinson, Jr.",
        "Howard W. Lutnick","James D. Taiclet, Jr.","Steven E. Simms",
        "Terry J. Lundgren","James J. Volker","Scott D. Sheffield",
        "John F. Lundgren","Christopher M. Crane"]


len(CEOs) #check length of the list to see if we got all (200)
#%%
        
CEOFirstNames = ["David","Michael","Mario",
            "Satya","Nicholas","Gregory",
            "Lawrence","Steven","David",
            "Leslie","Philippe","Robert",
            "Joseph","Marissa","Leonard",
            "Joshua","Marc","Jeffrey",
            "Herve","Jeffrey","Gary",
            "Eric","Zachary","Martine",
            "William","Nicholas","Steve",
            "Howard","Rex","Brian",
            "Montgomery","James","Jonathan",
            "Paul","Brian","Craig",
            "Lamberto","Ari","Ronald",
            "Stephen","Thomas","Stephen",
            "Wayne","Larry","Robert",
            "Michael","John","Brian",
            "Rupert","Laurence","Leslie",
            "James","James","Carol",
            "James","Peter","David",
            "Jayson","Brian","James",
            "Kenneth","Lloyd","Barry",
            "Darren","Howard","Kenneth",
            "Randall","Leonard","Peter",
            "Alex","David","Margaret",
            "Richard","Jay","Andrew",
            "Alan","William","John",
            "Michael","Paul","Indra",
            "Douglas","Phebe","John",
            "Jeffrey","John","John",
            "George","Alan","Lowell",
            "Muhtar","Ian","Virginia",
            "Paul","Stuart","Shantanu",
            "Marillyn","Alan","Ryan",
            "Richard","Richard","Marc",
            "Ronald","Thomas","John",
            "Samuel","Kevin","Richard",
            "Miles","Paal","Gregory",
            "Brad","Hamid","John",
            "Scott","Dave","Gary",
            "Alex","Marc","Patricia",
            "Miles","Thomas","Glenn",
            "Irene","Gregory","Mary",
            "John","Jeffrey","Martin",
            "Greg","Robert","Douglas",
            "Mark","Martin","Fabrizio",
            "Mark","Wesley","John",
            "Jay","Stephen","Richard",
            "Arne","James","Gregory",
            "Lorenzo","David","John",
            "Richard","Laura","Mark",
            "Robert","Martin","Brian",
            "Steven","Michael","Brian",
            "Mikkel","David","John",
            "Daniel","Inge","Robert",
            "Frederick","Paul","Stephen",
            "Joseph","John","Robert",
            "William","Kent","Charles",
            "Michael","Robert","Klaus",
            "David","Joseph","Gary",
            "Ajay","Trevor","Mario",
            "Ellen","Eric","Ian",
            "Thomas","Frederick","Hubert",
            "George","William","Michael",
            "Jeff","Donald","Robert",
            "Howard","James","Steven",
            "Terry","James","Scott",
            "John","Christopher"]

len(CEOFirstNames) #check lenth to see if we got them all
            
#%%
            
CEOLastNames = ["Zaslav","Fries","Gabelli",
                "Nadella","Woodman","Maffei",
                "Ellison","Mollenkopf","Hamamoto",
                "Moonves","Dauman","Iger",
                "Brown","Mayer","Schleifer",
                "Sapan","Benioff","Leiden",
                "Hoppenot","Bewkes","Loveman",
                "Foss","Nelson","Rothblatt",
                "McMorrow","Howley","Ells",
                "Lorber","Tillerson","Cornell",
                "Moran","Dimon","Oringer",
                "Rady","Roberts","Leavitt",
                "Andreotti","Bousbib","Tutor",
                "Wynn","Barker","MacMillan",
                "Smith","Merlo","Hugin",
                "Saylor","Wren","Harris",
                "Murdoch","Fink","Wexner",
                "Dolan","McNerney","Meyrowitz",
                "Gorman","Liguori","Cote",
                "Adair","Jellison","Cracchiolo",
                "Chenault","Blankfein","Zyskind",
                "Huston","Schultz","Frazier",
                "Stephenson","Bell","Carlino",
                "Gorsky","Lesar","Whitman",
                "Fairbank","Fishman","Liveris",
                "Lafley","Berkley","Stumpf",
                "Neidorff","Saville","Nooyi",
                "McMillon","Novakovic","Martin",
                "Immelt","Watson","Legere",
                "Scangos","Miller","McAdam",
                "Kent","Read","Rometty",
                "Ricci","Miller","Narayen",
                "Hewson","Auerbach","Lance",
                "Anderson","Muncrief","Casper",
                "Clarke","Farrell","Strangfeld",
                "Allen","Sheehan","Gonzalez",
                "Nadal","Kibsgaard","Wasson",
                "Smith","Moghadam","Chambers",
                "McGregor","Schaeffer","Dickerson",
                "Molinaroli","Holliday","Woertz",
                "White","Rutledge","Murphy",
                "Rosenfeld","Johnson","Barra",
                "Finnegan","Weiner","Flanagan",
                "Garland","Walker","Oberhelman",
                "Bertolini","Anstice","Freda",
                "Fields","Bush","Richels",
                "Flatley","Hemsley","Templeton",
                "Sorenson","Prokopanko","Goff",
                "Delpani","Simon","Koraleski",
                "Kramer","Alber","Parker",
                "Lawler","Craighead","Moynihan",
                "Kandarian","Corbat","Goldner",
                "Svane","Cordani","Hess",
                "Glaser","Thulin","Niblock",
                "Smith","Berns","Holmes",
                "Hooley","Donahoe","Bradway",
                "Sullivan","Thiry","Bunch",
                "Burke","Willett","Kleinfeld",
                "DeWalt","Swedish","Heminger",
                "Banga","Fetter","Longhi",
                "Kullman","Wiseman","Cook",
                "Wilson","Wilkinson","Joly",
                "Paz","Cooper","Roth",
                "Fettig","Washkewicz","Parkinson",
                "Lutnick","Taiclet","Simms",
                "Lundgren","Volker","Sheffield",
                "Lundgren","Crane",
                ]

len(CEOLastNames) #check length to see if we got them all

#%%

#REVIEW THIS SECTION IT IS IMPORTANT AND A LITTLE TRICKY!

######################
# working with lists #
######################

#we know how to slice lists
#we don't know how to set up an arbitrary list of items from a list
 

#we want a function that we can specify the list we want to  access 
    #and the list's items and return the value
    
#first argument of function is the input list, and the second is an index list
#we want to step through the items in the Index List 
    #save the corresponding items from the Index List 
    #that will contain the outputs
#we end the first line with a colon, indicating that there is a block of code about to follow

def GetItems(InputList,IndexList):
    
    Out = [] #defining empty list that will later contain the output values
    
    #now we want to step through the index list
    #Item seems to be specified arbitrarily
    #IndexList is a list of the items we'd like to return
    #We use Item to step through IndexList
    #We take our empty list Out and append current values in the Input List of the Index List which is stored in Items
    for Item in IndexList:
        Out.append(InputList[Item]) 
    
    return Out

GetItems(CEOs,[1,3,15])

#%%

#function to define the sample mean

def mean(Data): #Data is the argument for the list of values
    
    n = len(Data) #take the length of the list of Data and store it in 'n'
    
    #now we use a for loop 
    Ans = 0.0 #Ans for answer, initially set at 0.0
    for x in Data: #x steps through all the values in the Data list one at a time
        Ans += x #these values are accumulated into 'Ans'
        # '+=" means that you take the value on the left, add the value on the right, and then save it on the left
        #shorthand for 'Ans = Ans + x'
    
    Ans /= n #same thing as before, It will take the sum of Ans, divide it by the number of observations, and then store the answer in Ans
    return Ans
 
#%%
   
def sd(Data):
    
    Xbar = mean(Data)
    n = len(Data)
    
    Ans = 0.0
    for x in Data:
        Ans += (x-Xbar)**2 #each data value minus sample mean squared summation in Ans
    
    Ans /= (n-1) 
    Ans = Ans**0.5
    
    return Ans
#%%

#the range() funciton is different in Python 3.x than in the tutorial...

range(10) #creates a list of integers 0 to the final value minus one (might be different now?)
range(len(CEOs)) #does this for the list of the variable CEO
range(50,len(CEOs)) #starts at 50 and goes to 199(?)

#%%

#in the previous examples, we could just use a simple for loop and not create an index
    #now we will need step through multiple variables at the same time
    #now we use the for loop to step through an index as well


def cor(X,Y):
    
    Xbar = mean(X)
    Ybar = mean(Y)
    sdX = sd(X)
    sdY = sd(Y)
    
    Cov = 0.0
    for i in range(len(X)): #'i' represents an index, must step through a collection of the range of the number of observations
        Cov += (X[i]-Xbar)*(Y[i]-Ybar) #for the 'i'th value in the X list minus the X mean times...
    
    Cov /= (len(X)-1)
    
    Ans = Cov/(sdX*sdY)
    return Ans
    

#%%

len("abcd") #outputs the length of the string (in number of charecters) 


#%%
#the test of this cell (script) 
    #is having a long first name makes you more likely to have a long last name?

# map(function,list) - applies a function to all of the items in a list

#found the solution:
    #Before Python 3, map() returned a list, not an iterator. 
        #So your example would work in Python 2.7
    #list() creates a new list by iterating over its argument. 
         #list() is NOT JUST a type conversion from say tuple to list. 
         #So list(list((1,2))) returns [1,2]. ) 
        #So list(map(...)) is backwards compatible with Python 2.7
     
#works, I added list() argument to make map() work with Python 3.0
list(map(len, CEOFirstNames))

#works, inserted list() arguments to make map() work with Python 3.0
cor(list(map(len,CEOFirstNames)),(list(map(len,CEOLastNames))))    

