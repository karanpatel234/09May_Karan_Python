print("Welcome To Pytho Bank Management System")


def Role():
    print("1) Banker")
    print("2) Customer","\n")

    print("3) Exit")
def banker():
     print("1)  Add Customer")
     print("2)  View Customer")
     print("3)  Search Customer")
     print("4)  View All Customer")
     print("5)  Total Amounts In Bank","\n")
Add_costumer={}
def Bank():
    while True:
        '''print("1) Banker")
        print("2) Customer","\n")

        print("3) Exit")'''
        Role()        
        Bank_M=int(input("Enter a Role: "))
        if Bank_M==1:
                banker()
                Banker_Option=int(input("Selec your option: "))
                if Banker_Option==1:
                     add_Customer={}
                     Customer_Number=int(input("Enter a Number of Customer You want to Add: "))
                     for i in range(Customer_Number):
                          Account_No=input("Enter Account Number: ")
                          Costumer_Name=input("Enter Costumer Name: ")
                          Opening_Balance=input("Enter Opening Balance: ")
                          "Do you want to perform more operation press 'y' for yes and press 'n' for no : y" 


                          Add_costumer["Account No.":Account_No]={"Costumer Name:":Costumer_Name,"Opening Balance:":Opening_Balance}                                 
                                                                           
                elif Banker_Option==2:
                    if len(Add_costumer) >0:
                        print(Costumer_Name)
                    else:
                        print("No Data Found","\n")
                elif Banker_Option==3:
                     Search=input("Enter a Costumer Name: ")
                     if Search not in  Costumer_Name.values():
                          print("Sorry... Costumer Not Found....")
                     else:
                          print("Yes....")
                elif Banker_Option==4:
                    if len(Add_costumer)>0:
                        print(Add_costumer)
                    else:
                         print("No Data Found....")
                elif Banker_Option==5:
                     print("Sum of Total Amount: ",)
                                          
            
        else:
            #print("Exit")
            break

Bank()

"""def customers():
     print("1)  Withdrwa Amount")
     print("2)  Deposite Amount")
     print("3)  view Balance")"""