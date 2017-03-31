#Part 10 of a Python/Spyder Tutorial
#Private Data and Encapsulation

#based on a tutorial at
#https://www.youtube.com/watch?v=VstfQaQjSBc

#materials and further material available at:
    #http://datasciencesource.com/PythonWithSpyderMaterials/

#this is part 3 of a tutorial on objects in python

#we pick up were we left off, part of the code for the last section is below

##################################
# Private Data and Encapsulation #
##################################

#many problems occur in programs because of the side effects of code

#something may get changed and cause other parts of the program to stop working

#finding these can be time consuming

#the basic idea of Encapsulation is to have data is private to objects
    #and that the only way to change the data is to follow a method
    
###########
# Example #
###########

#phone numbers can be written in a variety of ways

#if we allow all of them to be written in the data, it can be messy to work with

#we will create a private variable
    #this way, phone numbers will be written in a standardized way
    #this will make our phone numbers consistent
    #phone numbers will not be able to be written in a different way

#Private Data Culture
    #you can technically overwrite private data in Python
    #it is more difficulte
    #it is greatly discouraged within the community
    

#%%

class Product:
    
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

    def SetPhone(self,PhoneNum):
        # Phone number format is XXX-XXX-XXXX
        #we need to make sure that the phone number is input in the right format
        
        #charecter string of numbers 1-9
        dgts="0123456789"
    
    #we're going to test whether the format is bad
        
        #need to make sure the number is a charecter string, tested below:
        BadFmt=False
        if type(PhoneNum)!=type("abc") or len(PhoneNum)!=12:
            BadFmt=True
        
        #now we test if the formats are in the right place
        if PhoneNum[3]!="-" or PhoneNum[7]!="-":
            BadFmt=True
        
        #now we test whether a charecter is in a string. here testing if
        if not ( PhoneNum[0] in dgts and PhoneNum[1] in dgts and \
                    PhoneNum[2] in dgts and PhoneNum[4] in dgts and \
                    PhoneNum[5] in dgts and PhoneNum[6] in dgts and\
                    PhoneNum[8] in dgts and PhoneNum[9] in dgts and \
                    PhoneNum[10] in dgts and PhoneNum[11] in dgts):
            BadFmt=True
        
        if BadFmt:
            print("Wrong phone number format. Use \"xxx-xxx-xxxx\"\n")
            return False
        
        #the __<name> indicates that this variable is private
        self.__PhoneNumber = PhoneNum #this line will either set the data or replace it
        
        return True
    
    #this part just returns the value of the private variable
    def GetPhone(self):
        return self.__PhoneNumber             
    

#%%

#Create two instances of the class product

Milk23 = Product("DAR023","VG Skim Milk","Very Good Brands","Georgia Dairy",[8,8,10,"in"],2.2,"lbs")
Cer12 = Product("CER012","VG Corn Flakes","Very Good Brands","House Products, Inc.",[9,3,11,"in"],18,"oz")

#%%

#if we try to call our private variable 
Milk23.__PhoneNumber #we haven't created it yet
Milk23.SetPhone("7894561234") # !! something went wrong, but regardless 
Milk23.GetPhone() #the code prevented the incorrect format from being saved

Milk23.SetPhone("789-456-1234") #now we use the correct format
Milk23.GetPhone() #and it outputs =)

#if we try to use an incorrect format again
Milk23.SetPhone("7a7.689.zzy6") #phone number that will be rejected
Milk23.GetPhone() #didn't overwrite

#this shows a nice way to avoid common bugs that can happen

#this object oriented strategy is called Encapsulation

