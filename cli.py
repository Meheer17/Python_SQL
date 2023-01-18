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
        print('''MENU
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
        ch=int(input("Enter your choice"))
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
            sql.DisplayAll()
        elif ch==8:
            sql.update()
        elif ch==9:
            sql.insert()
        elif ch==10:
            sql.del_rec()
        elif ch==11:
            break
        else:
            print("Invalid Choice")