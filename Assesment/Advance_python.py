
import pymysql,re,random 

try:
    admin_db=pymysql.connect(host='localhost',user='root',passwd='',database='bank')
    print('Database Connected!')
except Exception as e:
    print(e)

cr=admin_db.cursor()
#Admin crete table
admin_create_table='create table admindata(admin_id int primary key auto_increment,user_name varchar(30),password varchar(20))'
try:
    cr.execute(admin_create_table)
    print('Table created!')
except Exception as e:
    print(e)

#Customer login crete table
cust_create_table='create table customer_login_data(cust_id int primary key auto_increment,user_name varchar(30),password varchar(20),acc_no int,cust_name varchar(20),opening_bal int)'
try:
    cr.execute(cust_create_table)
    print('Table created!')
except Exception as e:
    print(e)

class RegisterAdmin:
    pass_pattern="[a-zA-z0-9]+[!@#$_*]+[a-zA-Z0-9]"
    admin_user_name=''
    admin_password=''
    
    def get_admin_data(self):
        self.user_input=input('Enter User Name: ')
        self.password=input('Enter Password(min 8 char & max 12 char): ')

        if len(self.password) >= 8 and len(self.password) <= 12:
            self.check_pass=re.findall(self.pass_pattern, self.password)

            if self.check_pass:
                self.admin_password = self.password
                self.admin_user_name = self.user_input
                #Data insert
                admin_data_insert='insert into admindata(user_name,password)values(%s,%s)'
                try:
                    cr.execute(admin_data_insert,(self.admin_user_name,self.admin_password))
                    admin_db.commit()
                    print('Record inserted!')
                except Exception as e:
                    print(e)

                print('Valid Password!')
            else:
                print('Error! Please Enter Valid Password..')
        else:
            print('Error! Please Enter Valid password..')


class Banker(RegisterAdmin):
    cust_user_name=''
    cust_password=''
    cust_acc_num=0
    cust_name=''
    op_bal=0

    def op_menu(self):
        print(f"{' '*40}Welcome to Banker's App\n")
        print(f"{' '*40}Operations Menu\n")
        print(f"{' '*40}1) Register")
        print(f"{' '*40}2) Login")
        print(f"{' '*40}3) Update all Customers")
        print(f"{' '*40}4) View all Customers")
        print(f"{' '*40}5) Delete all Customers")

    def admin_log_in(self):
        user_login=input('Enter Your User Name: ')
        user_password=input('Enter Your Password: ')
        #show data
        show_data=f'select * from admindata where password="{user_password}"'
        try:
            cr.execute(show_data)
            data=cr.fetchall()
            return data[0][1],data[0][2],user_login,user_password
        except Exception as e:
            print(e)

    def cust_op_menu(self):
        print(f"{' '*40}Welcome to Customer's App\n")
        print(f"{' '*40}Operations Menu\n")
        print(f"{' '*40}1) Register")
        print(f"{' '*40}2) Login")
        print(f"{' '*40}3) Withdraw Amount")
        print(f"{' '*40}4) Deposite Amount")
        print(f"{' '*40}5) View Balance")

    def get_cust_data(self):
        user_input=input('Enter User Name: ')
        password_input=input('Enter Password(min 8 char & max 12 char): ')
        name=(input('Enter Customer Name= '))
        balance=int(input('Enter Account Opening Balance(minmum balance 5000rs.): '))
        cust_acc_num=random.randint(9999,19999)

        if balance >= 5000:
            if len(password_input) >= 8 and len(password_input) <= 12:
                check_pass=re.findall(self.pass_pattern, password_input)
                if check_pass:
                    cust_password = password_input
                    cust_user_name = user_input
                    #Data insert
                    user_data_insert='insert into customer_login_data(user_name,password,acc_no,cust_name,opening_bal)values(%s,%s,%s,%s,%s)'
                    try:
                        cr.execute(user_data_insert,(cust_user_name,cust_password,cust_acc_num,name,balance))
                        admin_db.commit()
                        print('Record inserted!')
                    except Exception as e:
                        print(e)
                    print('Valid Password!')
                else:
                    print('Error! Please Enter Valid Password..')
            else:
                print('Error! Please Enter Valid password..')
        else:
            print('Error! Please Enter minimum account opening balance..')

    def cust_log_in(self):
        cust_login=input('Enter Your User Name: ')
        cust_password=input('Enter Your Password: ')
        #show data
        show_data=f'select * from customer_login_data where password="{cust_password}"'
        try:
            cr.execute(show_data)
            data=cr.fetchall()
            return data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],cust_login,cust_password
        except Exception as e:
            print(e)

    def delete_all_cust(self):
        #delete all record
        delete_data='drop table customer_login_data'
        try:
            cr.execute(delete_data)
            admin_db.commit()
            print('Data Deleted!')
        except Exception as e:
            print(e)

