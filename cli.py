import function as sql
f1=input("Please select Login or Signup. Select L for Login and S for Signup:  ")
if f1=="S" or f1=="s":
    print("SIGNUP")
    sql.SignUp()
elif f1=="L" or f1=="l":
    print("LOGIN")
    sql.Login()

if sql.Auth():
    while True:
        print('''\nMENU
        1. Display Table
        2. Create Table
        3. Describe Table
        4. Rename Table
        5. Delete Table
        6. Add/ Modify / Delete Column in Table
        7. Display Record
        8. Update Record
        9. Insert Record
        10. Delete Record
        11. Exit''')

        ch=int(input("\nEnter your choice: "))
        if ch==1:
            sql.ShowTable()
        elif ch==2:
            sql.CreateTable()
        elif ch==3:
            sql.DesTable()
        elif ch==4:
            sql.Rename()
        elif ch==5:
            sql.DropTable()
        elif ch==6:
            sql.ADMTable()
        elif ch==7:
            while True:
                print('\nMENU \n\t1. All \n\t2. With Where Clause \n\t3. Order By \n\t4. Group By \n\t5. Custom Query \n\t6. Exit')
                ch = int(input("\nEnter your choice: "))
                if ch == 1:
                    sql.DisplayAll()
                elif ch == 2:
                    sql.DisplayWithWhere()
                elif ch == 3:
                    sql.DisplayOrderBy()
                elif ch == 4:
                    sql.DisplayGroupBy()
                elif ch == 5:
                    sql.CustomQuery()
                elif ch == 6:
                    break
                else: 
                    print("Invalid")
        elif ch==8:
            sql.Update()
        elif ch==9:
            sql.insert()
        elif ch==10:
            sql.del_rec()
        elif ch==11:
            print("Bye!")
            break
        else:
            print("Invalid Choice")