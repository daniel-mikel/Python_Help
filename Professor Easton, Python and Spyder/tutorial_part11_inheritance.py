#Part 11 of a Python/Spyder Tutorial
#Objects and Inheritance

#based on a tutorial at
#https://www.youtube.com/watch?v=ueDdQ8sx6SM

#materials and further material available at:
    #http://datasciencesource.com/PythonWithSpyderMaterials/

#this is part 3 of a tutorial on objects in python

#we pick up were we left off, part of the code for the last section is below

###############
# Inheritance #
###############

#you can define objects that depend on other classes 
    #inherit their properties
    
#####################################
# Back to the grocery store example #
#####################################

#now we want a special class for milk products


#%% Define the Product class

class Product:
    
    Version = "Ver 3.4 Rev 6"
    
    def __init__(self,sku,name,brand,manu,dims,wt,wtunits):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacturer = manu
        self.Dimensions = dims
        self.Weight = wt           # Should have been Weight
        self.WtUnits = wtunits
    
    #this method allows us to print the data in a reasonable method
    def Print(self):
        out = "\nName:\t\t"+self.Name+"\nSKU:\t\t"+self.SKU+"\n"+ \
            "Brand:\t\t"+self.Brand+"\nManufacturer:\t"+self.Manufacturer+"\n\n"+ \
            "Dimensions\n"+ \
            "\tWidth:\t"+str(self.Dimensions[0])+self.Dimensions[3]+"\n"+ \
            "\tDepth:\t"+str(self.Dimensions[1])+self.Dimensions[3]+"\n"+ \
            "\tHeight:\t"+str(self.Dimensions[2])+self.Dimensions[3]+"\n\n"+ \
            "\tWeight:\t"+str(self.Weight)+self.WtUnits+"\n"
        print(out)
    
    #demonstrates private data
    #another example of a method
    def SetPhone(self,PhoneNum):
        # Phone number format is XXX-XXX-XXXX
    
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
    
    #get phone method to display the phone number
    def GetPhone(self):
        return self.__PhoneNumber
    
    #method to calculate volume of product
    def PrintShelfVolume(self):
        volume = self.Dimensions[0]*self.Dimensions[1]*self.Dimensions[2]
        out = "Shelf Volume = " + str(volume) + " " + \
                self.Dimensions[3] + " cubed\n"
        print(out)
        return volume
    
    #method to calculate the footprint of the object on the shelf
    def FootprintArea(self):
        return self.Dimensions[0]*self.Dimensions[1]

#%%   Create two instances           

#our old instances when they were both treated as a 'Product' class

Milk23 = Product("DAR023","VG Skim Milk","Very Good Brands","Georgia Dairy",[8,8,10,"in"],2.2,"lbs")
Cer12 = Product("CER012","VG Corn Flakes","Very Good Brands","House Products, Inc.",[9,3,11,"in"],18,"oz")

#%%    Define the MilkProduct class

#tells Python that MilkProduct is a class that inherits all of the properties of the 'Product' class 
class MilkProduct(Product):
    
    #attributes
    Category = "Dairy"
    Storage = "Refrigerated"
    
    #the '=None' sets the default of the varialbe to None if not specified otherwise
    def __init__(self,sku,name,brand=None,manu=None,dims=None,wt=None, \
        wtunits=None,vol=None,fatcat="Whole",expir=None,servsize=None, \
        numserve=None,cals=None,fatgrams=None,fatcals=None,phone=None):
        
        #this line reinitiates the __init__ function of the class we are inheriting from
        #'Product.' specifies the class that we are inheriting from
        #then we list the objects its inheriting as we did when we set up the original class
        Product.__init__(self,sku,name,brand,manu,dims,wt,wtunits)
        
        #this specifies the new objects unique to the MilkProduct class
        self.Volume = vol
        self.FatCategory = fatcat
        self.ExpirationDate = expir
        self.ServingSize = servsize
        self.NumberServings = numserve
        self.Calories = cals
        self.FatGrams = fatgrams
        self.FatCalories = fatcals
        
        #the method .SetPhone has not been defined in the class MilkProduct at all
        #because of inheritance we can use it as if we had
        #the interpreter is looking for an attribute
            #if it doesn't find it in MilkProduct, it looks back into the class we are setting MilkProduct from (Product)
        #I think this means the function doesn't have to be defined
            #and if it does it has to follow the method .SetPhone
            #not that 'None' would be set as the phone number
        if phone!=None:
            self.SetPhone(phone)
       
#%%    Define the LaundreyDetergentProduct class   
    
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

#%%   Create two instances     

#Milk23 defines all of the variables we have set up for the MilkProduct class and the Product class
Milk23 = MilkProduct("DAR023","VG Skim Milk","Very Good Brands", \
        "Georgia Dairy",[8,8,10,"in"],2.2,"lbs","1Gal","Skim","2014-09-27", \
        8,16,90,0,0,"305-735-4353")

#Det16 DOES NOT define every varaible for the LaundryDetergentProduct class and Product class
    #we didn't define the 'manu' variable, we have skipped it
    #but must define every variable we are setting after we skipped 'manu'        
Det16 = LaundryDetergentProduct("LAU016","VG Laundry Detergent", \
        "Very Good Brands", dims=[9,3,11,"in"], wt=18, wtunits="oz", \
        numloads=72, sudslevel="HE", form="Liquid")

#%%

##############################
# Examine what we've created #
##############################

#Milk23

Milk23.SKU #Milk23 has all of the variables in product

Milk23.ServingSize #now Milk23 also has attributes unique to MilkProducts

Milk23.FootprintArea #has methods defined that are defined in Product

Milk23.Volume

#if we get lost, we can look at all the attributes of Milk23 like so
dir(Milk23)

#Det16
dir(Det16)
Det16.SKU
Det16.Dimensions
Det16.SudsingLevel
Det16.Scent #nothing appears with this command because this was never defined