# =========================================================================================================

rga=RegisterAdmin()
# rga.get_admin_data()

bank=Banker()


print(f'{" "*40}WELCOME TO PYTHON BANK RANAGEMENT SYSTEM\n')
print(f'{" "*40}Select your role\n')
print(f'{" "*45}1) Banker')
print(f'{" "*45}2) Customer\n')
print(f'{" "*45}3) Exit\n')

print('choose your role :')
main_ch=int(input('> '))

if main_ch == 1:
    bank.op_menu()
    menu_ch=int(input('Enter operation which you want to perform: '))
    if menu_ch == 1:
        rga.get_admin12_data()
    elif menu_ch == 2:
        x=bank.admin_log_in()
        if x[2] == x[0] and x[1] == x[3]:
            print('Login successfull!')
        else:
            print('Error!please Enter Valid Username & Password')
    elif menu_ch == 3:
        x=bank.admin_log_in()      
        if x[2] == x[0] and x[1] == x[3]:
            print('Login successfull!')
        else:
            print('Error!please Enter Valid Username & Password')
    elif menu_ch == 4:
        x=bank.admin_log_in()
        if x[2] == x[0] and x[1] == x[3]:
            print('Login successfull!')
            #Show Data
            show_cust_data='select * from customer_login_data'
            try:
                cr.execute(show_cust_data)
                data=cr.fetchall()
                for i in data:
                    print('\nCustomer Account Number: ',i[3])
                    print('Customer Name: ',i[4])
                    print('Balance: : ',i[5])
            except Exception as e:
                print(e)
        else:
            print('Error!please Enter Valid Username & Password')
    elif menu_ch == 5:
        x=bank.admin_log_in()
        if x[2] == x[0] and x[1] == x[3]:
            print('Login successfull!')
            bank.delete_all_cust()
        else:
            print('Error!please Enter Valid Username & Password')

    while True:
        more_opp=input("Do you want to perform more operations press 'y' for yes and press 'n' for no: ")

        if more_opp.lower() == 'y':
            bank.op_menu()
            menu_ch=int(input('Enter operation which you want to perform: '))
            if menu_ch == 1:
                rga.get_cust_data()
            elif menu_ch == 2:
                x=bank.admin_log_in()
                if x[2] == x[0] and x[1] == x[3]:
                    print('Login successfull!')
                else:
                    print('Error!please Enter Valid Username & Password')
            elif menu_ch == 3:
                x=bank.admin_log_in()      
                if x[2] == x[0] and x[1] == x[3]:
                    print('Login successfull!')
                else:
                    print('Error!please Enter Valid Username & Password')
            elif menu_ch == 4:
                x=bank.admin_log_in()
                if x[2] == x[0] and x[1] == x[3]:
                    print('Login successfull!')
                    #Show Data
                    show_cust_data='select * from customer_login_data'
                    try:
                        cr.execute(show_cust_data)
                        data=cr.fetchall()
                        for i in data:
                            print('\nCustomer Account Number: ',i[3])
                            print('Customer Name: ',i[4])
                            print('Balance: : ',i[5])
                    except Exception as e:
                        print(e)
                else:
                    print('Error!please Enter Valid Username & Password')
            elif menu_ch == 5:
                x=bank.admin_log_in()
                if x[2] == x[0] and x[1] == x[3]:
                    print('Login successfull!')
                    bank.delete_all_cust()
                else:
                    print('Error!please Enter Valid Username & Password')
        else:
            exit(0)


        
