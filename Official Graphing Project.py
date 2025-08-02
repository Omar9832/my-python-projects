import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt 
import sympy as sp  

i=1
class GUI:
    def __init__(self):
        global i

        self.main=tk.Tk() #creates a new window for home and assigns its properties
        self.main.geometry("1000x1000")
        self.main.title("Home")
        self.main.configure(bg="#008B8B")


        self.mainframe1=tk.Frame(self.main, highlightbackground="red", highlightthickness=5) #creates a frame for the title with its designated attributes 
        self.mainframe1.place(x=550, y=100)
        
        self.mainlabel1=tk.Label(self.mainframe1, text="Calculator", height=3, width=30, fg="maroon", font=("Arial", 30)) #create a label that acts as the title for home page
        self.mainlabel1.pack()


        self.mainframe2=tk.Frame(self.main, highlightbackground="green", highlightthickness="3", height=15)  #creates a frame for the buttons
        self.mainframe2.place(x=675, y=500)  

        self.mainframe2.columnconfigure(0, weight=1)  #creates a 1 row and 2 column arrangement
        self.mainframe2.columnconfigure(1, weight=1)


        self.mainbutton1=tk.Button(self.mainframe2, text="Sign up", font=("Arial", 15), bg="#00008B", fg="#98FF98", height=5, width=20, command=self.gotosignup)  #creates first button for sign up
        self.mainbutton1.grid(row=0, column=0, sticky="we")

        self.mainbutton2=tk.Button(self.mainframe2, text="log in", height=5, width=20, bg="#00008B", fg="#98FF98", font=("Arial", 15), command=self.gotologin)  #creates second button for log in
        self.mainbutton2.grid(row=0, column=1, sticky="we")

        self.mainbutton3=tk.Button(self.main, text="CLOSE", height=5, width=20, font=("Arial", 15), bg="#333333", fg="#98FF98", command=self.closewindow1)  #creates a secong button for close
        self.mainbutton3.place(x=800, y=800)

        while i>0:
            self.signupentry1=tk.Entry()
            self.signupentry2=tk.Entry()
            self.signupentry3=tk.Entry()
            self.usercred1={}
            self.usercred1[self.signupentry2.get()]=self.signupentry1.get()
            self.usercred2={}
            self.usercred2[self.signupentry2.get()]=self.signupentry3.get()
            i=i-1

        self.main.mainloop() #runs the window

    def closewindow1(self):
        self.main.destroy()    #destroys the window
        print("Home window closed.....")

    def gotosignup(self):
        self.main.withdraw()    #creates a window for sign up and assigns its properties
        self.signup=tk.Toplevel(self.main)
        self.signup.geometry("500x500")
        self.signup.title("Sign up")
        self.signup.configure(bg="#333333")

        self.signupframe1=tk.Frame(self.signup, bg="#333333")   #creates a frame for username, email, and password
        self.signupframe1.pack()

        self.signupframe1.columnconfigure(0, weight=1)  #creates columns
        self.signupframe1.columnconfigure(1, weight=1)
    

        self.signuplabel1=tk.Label(self.signupframe1, text="Sign Up", height=5, width=15, bg="#333333", fg="#FFD700", font=("Arial", 20)) #creates a title for sign up window
        self.signuplabel1.grid(row=0, column=0, columnspan=2, sticky="news", pady=25)

    

        self.signuplabel2=tk.Label(self.signupframe1, text="Username", height=5, width=10, fg="#FFFFFF", bg="#333333", font=("Arial", 15))  #creates label for username
        self.signuplabel2.grid(row=1, column=0)

        self.signupentry1=tk.Entry(self.signupframe1, font=("Arial", 20), width=50)   #creates entry for username
        self.signupentry1.grid(row=1, column=1, pady=15)

        self.signuplabel3=tk.Label(self.signupframe1, text="Email(ends with @hotmail.com or @gmail.com)", bg="#333333", fg="#FFFFFF", font=("Arial", 15), height=5, width=40)   #creates label for email
        self.signuplabel3.grid(row=2, column=0)

        self.signupentry2=tk.Entry(self.signupframe1, font=("Arial", 20), width=50)   #creates entry for email
        self.signupentry2.grid(row=2, column=1, pady=15)

        self.signuplabel4=tk.Label(self.signupframe1, text="Password", height=5, width=10, bg="#333333", fg="#FFFFFF", font=("Arial", 15))  #creates a label for password
        self.signuplabel4.grid(row=3, column=0)

        self.signupentry3=tk.Entry(self.signupframe1, font=("Arial", 20), width=50, show="*") #creates an entry for password
        self.signupentry3.grid(row=3, column=1, pady=15)


        self.signuplabel5=tk.Label(self.signupframe1, text="Re-type Password", height=5, width=15, font=("Arial", 15), bg="#333333", fg="#FFFFFF")  #creates  a label for re-type password
        self.signuplabel5.grid(row=4, column=0)

        self.signupentry4=tk.Entry(self.signupframe1, font=("Arial", 20), width=50, show="*")  #creates entry for re-type password
        self.signupentry4.grid(row=4, column=1, pady=15)

        self.signupcheckbuttonvar=tk.IntVar(value=0)

        self.signupcheckbutton=tk.Checkbutton(self.signup, text="Show Password", height=5, font=("Arial", 15), variable=self.signupcheckbuttonvar, command=self.showpassword)    #creates checkbutton for showing password
        self.signupcheckbutton.pack(padx=10, pady=10)                                                                              

        self.signupbutton1=tk.Button(self.signup, text="Sign Up", height=3, width=10, bg="#FFD700", font=("Arial", 15), command=self.gotosignupfinished)  #creates a button for sign up
        self.signupbutton1.pack(padx=10, pady=10)




        self.signup.mainloop()      #runs the window for sign up


    def showpassword(self):
        if self.signupcheckbuttonvar.get()==1:
            self.signupentry3.configure(show="")        #password will be shown if checked
            self.signupentry4.configure(show="")

        else:
            
            self.signupentry3.configure(show="*")       #password will be not be shown when
            self.signupentry4.configure(show="*")

    def gotosignupfinished(self):
        if not(self.signupentry1.get() and self.signupentry2.get() and self.signupentry3.get() and self.signupentry4.get()):
            messagebox.showerror("Error", "Please make sure to fill out everything")
        elif self.signupentry1.get() in self.usercred1:
            messagebox.showerror("Error", "Username already exists")
        elif self.signupentry2.get() in self.usercred1:
            messagebox.showerror("Error", "Email already exists")
        elif not(self.signupentry2.get().endswith("@hotmail.com") or self.signupentry2.get().endswith("@gmail.com")):
            messagebox.showerror("Error", "Email should end with hotmail.com or gmail.com")
        elif not(self.signupentry3.get()==self.signupentry4.get()):
            messagebox.showerror("Error", "Passwords must be equal")
        else:
            
            self.usercred1[self.signupentry2.get()]=self.signupentry1.get()
            self.usercred1[self.signupentry2.get()]=self.signupentry3.get()
            self.signup.withdraw()
            self.gotohome2()

                
    def gotohome2(self):
        self.home2=tk.Toplevel(self.main)
        self.home2.geometry("500x500")
        self.home2.title("Home")
        self.home2.configure(bg="#333333")
        self.home2frame1=tk.Frame(self.home2, bg="#333333")
        self.home2frame1.pack()
        self.home2label1=tk.Label(self.home2frame1, text="Home", height=5, width=15, bg="#333333", fg="#FFD700", font=("Arial", 50))
        self.home2label1.grid(row=0, column=0, sticky="news")
        self.home2button1=tk.Button(self.home2frame1, text="Graph", height=10, width=80, font=("Arial", 15), bg="#FFD700", command=self.gotograph)
        self.home2button1.grid(row=1, column=0)
        self.home2mainmenu=tk.Menu(self.home2)
        self.home2submenu=tk.Menu(self.home2mainmenu, tearoff=0, bg="#FFD700")
        self.home2submenu.add_command(label="Account")
        self.home2submenu.add_command(label="Delete Account")
        self.home2submenu.add_command(label="Log Out")
        self.home2mainmenu.add_cascade(menu=self.home2submenu, label=self.signupentry1.get())
        self.home2.config(menu=self.home2mainmenu)
        self.home2.mainloop()
    
    def gotograph(self):
        self.home2.withdraw()
        self.graph=tk.Toplevel(self.main)
        self.graph.geometry("1000x1000")
        self.graph.title("Graph")
        self.graph.configure(bg="#333333")
        self.graphframe1=tk.Frame(self.graph, bg="#333333")
        self.graphframe1.pack()
        self.graphlabel1=tk.Label(self.graphframe1, text="Choose functions", height=5, width=15, font=("Arial", 20), bg="#333333", fg="#FFD700")
        self.graphlabel1.grid(row=0, column=0, columnspan=2, sticky="news")
        self.graphlabel2=tk.Label(self.graphframe1, text="Function 1", height=5, width=15, bg="#333333", fg="#FFD700", font=("Arial", 15))
        self.graphlabel2.grid(row=1, column=0)
        self.graphentry1=tk.Entry(self.graphframe1, font=("Arial", 20), width=50)
        self.graphentry1.grid(row=1, column=1, pady=15)
        self.graphlabel3=tk.Label(self.graphframe1, text="Function 2", height=5, width=15, bg="#333333", fg="#FFD700", font=("Arial", 15))
        self.graphlabel3.grid(row=2, column=0)
        self.graphentry2=tk.Entry(self.graphframe1, font=("Arial", 20), width=50)
        self.graphentry2.grid(row=2, column=1, pady=15)
        self.graphbutton1=tk.Button(self.graph, text="Submit", height=3, width=10, bg="#FFD700", font=("Arial", 15), command=self.gotofinishedgraph)  #creates a button for sign up
        self.graphbutton1.pack(padx=10, pady=10)
        self.graph.mainloop()

    def gotofinishedgraph(self):
        self.cleaned_input1=" ".join(self.graphentry1.get().split())
        self.cleaned_input2=" ".join(self.graphentry2.get().split())
        if not(self.graphentry1.get() and self.graphentry2.get()):
                messagebox.showerror("Error", "Please fill all")
        try:
            self.expression1=sp.sympify(self.cleaned_input1.replace('^', '**'))
            self.expression2=sp.sympify(self.cleaned_input2.replace('^', '**'))
        except sp.SympifyError:
            messagebox.showerror("Error", "Functions must be polynomial")
            return
        x=sp.symbols('x')
        yvalues=[]
        xvalues=[0, 2, 3, 4, 5]
        for xvalue in xvalues:
            self.sub=self.expression1.subs(x, xvalue)
            result=self.sub.evalf()
            yvalues.append(float(result))
            
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        yvalues2=[]
        for xvalue in xvalues:

            self.sub=self.expression2.subs(x, xvalue)
            result=self.sub.evalf() 
            yvalues2.append(float(result))
            
            
        plt.plot(xvalues, yvalues, label=f"Function 1: {self.expression1}", mec="red", mfc="blue", linestyle="solid")
        plt.plot(xvalues, yvalues2, label=f"Function 2: {self.expression2}", mec="green", mfc="orange", linestyle="solid")
        plt.title(f"The graph of {self.expression1} and {self.expression2}")
        plt.legend()
        plt.grid()
        plt.show()

                



    def gotologin(self):
        self.main.withdraw()
        self.login=tk.Toplevel(self.main)
        self.login.geometry("500x500")
        self.login.title("Log In")
        self.login.configure(bg="#333333")
        self.loginframe1=tk.Frame(self.login, bg="#333333")
        self.loginframe1.pack()
        self.loginlabel1=tk.Label(self.loginframe1, text="Log In", height=5, width=15, font=("Arial", 20), bg="#333333", fg="#FFD700")
        self.loginlabel1.grid(row=0, column=0, columnspan=2, pady=25, sticky="news")
        self.loginlabel2=tk.Label(self.loginframe1, text="Email", height=5, width=10, font=("Arial", 20), bg="#333333", fg="#FFFFFF")
        self.loginlabel2.grid(row=1, column=0)
        self.loginentry1=tk.Entry(self.loginframe1, font=("Arial", 20), width=50)
        self.loginentry1.grid(row=1, column=1, pady=15)
        self.loginlabel3=tk.Label(self.loginframe1, text="Password", height=5, width=10, font=("Arial", 20), bg="#333333", fg="#FFFFFF")
        self.loginlabel3.grid(row=2, column=0)
        self.loginentry2=tk.Entry(self.loginframe1, font=("Arial", 20), width=50, show="*")
        self.loginentry2.grid(row=2, column=1, pady=15)
        self.logincheckbuttonvar=tk.IntVar(value=0)
        self.logincheckbutton1=tk.Checkbutton(self.login, text="Show Password", height=5, font=("Arial", 15), variable=self.logincheckbuttonvar, command=self.showpassword2)
        self.logincheckbutton1.pack(padx=10, pady=10)
        self.loginbutton1=tk.Button(self.login, text="Log In", height=3, width=10, bg="#FFD700", font=("Arial", 15), command=self.gotologinfinished)
        self.loginbutton1.pack(padx=10, pady=10)
        self.login.mainloop()

    
    def showpassword2(self):
        if self.logincheckbuttonvar.get()==1:
            self.loginentry2.configure(show="")
        else:
            self.loginentry2.configure(show="*")
    def gotologinfinished(self):
        if not(self.loginentry1.get() and self.loginentry2.get()):
            messagebox.showerror("Error", "Please make sure to enter everything")
        elif not(self.loginentry1.get() in self.usercred1):
            messagebox.showerror("Error", "Email does not exist")
        elif not(self.loginentry2.get()==self.usercred2[self.loginentry2.get()]):
            messagebox.showerror("Error", "Invalid Password")
        else:
            self.login.withdraw()
            self.gotohome2()

        
GUI()

    