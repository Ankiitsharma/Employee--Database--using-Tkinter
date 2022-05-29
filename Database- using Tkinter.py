import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from PIL import ImageTk #to import jpg files

def login():
    
    username=str(entry1.get())
    password=str(entry2.get())
    
    if(username=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")
    elif(username=="1" and password=="1"):
        mainMenu()
        root.quit()
    else:
        messagebox.showerror("","incorrect username and password")

    
def create_fun():
    
    def saveRecord():
        e_id=m_id.get()
        e_name=m_name.get()
        e_dsg=m_dsg.get()
        e_salary=m_salary.get()
        e_city=m_city.get()
        
        
        con= pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            db="project"
        )
        cur=con.cursor()


       # try:
        if m_id=="":
            query=("insert into employee (e_name,e_dsg,e_salary,e_city)values(%s,%s,%s,%s)")
            val=(e_name,e_dsg,e_salary,e_city)
            cur.execute(query,val)
            con.commit()
            messagebox.showinfo("success","Record Inserted")
        else:
            query=("insert into employee (e_id,e_name,e_dsg,e_salary,e_city)values(%s,%s,%s,%s,%s)")
            val=(e_id,e_name,e_dsg,e_salary,e_city)
            cur.execute(query,val)
            con.commit()
            messagebox.showinfo("success","Record Inserted")
            creat_win.destroy()
            mainMenu()

        """except:
            messagebox.showwarning("Error","Enter the valid record <")"""

    
    creat_win=Tk()
    creat_win.title("welcome..")
    creat_win.state("zoomed")
    creat_win.resizable(False,False)
        #Label for create function:
        
    Label(creat_win,text=f"EMPLOYEE MANAGEMENT SYSTEM", font=("impect 15 bold"),bd=2,bg='gold2').grid(row=0,column=0,columnspan=5)
    title=Label(creat_win,text="Create a new employee record",font=("Goudy old style",8,"bold"),fg="black").grid(row=3,column=0,columnspan=3)
    e_id1=Label(creat_win,text="Enter Employee ID (Optional)",font=("impect",10,"bold"))
    e_id1.grid(row=4,column=0)
    e_name1=Label(creat_win,text="Enter Employee Name *",font=("impect",10,"bold"))
    e_name1.grid(row=6,column=0)
    e_dsg1=Label(creat_win,text="Enter Employee Designation *",font=("impect",10,"bold"))
    e_dsg1.grid(row=8,column=0)
    e_salary1=Label(creat_win,text="Enter Employee Salary *",font=("impect",10,"bold"))
    e_salary1.grid(row=10,column=0,)
    e_city1=Label(creat_win,text="Enter Employee City *",font=("impect",10,"bold"))
    e_city1.grid(row=12,column=0)
    
    #Entry for create function
    
    m_id=Entry(creat_win,bd=6)
    m_id.grid(row=4,column=1)
    m_name=Entry(creat_win,bd=6)
    m_name.grid(row=6,column=1)
    m_dsg=Entry(creat_win,bd=6)
    m_dsg.grid(row=8,column=1) 
    m_salary=Entry(creat_win,bd=6)
    m_salary.grid(row=10,column=1)   
    m_city=Entry(creat_win,bd=6)
    m_city.grid(row=12,column=1)
    
    get_details=Button(creat_win,text="Submit",font=("impect",10,"bold"),command= saveRecord,height=2,width=10,bd=3)
    get_details.grid(row=16,column=0)
   
    creat_win.mainloop()           

        

        
