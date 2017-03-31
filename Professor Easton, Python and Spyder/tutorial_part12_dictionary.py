#Part 12 of a Python/Spyder Tutorial
#Objects and Dictonaries

#based on a tutorial at
#https://www.youtube.com/watch?v=FzzYUbSuOSU&feature=youtu.be

#materials and further material available at:
    #http://datasciencesource.com/PythonWithSpyderMaterials/

#this is part 3 of a tutorial on objects in python

#we pick up were we left off, part of the code for the last section is below

################
# Dictionaries #
################

#Key, Value pairs is an important concept in SQL
    #In Python this is called a Dictionary 




#%%

#setting up a dictionary
#curly brackets denote dictionary
#the colon ':' is used to seperate key and value pairs
#the comma is used to seperate lines
#the left side is specifing the SKU numbers, as a string
#the right side is specifying the product, aslo as a string
#both the keys and values here are both strings
    #this doesn't have to be the case
    #they can be anything
#keys are uniqe
    #the values don't have to be unique
#if you accidently make two identical keys one will overwrite the other
SKUDict = {
    "Milk23":"VG Skim Milk",
    "Milk24":"VG 1% Milk",
    "Milk25":"VG 2% Milk",
    "Milk26":"VG Whole Milk",
    "Cer12":"VG Corn Flakes",
    "Cer13":"VG Toasted Oats",
    "Cer14":"VG Toasted Rice"   
}

SKUDict #prints the dictionary

SKUDict["Cer12"] #use square brackets to reference items in the Dicitonary, like a list
       
SKUDict["Cer12"] = "VG Corn Flakes (test)" #allows you to assign values to change them
SKUDict["Cer12"] = "VG Corn Flakes" #now we change it back

#when you assign to a key that isn't in the dictionary, it just creates a new entry
SKUDict['Cer15'] = "VG Rice Flakes" #we can also assing additional keys and values 
       #keys have no order
           #this also means they can't be sorted
           #they would have to be turned into somthing at isn't a dictionary
           #then you could sort it
           #but it wouldn't be a dicitonary again...


#%%

# Create an empty dictionary use {} or dict()

SKUDict = {} #first way to create an empty dictionary
SKUDict = dict() #second way to create an empty dictionary

SKUDict["Milk23"] = "VG Skim Milk"
SKUDict["Milk24"] = "VG 1% Milk"
SKUDict["Milk25"] = "VG 2% Milk"
SKUDict["Milk26"] = "VG Whole Milk"
SKUDict["Cer12"] = "VG Corn Flakes"
SKUDict["Cer13"] = "VG Toasted Oats"
SKUDict["Cer14"] = "VG Toasted Rice"
SKUDict['Cer15'] = "VG Rice Flakes"

       
#(warning) if you run these, you may get a different order of returns        
SKUDict.keys() #gives you list of keys in the dictionary
SKUDict.values() #also a list, but the values of the dictionary

              
SKUDict.pop('Milk25') #removes the item from the dictionary
SKUDict.popitem() #similar to above, just returns an item from the dictionary and removes it
'Milk23' in SKUDict #test if key is in the list of keys
'Milk2' in SKUDict #above test will fail
dir(SKUDict)

#%%
#Copying the dictionary name does not copy the dictionary data!


TestDict = SKUDict
TestDict
SKUDict

SKUDict['Cer15'] = "Hello!" #create new key value in SKUDict
TestDict #shows up in TestDict!

#dictionary constructure!
TestDict = dict(SKUDict) #this creates TestDict as a copy of the data currently in SKUDict at the time of assignment
TestDict
SKUDict

SKUDict['Milk23'] = "Hello!" #create new value for key in SKUDict
SKUDict #new value in SKUDict
TestDict #new value in SKUDict stayed only in SKUDict

#%%

#this isn't working... 
#uncomment and delete next cell if you can get it to work

#from tutorial_part11_inheritance.py import MilkProduct, LaundryDetergentProduct

#%%
 
#this cell was added because the previous one was was broken
    #this is just last lectures code without comments and put in a single cell


