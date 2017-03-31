#Part 7 and 8 of a Python/Spyder Tutorial

#based on a tutorial at
#https://www.youtube.com/watch?annotation_id=annotation_1025620673&feature=iv&src_vid=B6GESczuTrY&v=G6U5fQ8Siwo
    #talking in meta about data and tables, no coding
#https://www.youtube.com/watch?v=JJPM7hI4fjE
    #the tutorial, the coding part

#the videos have been updated to reflect Python 3.x (?) 
    #it may be easier moving forward to go back to previous videos to 

#####################
#Features of Objects#
#####################

#Objects have three features
    #(1) Inheritance
    #(2) Methods
    #(3) Encapsolution

################
#Object Example#
################

#our product will have a certain structure, with data held inside of it

#Product Structure
    #SKU - the serial number
    #Product Name
    #Brand
    #Manufacture
    #As a list [width, depth, height, units]
    #Weight
    #Units

#objects are created in python using the 'class' statement
#the colon signals to python that there is a block of coding coming
class VGSM:
    SKU="DAR023"
    Name="VG Skim Milk"
    Brand="Very Good Brands"
    Manufacture="Georgia Dairy, inc."
    Dimensions=[8,8,10,"in"]
    Weight=2.2
    WtUnits="lbs"

#now we have an object, and we can reference it
VGSM.Manufacture #prints out the Manufacture
VGSM.Dimensions[1] #gives us the depth, which was inside of a list

               
#problem, VGSM only referes to the milk
#what we really want is a template for the data
#we really want to be able to automate this process


#and use it like this:    
    #CER12 = Product("CER012", "VG Corn Flakes", "Very Good Brands", "In House, Inc.", [8,3,10, "in", 3.0, "oz"])
    #LDet24 = Product("LD024", "VG Clean Socks", "Very Good Brands",. )    
    
#How you do it
    #underscores common for private data, creating a function
    #here the case is to differenciate btw. the f() arguments and the object class    

class Product:
    def __init__(self, sku,name, brand, manu, dims, wt, wtunit):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacture = manu
        self.Dimensions = dims
        self.Weight = wt
        self.WtUnits = wtunit
        
#now were going to put this through the function
Milk23 = Product("DAR023", "VG Skim Milk", "Very Good Brands", "Georgia Dairy, inc", [8,8,10,"in"], 2.2, "lbs")

#the function has created an object!
Milk23.Weight #check the weight of the milk    

#now that we have this function, we can use it to define any other type of product
Cer12 = Product("CER012", "VG Corn Flakes", "Very Good Brands", "House Products, inc.", [9,3,11,"in"], 18, "oz")    
Cer12.Dimensions

