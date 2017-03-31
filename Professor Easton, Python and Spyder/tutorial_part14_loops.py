#Part 14 of a Python/Spyder Tutorial
#If Statements

#based on a tutorial at
#https://www.youtube.com/watch?v=w7sfSkQqdgw

#materials and further material available at:
    #https://www.youtube.com/watch?v=1bDSv18zGTU

#we pick up were we left off, part of the code for the last section is below

###########################
# If Statements in Python #
###########################


#The if statement loop in Python 2.7:

#if logical expression:
    #code block
#elif logical expression:                # Optional, can be more than one
    #code block
#else:
    #code block                          # Optional

# In Excel
# =if(logical expression, value if true, value if false)          


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

len(CEOs)
#%%

#this takes a list above, and another list that you give
    #it will extract the values at those index numbers

def GetItems(InputList,IndexList):
     
    Out = [] #create an empty list 'Out'
    
    for Item in IndexList:
        Out.append(InputList[Item])
    
    return Out

#note: since 'Out' is a list, IndexList must be labeled as a list
    #the code: GetItems(CEOs, 1) won't work
    #instead you'll need: GetItems(CEOs, [1])
GetItems(CEOs,[1,3,15]) #gives your the 2nd, 4th, and 16th items in the list

#we can check our function like so
CEOs[1] #2nd item
CEOs[3] #4th item
CEOs[15] #16th item
#%%

#in the function above, we make no effort to check the inputs for either of the used lists
    #good code will check if its inputs are like the things that are required for the funciton to work
    #this code does the same as above, but with error messages if format are incorrect

def GetListItems(InputList,IndexList):
    
    if not isinstance(InputList,list): #isinstance() built in function
        print("Error: InputList is not a list! An empty list is returned.")
        return []
    
    if not isinstance(IndexList,list): #this happens if IndexList isn't a list
        if isinstance(IndexList,int): #if its just a single integer, then we convert the integer to a list
            tmp = IndexList
            IndexList = []
            IndexList.append(tmp)
        else:
            print("Error: IndexList is not a list! An empty list is returned.")
            return []
 
    Out = []
    
    n = len(InputList)

    for Item in IndexList:
        if isinstance(Item,int): #we're checking if value in IndexList is an integer
            if Item >= -n and Item < n: #checking if value in IndexList has an object in InputList
                Out.append(InputList[Item])
            else: #what happens if the object in IndexList doesn't have a value in InputList
                print("Warning: Index out of range! The value None is returned.")
                Out.append(None) #stores a 'none' in the position of the error
        else: #what happens if the object in IndexList is not an integer
            print("Warning: Index is not an integer! The value None is returned.")
            Out.append(None)
            

    return Out

GetListItems(CEOs,[1,3,15])

#%%


GetListItems(CEOs,"abc") #function detects that IndexList is not a list of integers

x = {}
x['a'] = 5
x['b'] = "abc"
type(x)
GetListItems(x,[1,3,15]) #function detects that 'x' is not a list ('x' is a dictionary)
GetListItems(CEOs,[1,3,200])
GetListItems(CEOs,[1,3,-10])
GetListItems(CEOs,[1,-201,-30])
GetListItems([],[1,3,15])
GetListItems(CEOs,15)
GetListItems(CEOs,[15])