class Product:
    
    Version = "Ver 3.4 Rev 6"
    
    def __init__(self,sku,name,brand,manu,dims,wt,wtunits):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacturer = manu
        self.Dimensions = dims
        self.Weight = wt           
        self.WtUnits = wtunits
    
    def Print(self):
        out = "\nName:\t\t"+self.Name+"\nSKU:\t\t"+self.SKU+"\n"+ \
            "Brand:\t\t"+self.Brand+"\nManufacturer:\t"+self.Manufacturer+"\n\n"+ \
            "Dimensions\n"+ \
            "\tWidth:\t"+str(self.Dimensions[0])+self.Dimensions[3]+"\n"+ \
            "\tDepth:\t"+str(self.Dimensions[1])+self.Dimensions[3]+"\n"+ \
            "\tHeight:\t"+str(self.Dimensions[2])+self.Dimensions[3]+"\n\n"+ \
            "\tWeight:\t"+str(self.Weight)+self.WtUnits+"\n"
        print(out)
    
    def SetPhone(self,PhoneNum):
    
        dgts="0123456789"
    
        BadFmt=False
        if type(PhoneNum)!=type("abc") or len(PhoneNum)!=12:
            BadFmt=True
        
        if PhoneNum[3]!="-" or PhoneNum[7]!="-":
            BadFmt=True
        
        if not ( PhoneNum[0] in dgts and PhoneNum[1] in dgts and \
                    PhoneNum[2] in dgts and PhoneNum[4] in dgts and \
                    PhoneNum[5] in dgts and PhoneNum[6] in dgts and\
                    PhoneNum[8] in dgts and PhoneNum[9] in dgts and \
                    PhoneNum[10] in dgts and PhoneNum[11] in dgts):
            BadFmt=True
        
        if BadFmt:
            print("Wrong phone number format. Use \"xxx-xxx-xxxx\"\n")
            return False
        
        self.__PhoneNumber = PhoneNum
        
        return True
    
    def GetPhone(self):
        return self.__PhoneNumber
    
    def PrintShelfVolume(self):
        volume = self.Dimensions[0]*self.Dimensions[1]*self.Dimensions[2]
        out = "Shelf Volume = " + str(volume) + " " + \
                self.Dimensions[3] + " cubed\n"
        print(out)
        return volume
    
    def FootprintArea(self):
        return self.Dimensions[0]*self.Dimensions[1]
    
class MilkProduct(Product):
    
    Category = "Dairy"
    Storage = "Refrigerated"
    
    def __init__(self,sku,name,brand=None,manu=None,dims=None,wt=None, \
        wtunits=None,vol=None,fatcat="Whole",expir=None,servsize=None, \
        numserve=None,cals=None,fatgrams=None,fatcals=None,phone=None):
        
        Product.__init__(self,sku,name,brand,manu,dims,wt,wtunits)
        
        self.Volume = vol
        self.FatCategory = fatcat
        self.ExpirationDate = expir
        self.ServingSize = servsize
        self.NumberServings = numserve
        self.Calories = cals
        self.FatGrams = fatgrams
        self.FatCalories = fatcals
        
        if phone!=None:
            self.SetPhone(phone)    
    
class LaundryDetergentProduct(Product):
    
    Category = "Laundry"

    def __init__(self,sku,name,brand=None,manu=None,dims=None,wt=None, \
        wtunits=None,numloads=None,sudslevel="Not HE",form="Powder", \
        scent=None,phone=None):
        
        Product.__init__(self,sku,name,brand,manu,dims,wt,wtunits)
        
        self.NumberLoads = numloads
        self.SudsingLevel = sudslevel
        self.PhysicalForm = form
        self.Scent = scent
        
        if phone!=None:
            self.SetPhone(phone)
    
    

#%%


#Another Dictionary
    #the keys are still strings
    #the data are values using the given classes
#now instead of SKUDict having strings as values (like the first cell in this lecture)
    #we now have objects as values 


SKUDict = {}

SKUDict["Milk23"] = MilkProduct("Milk23","VG Skim Milk","Very Good Brands", \
        "Georgia Dairy",[8,8,10,"in"],2.2,"lbs","1Gal","Skim","2015-09-27", \
        8,16,90,0,0,"305-735-4353")
        
SKUDict["Milk24"] = MilkProduct("Milk24","VG 1% Milk","Very Good Brands", \
        "Georgia Dairy",[8,8,10,"in"],2.2,"lbs","1Gal","1%","2015-09-27", \
        8,16,102,2.37,21,"305-735-4353")
        
SKUDict["Milk25"] = MilkProduct("Milk25","VG 2% Milk","Very Good Brands", \
    "Georgia Dairy",[8,8,10,"in"],2.2,"lbs","1Gal","2%","2015-09-27", \
    8,16,122,4.81,43,"305-735-4353")

SKUDict["Milk26"] = MilkProduct("Milk26","VG Whole Milk","Very Good Brands", \
    "Georgia Dairy",[8,8,10,"in"],2.2,"lbs","1Gal","Whole","2015-09-27", \
    8,16,146,7.93,71,"305-735-4353")
    
SKUDict["Det16"] = LaundryDetergentProduct("Det16","VG Laundry Detergent HE", \
        "Very Good Brands",dims=[9,3,11,"in"],wt=18,wtunits="oz", \
        numloads=72,sudslevel="HE",form="Liquid")

SKUDict["Det17"] = LaundryDetergentProduct("Det17","VG Laundry Detergent Regular", \
        "Very Good Brands",dims=[9,3,11,"in"],wt=18,wtunits="oz", \
        numloads=72,sudslevel="Not HE",form="Liquid")

SKUDict["Det18"] = LaundryDetergentProduct("Det18","VG Laundry Detergent Powder", \
        "Very Good Brands",dims=[9,3,11,"in"],wt=18,wtunits="oz", \
        numloads=72,sudslevel="Not HE",form="Powder")

#%%

SKUDict #we can see that all the items are in the dictionary

#We can also access the data as if they were seperate objects not part of a dictonary
SKUDict['Milk25'].FatCalories #gives you the value
SKUDict['Det16'].FatCalories #gives error because class doesn't hold that value

########################
# What We Accomplished #
########################

#we've built a dicitonary where the keys are strings as before
    #the values are objects that have classes