def display_fun():
    root3=Tk()
    root3.title("EMPLOYEE RECORD")
    root3.state("zoomed")
    Label(root3,text="EMPLOYEE RECORDS",font=("impect 10 bold"),bd=2,bg='gold2').pack()

    con= pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="project"
        )
    cur=con.cursor()
    quary="select * from employee"
    cur.execute(quary)
    
    rows=cur.fetchall()
    
    total=cur.rowcount # To show the total entries in table
    Label(root3,text="Total Data Entries :"+str(total),font=("impect 7 bold"),bd=2).pack()

    
    tv=ttk.Treeview(root3,column=(1,2,3,4,5), show="headings",height="20")
    tv.pack()


    tv.heading(1, text="ID")
    tv.heading(2, text="NAME")
    tv.heading(3, text="DESIGNATION")
    tv.heading(4, text="SALARY")
    tv.heading(5, text="CITY")
    

    for i in rows:
        tv.insert('','end',values=i)
        

        
def search_fun():
    def findResult():
        try:

            root5=Tk()
            root5.title("Result")
            root5.state("zoomed")
            find_e_id=(find_id.get())
            con= pymysql.connect(
                host="localhost",
                user="root",
                password="root",
                db="project"
            )
            cur=con.cursor()
            quary3="select * from employee where e_id='%s'"%find_e_id
            cur.execute(quary3)
            r=cur.fetchone()
            if(r is not None):
                tv=ttk.Treeview(root5,column=(1,2,3,4,5), show="headings",height="5")
                tv.pack()
                
                tv.heading(1, text="ID")
                tv.heading(2, text="NAME")
                tv.heading(3, text="DESIGNATION")
                tv.heading(4, text="SALARY")
                tv.heading(5, text="CITY")
                tv.insert('','end',values=r)
            else:
                root5.destroy()
                messagebox.showwarning("","No result Found...")

        except:
            root5.destroy()
            messagebox.showwarning("","Enter a valid employee ID ")

    root4=Toplevel()
    root4.state("zoomed")
    root4.resizable(False,False)
    root4.title("Serach")
    Label(root4,text=f"EMPLOYEE MANAGEMENT SYSTEM", font=("Arial Black",17,"bold"),bd=2,fg="black").grid(row=2,column=0,columnspan=7)
    Label(root4,text=f"EMPLOYEE ID :",font=("impect",13,"bold")).grid(row=6,column=0)

    global find_id
    find_id=Entry(root4,bd=5)
    find_id.grid(row=6,column=2)

    Button(root4,text="SEARCH",font=("Arial Black",9 ,"bold"),command=findResult,height=2,width=12,bd=3,bg="red",fg="white").grid(row=7,column=4)

    root4.mainloop()


def edit_fun():
    def find_R():
        pass
    
    edit_win= Tk()
    edit_win.title("Result")
    edit_win.geometry("600x400")
    edit_win.resizable(False,False)
    edit_win.title("Serach")
    Label(edit_win,text=f"EMPLOYEE MANAGEMENT SYSTEM", font=("Arial Black",17,"bold"),bd=2,fg="black").grid(row=1,column=0,columnspan=5)
    Label(edit_win,text= "UPDATE EMPLOYEE RECORD", font=("impect",10,"bold"),bd=2,fg="navy").grid(row=2,column=2)
    Label(edit_win,text="ENTER EMPLOYEE ID TO UPDATE :",font=("impect",10,"bold")).grid(row=4,column=0)

    global find_id
    up_entry=Entry(edit_win,bd=4)
    up_entry.grid(row=4,column=2)

    Button(edit_win,text="FIND",font=("Arial Black",9 ,"bold"),command=find_R,height=2,width=9,bd=3,bg="red",fg="white").grid(row=4,column=4)

    
    edit_win.mainloop()

def delete_fun():
    def del_Rec():
        del_2=str(delete_entry.get())
        con= pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            db="project"
            )

        cur=con.cursor()
        quary4=f"DELETE FROM employee WHERE e_id="+del_2
        cur.execute(quary4)
        messagebox.showinfo("success","Record Deleted")

            
    

    
    delete_record=Tk()
    delete_record.title("Delete Employee Record")
    delete_record.state("zoomed")
    delete_record.resizable(False,False)

    
    Label(delete_record,text=f"EMPLOYEE MANAGEMENT SYSTEM", font=("Arial Black",17,"bold"),bd=2,fg="black").grid(row=1,column=0,columnspan=5)
    Label(delete_record,text= "DELETE EMPLOYEE RECORD", font=("impect",10,"bold"),bd=2,fg="navy").grid(row=2,column=2)
    Label(delete_record,text="ENTER EMPLOYEE ID TO Delete :",font=("impect",10,"bold")).grid(row=4,column=0)
    delete_entry=Entry(delete_record,bd=4)
    delete_entry.grid(row=4,column=2)

    delete=Button(delete_record,text="Delete",font=("Arial Black",9 ,"bold"),command=del_Rec,height=2,width=9,bd=3,bg="red",fg="white").grid(row=4,column=4)

    
    delete_record.mainloop()

    

