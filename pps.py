#VACCINE BOOKING SYSTEM

print("==========================================================================")
print("**************************************************************************")

print("                         BOOK YOUR VACCINE")

print("**************************************************************************")
print("==========================================================================")
print("")

import pickle #Python pickle module is used for serializing and de-serializing python object structures.

import os     #The OS module in Python provides functions for interacting with the operating system.



print("Don't Hesitate let's vaccinate!!")
print("")


#function  to add details of the person getting vaccinated.

def persondetails():
    vaccine=[]
    adharno=int(input("Enter Adhar number:"))
    name=input("Enter person name:")
    age=int(input("Enter person age:"))
    vactype=input("Enter vaccine type:")
    vaccine=[adharno,name,age,vactype]
    f=open("Vaccine2022.dat",'ab') #opening a binary file in append mode
    pickle.dump(vaccine,f)
    f.close()



#function to search details of the person  entered by the user
    
def searchdetails(adharno):#adharno  should be entered by the user
    f=open("Vaccine2022.dat",'rb')
    flag=False
    while True:
        try:
            rec=pickle.load(f)
            if adharno==rec[0]:
                print("Person Name:",rec[1])
                print("Person Age:",rec[2])
                print("Vaccine type:",rec[3])
                flag=True
        except EOFError:
            break
    if flag==False:
        print("No Records found")
    f.close()


#function to delete details of the person entered by the user


def deletedetails(adharnum):#adharno  should be entered by the user
    f=open("Vaccine2022.dat",'rb')
    f1=open("Temp.dat",'wb')
    found=False
    while True:
        try:
            rec=pickle.load(f)
            if rec[0]==adharnum:
                found=True
                print("Data Deleted Successfully")
            else:
                pickle.dump(rec,f1)
        except EOFError:
            break
    f.close()
    f1.close()
    os.remove("Vaccine2022.dat")
    os.rename("Temp.dat","Vaccine2022.dat")


#function to display details of all vaccinated person


def displaydetails():
    with open("Vaccine2022.dat",'rb') as f:
        while True:
            try:
                record=pickle.load(f)
                print("Adhar Number:",record[0])
                print("Person Name:",record[1])
                print("Person Age:",record[2])
                print("Vaccine Type:",record[3])
            except EOFError:
                break


#menu driven program

#main function
            
ch=0

while(ch!=5):
    
    print("1.Enter Person Details")
    print("2.Search Person Details")
    print("3.Delete Person Details")
    print("4.Display Person Details")
    print("5.Exit")
    print("")
    ch=int(input("Enter your choice:"))
    print()
    
    if (ch==1):
        persondetails()
        
    elif (ch==2):
        adharno=int(input("Enter adhar number to be Searched:"))
        searchdetails(adharno)
        
    elif (ch==3):
        adharnum=int(input("Enter adhar number to be Deleted:"))
        deletedetails(adharnum)
        
    elif (ch==4):
        displaydetails()
        
    elif (ch==5):
        print("Thank You!!")
        
    else:
        print("Enter the valid choice between 1 and 5")


#Prevention is better than cure so start getting vaccinated
#end
print("--------------------------------------------------------------------")
