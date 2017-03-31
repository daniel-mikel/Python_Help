#Part 9 of a Python/Spyder Tutorial

#based on a tutorial at
#https://www.youtube.com/watch?v=oj4bWBFptt4

#materials and further material available at:
    #http://datasciencesource.com/PythonWithSpyderMaterials/

#this is part 2 of a tutorial on objects in python

#we pick up were we left off, part of the code for the last section is below

#########
# Cells #
#########

#we set up cells blocks of code to make the code easier to execute
#now we can execute all code in the block by having clicked the cursor inside
    #then to execute the cell: ctrl+enter 
    #or to execute the current cell and move to the next cell: ctrl+shift 

#%%

class Product:
    def __init__(self, sku,name, brand, manu, dims, wt, wtunit):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacture = manu
        self.Dimensions = dims
        self.Weight = wt
        self.WtUnits = wtunit
        
#%%
     
Milk23 = Product("DAR023", "VG Skim Milk", "Very Good Brands", "Georgia Dairy, inc", [8,8,10,"in"], 2.2, "lbs")
Cer12 = Product("CER012", "VG Corn Flakes", "Very Good Brands", "House Products, inc.", [9,3,11,"in"], 18, "oz")    

#%%

###########
# Version #
###########

#we want the function to have a version number
#that way, if we change the code, we can see when the objects were made
#if we have errors, we will know when they break better
#probably has other uses as well

#%%

class Product:
    Version = "Ver 1.2, Rev 3"
    def __init__(self, sku,name, brand, manu, dims, wt, wtunit):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacture = manu
        self.Dimensions = dims
        self.Weight = wt
        self.WtUnits = wtunit
        
Milk23 = Product("DAR023", "VG Skim Milk", "Very Good Brands", "Georgia Dairy, inc", [8,8,10,"in"], 2.2, "lbs")
Cer12 = Product("CER012", "VG Corn Flakes", "Very Good Brands", "House Products, inc.", [9,3,11,"in"], 18, "oz")    

Milk23.Version #allows us to see what version of the dynamic function the object was created under
        
#%%

#this also shows that you can have variables that are dynamically created with ones that aren't dynamically created

#version is an ATTRIBUTE that will be attached to every instance of this object

########################
# the __init__ function#
########################

#executed automatically, here when Product is used to create an instance

##########
# Method #
##########

#Now we create a METHOD for this code

#About the Print function
    # /n means start on new line
    # /t means new tab
    # the "+ \" Tells Python that you're using another line for the code
#%%

class Product:
    
    #attribute is here
    Version = "Ver 1.2 Rev 3"
    
    def __init__(self,sku,name,brand,manu,dims,wt,wtunits):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacturer = manu
        self.Dimensions = dims
        self.Weight = wt           # Should have been Weight
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

#%%        

Milk23 = Product("DAR023","VG Skim Milk","Very Good Brands","Georgia Dairy",[8,8,10,"in"],2.2,"lbs")
Cer12 = Product("CER012","VG Corn Flakes","Very Good Brands","House Products, Inc.",[9,3,11,"in"],18,"oz")        

#%%

#now we can use the print method that is a part of the class definition of the object
Cer12.Print()
Milk23.Print()

#########
# dir() #
#########
dir(Cer12) #gives you a list of all of the attributes of an object
   #and private information of the object

#########################################
# comment/uncomment large parts of code #
#########################################

#use "ctrl" + "1" to (un)comment selected lines at the same time
   