elif main_ch == 2:
    bank.cust_op_menu()
    cust_menu_ch=int(input('Enter operation which you want to perform: '))
    if cust_menu_ch == 1:
        bank.get_cust_data()
    if cust_menu_ch == 2:
        y=bank.cust_log_in()
        print(y)
        if y[5] == y[0] and y[6] == y[1]:
            print('Login successfull!')
        else:
            print('Error!please Enter Valid Username & Password')
    if cust_menu_ch == 3:
        z=bank.cust_log_in()
        if z[5] == z[0] and z[6] == z[1]:
            print('Login successfull!')
            amount_input=int(input('Enter Withdraw Amount: '))
            if z[4] >= 2000:
                final_amount=z[4] - amount_input
                #update record
                update_record=f'update customer_login_data set opening_bal={final_amount} where user_name="{z[0]}"'
                try:
                    cr.execute(update_record)
                    admin_db.commit()
                    print('Record Updated!')
                except Exception as e:
                    print(e)
            else:
                print('Error! Insuficient Balance....')
        else:
            print('Error!please Enter Valid Username & Password')
    if cust_menu_ch == 4:
        z=bank.cust_log_in()
        if z[5] == z[0] and z[6] == z[1]:
            print('Login successfull!')
            deposite_input=int(input('Enter Deposite Amount: '))
            
            total_amount=int(z[4]) + deposite_input
            #update record
            update_record=f'update customer_login_data set opening_bal={total_amount} where user_name="{z[0]}"'
            try:
                cr.execute(update_record)
                admin_db.commit()
                print('Record Updated!')
            except Exception as e:
                print(e) 
        else:
            print('Error!please Enter Valid Username & Password')
    if cust_menu_ch == 5:
        z=bank.cust_log_in()
        if z[5] == z[0] and z[6] == z[1]:
            print('Login successfull!')
            #Show data
            show_bal=f'select opening_bal from customer_login_data where user_name="{z[0]}"'
            try:
                cr.execute(show_bal)
                data=cr.fetchall()
                print('Balance: ',data[0][0])
            except Exception as e:
                print(e) 
        else:
            print('Error!please Enter Valid Username & Password')

    while True:
        more_op=input("Do you want to perform more operations press 'y' for yes and press 'n' for no: ")
        
        if more_op.lower() == 'y':
            bank.cust_op_menu()
            cust_menu_ch=int(input('Enter operation which you want to perform: '))
            if cust_menu_ch == 1:
                bank.get_cust_data()
            if cust_menu_ch == 2:
                y=bank.cust_log_in()
                print(y)
                if y[5] == y[0] and y[6] == y[1]:
                    print('Login successfull!')
                else:
                    print('Error!please Enter Valid Username & Password')
            if cust_menu_ch == 3:
                z=bank.cust_log_in()
                if z[5] == z[0] and z[6] == z[1]:
                    print('Login successfull!')
                    amount_input=int(input('Enter Withdraw Amount: '))
                    if int(z[4]) >= 2000:
                        final_amount=int(z[4]) - amount_input
                        #update record
                        update_record=f'update customer_login_data set opening_bal={final_amount} where user_name="{z[0]}"'
                        try:
                            cr.execute(update_record)
                            admin_db.commit()
                            print('Record Updated!')
                        except Exception as e:
                            print(e)
                    else:
                        print('Error! Insuficient Balance....')
                else:
                    print('Error!please Enter Valid Username & Password')
            if cust_menu_ch == 4:
                z=bank.cust_log_in()
                if z[5] == z[0] and z[6] == z[1]:
                    print('Login successfull!')
                    deposite_input=int(input('Enter Deposite Amount: '))
                    
                    total_amount=int(z[4]) + deposite_input
                    #update record
                    update_record=f'update customer_login_data set opening_bal={total_amount} where user_name="{z[0]}"'
                    try:
                        cr.execute(update_record)
                        admin_db.commit()
                        print('Record Updated!')
                    except Exception as e:
                        print(e) 
                else:
                    print('Error!please Enter Valid Username & Password')
            if cust_menu_ch == 5:
                z=bank.cust_log_in()
                if z[5] == z[0] and z[6] == z[1]:
                    print('Login successfull!')
                    #Show data
                    show_bal=f'select opening_bal from customer_login_data where user_name="{z[0]}"'
                    try:
                        cr.execute(show_bal)
                        data=cr.fetchall()
                        print('Available Balance: ',data[0][0])
                    except Exception as e:
                        print(e) 
                else:
                    print('Error!please Enter Valid Username & Password')
        else:
            exit()


        