def exit_fun():
    option=messagebox.askyesno('confirmation','Do you want to logout?')
    if(option==True):
        root.destroy()
        



def mainMenu():
    username1=str(entry1.get())
    password1=str(entry2.get())
    root1=Toplevel()
    root1.title(f"welcome..{username1}")
    root1.state("zoomed")
    root1.resizable(False,False)
    #PhotoImage
    root1.bg=ImageTk.PhotoImage(file="images/menuImage.jpg")
    root1.bg_image=Label(root1,image=root1.bg).place(x=0,y=0)
    #Dashboard option
    Label(root1,text=f"<<<<<EMPLOYEE MANAGEMENT SYSTEM>>>>", font=("impect 18 bold"),bd=2,bg='gold2').grid(row=0,column=0,columnspan=9)    
    Button(root1,text="CREATE",font=("Arial Black",10,"bold"),command=create_fun,height=4,width=15,bd=4,padx=15,pady=10,bg="red",fg="white").grid(row=3,column=0)
    Button(root1,text="Display",font=("Arial Black",10,"bold"),command=display_fun,height=4,width=15,bd=4,padx=15,pady=10,bg="red",fg="white").grid(row=3,column=2)
    Button(root1,text="SEARCH",font=("Arial Black",10,"bold"),command=search_fun,height=4,width=15,bd=4,padx=15,pady=10,bg="red",fg="white").grid(row=3,column=3)
    Button(root1,text="EDIT",font=("Arial Black",10,"bold"),command=edit_fun,height=4,width=15,bd=4,padx=15,pady=10,bg="red",fg="white").grid(row=3,column=4)
    Button(root1,text="DELETE",font=("Arial Black",10," bold"),command=delete_fun,height=4,width=15,bd=4,padx=15,pady=10,bg="red",fg="white").grid(row=3,column=5)
    Button(root1,text="EXIT",font=("Arial Black",10,"bold"),command=exit_fun,height=4,width=15,bd=4,padx=15,pady=10,bg="red",fg="white").grid(row=3,column=6)
    root1.mainloop()

    
root=Tk()
root.title("Employee Login Page")
root.state("zoomed")
root.resizable(False,False)

#PhotoImage
root.bg=ImageTk.PhotoImage(file="images/image4.jpg")
root.bg_image=Label(root,image=root.bg).place(x=0,y=0)
frame_login=Frame(root,bg="white").place(x=20,y=75,height=210,width=380)


Label(frame_login,text="LOGIN SYSTEM",font=("times new roman",15,"bold"),bg='gold2').place(x=0,y=6,width=700,height=35)
Label(frame_login,text="Username",font=("impect",15,"bold"),bg="white").place(x=30,y=80)
Label(frame_login,text="Password",font=("impect",15,"bold"),bg="white").place(x=30,y=120)
#Button(root,text="Forget password...",fg="navy",command=forget,height=2,width=15,bd=0).place(x=25,y=90)
global entry1
global entry2

entry1=Entry(root,bd=6)
entry1.place(x=150,y=80)
entry2=Entry(root,show="*",bd=6)
entry2.place(x=150,y=120)


btn1=Button(root,text="Login",font=("Arial Black",9,"bold"),bg="red",fg="white",command=login,height=3,width=12,bd=5)
btn1.place(x=60,y=180)

root.mainloop()
