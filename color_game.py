
import tkinter as tk
from tkinter import messagebox
import random
i=0
t=0
q=0
b=0
u=0
class GUI:
    
    def __init__(self):
        global t
        self.main=tk.Tk()
        self.main.geometry("1000x1000")
        self.main.configure(bg="aqua")
        self.main.wm_attributes("-fullscreen", True)
        self.displaytimer=tk.Label()
        self.colorgame=tk.Toplevel()
        self.colorgame.withdraw() 
        if t<1:
            self.userinfo1={}
            self.userinfo2={}
            t=t+1
        self.mainframe1=tk.Frame(self.main, highlightbackground="red", highlightthickness=5)
        self.mainlabel1=tk.Label(self.mainframe1, text="Welcome, do you want to play guessing text color game", height=5, font=("Bold", 20), bg="purple", fg="black")
        self.mainlabel1.pack(padx=10, pady=10)
        self.mainframe2=tk.Frame(self.main, highlightbackground="green", highlightthickness=5)
        self.mainframe2.columnconfigure(0, weight=1)
        self.mainframe2.columnconfigure(1, weight=1)
        self.mainbutton1=tk.Button(self.mainframe2, text="Sign Up or Log in", height=5, width=50, font=("Arial", 15), bg="maroon", fg="black", command=self.gotosignuporlogin)
        self.mainbutton1.grid(row=0, column=0, sticky="we")
        self.mainbutton2=tk.Button(self.mainframe2, text="CLOSE", height=5, width=50, font=("Arial", 15), bg="red", fg="black", command=self.destroymain)
        self.mainbutton2.grid(row=0, column=1, sticky="we")
        self.mainframe1.place(x=500, y=100)
        self.mainframe2.place(x=300, y=500)
        self.main.mainloop()
    def destroymain(self):
        self.main.destroy()
    
    def gotosignuporlogin(self):
      
        self.main.withdraw()
        self.signuporlogin=tk.Toplevel(self.main)
        self.signuporlogin.geometry("1000x1000")
        self.signuporlogin.title("Sign Up or Log in")
        self.signuporlogin.configure(bg="aqua")
        self.signuporlogin.wm_attributes("-fullscreen", True)
        self.signuporloginframe1=tk.Frame(self.signuporlogin, highlightbackground="purple", highlightthickness=5)
        self.signuporloginlabel1=tk.Label(self.signuporloginframe1, text="Sign up or Log in", width=100, height=5, font=("Bold", 20), bg="green", fg="black")
        self.signuporloginlabel1.pack(padx=10, pady=10)
        self.signuporloginbutton1=tk.Button(self.signuporlogin, text="Sign Up", width=100, height=5, font=("Arial", 15), bg="blue", fg="black", command=self.gotosignup)
        self.signuporloginbutton1.place(x=400, y=300)
        self.signuporloginbutton2=tk.Button(self.signuporlogin, text="Log in", width=100, height=5, font=("Arial", 15), bg="red", fg="black", command=self.gotologin)
        self.signuporloginbutton2.place(x=400, y=700)
        self.signuporloginbutton3=tk.Button(self.signuporlogin, text="Home", height=3, width=120, font=("Arial", 15), bg="green", fg="black", command=self.close1)
        self.signuporloginbutton3.place(x=300, y=900)
        self.signuporloginframe1.place(x=150, y=100)
       
        
    def close1(self):
        self.signuporlogin.destroy()
        self.main.deiconify()
    
    def gotosignup(self):
        self.signuporlogin.withdraw()
        self.signup=tk.Toplevel(self.main)
        self.signup.geometry("1000x1000")
        self.signup.title("Sign Up")
        self.signup.configure(bg="aqua")
        self.signup.wm_attributes("-fullscreen", True)
        self.signupframe1=tk.Frame(self.signup, highlightbackground="red", highlightthickness=5)
        self.signuplabel1=tk.Label(self.signupframe1, text="Sign Up", height=5, font=("Bold", 20), bg="maroon", fg="black", width=46)
        self.signuplabel1.pack(padx=10, pady=10)
        self.signupframe2=tk.Frame(self.signup, highlightbackground="orange", highlightthickness=3)
        self.signupframe2.columnconfigure(0, weight=1)
        self.signupframe2.columnconfigure(1, weight=1)
        self.signuplabel2=tk.Label(self.signupframe2, text="Create Username:", height=5, font=("Arial", 18), fg="black")
        self.signuplabel2.grid(row=0, column=0)
        self.signupentry1=tk.Entry(self.signupframe2, width=100, font=("Arial", 20))
        self.signupentry1.insert(0, "")
        self.signupentry1.grid(row=0, column=1)
        self.signuplabel3=tk.Label(self.signupframe2, text="Create Email(Must end with @hotmail.com or @gmail.com):", height=5, font=("Arial", 18), fg="black")
        self.signuplabel3.grid(row=1, column=0)
        self.signupentry2=tk.Entry(self.signupframe2, width=100, font=("Arial", 20))
        self.signupentry2.insert(0, "")
        self.signupentry2.grid(row=1, column=1)
        self.signuplabel4=tk.Label(self.signupframe2, text="Password:", height=5, font=("Arial", 18), fg="black")
        self.signuplabel4.grid(row=2, column=0)
        self.signupentry3=tk.Entry(self.signupframe2, width=100, font=("Arial", 20))
        self.signupentry3.insert(0, "")
        self.signupentry3.grid(row=2, column=1)
        self.signuplabel5=tk.Label(self.signupframe2, text="re-type password:", height=5, font=("Arial", 18), fg="black")
        self.signuplabel5.grid(row=3, column=0)
        self.signupentry4=tk.Entry(self.signupframe2, width=100, font=("Arial", 20))
        self.signupentry4.insert(0, "")
        self.signupentry4.grid(row=3, column=1)
        self.signupbutton1=tk.Button(self.signup, text="Sign Up", height=2, width=50, font=("Arial", 15), bg="green", fg="black", command=self.gotosignupfinished)
        self.signupbutton1.place(x=600, y=900)
        self.signupframe1.place(x=500, y=20)
        self.signupframe2.place(x=100, y=250)
        self.signupbutton2=tk.Button(self.signup, text="Back", height=5, width=20, font=("Arial", 15), bg="red", fg="black", command=self.close3)
        self.signupbutton2.place(x=25, y=900)
        
    
    def close3(self):
        self.signup.destroy()
        self.signuporlogin.deiconify()

    def gotosignupfinished(self):
        global t

        if not(self.signupentry1.get() and self.signupentry2.get() and self.signupentry3.get() and self.signupentry4.get()):
            messagebox.showerror("Error", "Please fill in everything")
        elif not(self.signupentry2.get().endswith("@hotmail.com") or self.signupentry2.get().endswith("@gmail.com")):
            messagebox.showerror("Error", "Please include @hotmail or @gmail.com at the end of your email")
        elif not(self.signupentry3.get()==self.signupentry4.get()):
            messagebox.showerror("Error", "Both passwords must be the same")
        elif self.signupentry2.get() in self.userinfo1:
            messagebox.showerror("Error", "Email already taken")
        elif self.signupentry1.get() in self.userinfo2:
            messagebox.showerror("Error", "Username already taken")
        else:
            self.userinfo1[self.signupentry2.get()]=self.signupentry3.get()
            self.userinfo2[self.signupentry2.get()]=self.signupentry1.get()
            print(self.userinfo2[self.signupentry2.get()], "has logged in")
            print(self.userinfo2[self.signupentry2.get()], "Email:", self.signupentry2.get())
            print(self.userinfo2[self.signupentry2.get()], "Password:", self.userinfo1[self.signupentry2.get()])
            print(self.userinfo1)
            print(self.userinfo2)
           
            self.signup.withdraw()
            self.Home2()
            
    def Home2(self):
        self.main2=tk.Toplevel(self.main)
        self.main2.geometry("1000x1000")
        self.main2.title("Home 2")
        self.main2.configure(bg="aqua")
        self.main2.wm_attributes("-fullscreen", True)
        self.main2frame1=tk.Frame(self.main2, highlightbackground="green", highlightthickness=5)
        self.main2label1=tk.Label(self.main2frame1, text="Click to play", height=5, font=("Bold", 20), bg="red", fg="black", width=70)
        self.main2label1.pack(padx=10, pady=10)
        self.main2string1=tk.StringVar()
        self.main2string1.set(self.signupentry1.get())
        self.main2frame2=tk.Frame(self.main2, highlightbackground="purple", highlightthickness=3)
        self.main2menu=tk.Menu(self.main2frame2)
        self.main2.config(menu=self.main2menu)
        self.submenu=tk.Menu(self.main2menu, bg="green")
        self.submenu.add_command(label="Account", command=self.gotoaccountdetails)
        self.submenu.add_command(label="Friends", command=self.gotofriends)
        self.submenu.add_command(label="Delete Account", command=self.deleteaccount)
        self.submenu.add_command(label="Log Out", command=self.logout)
        self.main2menu.add_cascade(label=self.main2string1.get(), menu=self.submenu)
        self.main2button1=tk.Button(self.main2, text="Play", height=5, bg="green", width=50, fg="black", font=("Arial", 15), command=lambda:[self.start_timer(), self.gotocheckentryfilled()])
        self.main2button1.place(x=700, y=500)
        self.main2frame1.place(x=400, y=100)
        self.main2frame2.place(x=900, y=900)
        
    
    def gotoaccountdetails(self):
        self.main2.withdraw()
        self.accountdetails=tk.Toplevel(self.main)
        self.accountdetails.geometry("2000x2000")
        self.accountdetails.title("Account Details")
        self.accountdetails.wm_attributes("-fullscreen", True)
        self.accountdetails.configure(bg="aqua")
        self.accountdetailsframe1=tk.Frame(self.accountdetails, highlightbackground="red", highlightthickness=5)
        self.accountdetailslabel1=tk.Label(self.accountdetailsframe1, text="Account Details", width=70, height=5, bg="purple", fg="black", font=("Bold", 20))
        self.accountdetailslabel1.pack(padx=10, pady=10)
        self.accountdetailsframe2=tk.Frame(self.accountdetails, highlightbackground="green", highlightthickness=3)
        self.accountdetailsframe2.columnconfigure(0, weight=1)
        self.accountdetailsframe2.columnconfigure(1, weight=1)
        self.accountdetailslabel2=tk.Label(self.accountdetailsframe2, text="Your Email:", height=5, font=("Arial", 18), fg="black")
        self.accountdetailslabel2.grid(row=0, column=0)
        self.accountdetailsentry1=tk.Entry(self.accountdetailsframe2, width=40, font=("Arial", 16))
        self.accountdetailsentry1.insert(0, self.signupentry2.get())
        self.accountdetailsentry1.grid(row=0, column=1)
        self.accountdetailsentry1.configure(state=tk.DISABLED)
        self.accountdetailsbutton1=tk.Button(self.accountdetails, text="Change Email", height=5, width=15, font=("Arial", 15), bg="blue", fg="black", command=self.gotochange_email)
        self.accountdetailsbutton1.place(x=200, y=700)
        self.accountdetailsframe3=tk.Frame(self.accountdetails, highlightbackground="maroon", highlightthickness=3)
        self.accountdetailsframe3.columnconfigure(0, weight=1)
        self.accountdetailsframe3.columnconfigure(1, weight=1)
        self.accountdetailslabel3=tk.Label(self.accountdetailsframe3, text="Your Password:", height=5, font=("Arial", 18))
        self.accountdetailslabel3.grid(row=0, column=0)
        self.accountdetailsentry2=tk.Entry(self.accountdetailsframe3, width=40, font=("Arial", 16))
        self.accountdetailsentry2.insert(0, self.signupentry3.get())
        self.accountdetailsentry2.grid(row=0, column=1)
        self.accountdetailsentry2.configure(state=tk.DISABLED)
        self.accountdetailsbutton2=tk.Button(self.accountdetails, text="Change Password", height=5, width=15, font=("Arial", 16), bg="red", fg="black", command=self.gotochangepassword)
        self.accountdetailsbutton2.place(x=800, y=700)
        self.accountdetailsframe4=tk.Frame(self.accountdetails, highlightbackground="orange", highlightthickness=3)
        self.accountdetailsframe4.columnconfigure(0, weight=1)
        self.accountdetailsframe4.columnconfigure(0, weight=1)
        self.accountdetailslabel4=tk.Label(self.accountdetailsframe4, text="Your Username:", height=5, font=("Arial", 18))
        self.accountdetailslabel4.grid(row=0, column=0)
        self.accountdetailsentry3=tk.Entry(self.accountdetailsframe4, width=40, font=("Arial", 16))
        self.accountdetailsentry3.insert(0, self.signupentry1.get())
        self.accountdetailsentry3.grid(row=0, column=1)
        self.accountdetailsentry3.configure(state=tk.DISABLED)
        self.accountdetailsbutton3=tk.Button(self.accountdetails, text="Change Username", height=5, width=15, font=("Arial", 15), bg="pink", fg="black", command=self.gotochangeusername)
        self.accountdetailsbutton3.place(x=1500, y=700)
        self.accountdetailsbutton1state=self.accountdetailsbutton1["state"]
        self.accountdetailsbutton2state=self.accountdetailsbutton2["state"]
        self.accountdetailsbutton3state=self.accountdetailsbutton3["state"]
        if self.accountdetailsbutton1state==tk.DISABLED:
            messagebox.showinfo("Cooldown", "You received a cooldown of 14 days for email")
        if self.accountdetailsbutton2state==tk.DISABLED:
            messagebox.showinfo("Cooldown", "You received a cooldown of 14 days for password")
        if self.accountdetailsbutton3state==tk.DISABLED:
            messagebox.showinfo("Cooldown", "You received a cooldown of 14 days for username")
        self.accountdetailsbutton4=tk.Button(self.accountdetails, text="Back", height=5, width=15, font=("Arial", 15), bg="red", fg="black", command=self.close5)
        self.accountdetailsbutton4.place(x=5, y=900)
        self.accountdetailsframe1.place(x=300, y=100)
        self.accountdetailsframe2.place(x=5, y=500)
        self.accountdetailsframe3.place(x=590, y=500)
        self.accountdetailsframe4.place(x=1250, y=500)
       

    def close5(self):
        self.accountdetails.withdraw()
        self.main2.deiconify()
    def gotochange_email(self):
        if hasattr(self, 'change_email') and self.change_email is not None:
            print("Destroying existing change email window")
            self.change_email.destroy()
        self.accountdetails.withdraw()
        self.change_email=tk.Toplevel(self.main)
        self.change_email.geometry("1000x1000")
        self.change_email.title("Change Email")
        self.change_email.configure(bg="aqua")
        self.change_email.wm_attributes("-fullscreen", True)
        self.change_emailframe1=tk.Frame(self.change_email, highlightbackground="red", highlightthickness=5)
        self.change_emaillabel1=tk.Label(self.change_emailframe1, text="Change Email", height=5, width=70, font=("Bold", 20), bg="orange", fg="black")
        self.change_emaillabel1.pack(padx=10, pady=10)
        self.change_emailframe2=tk.Frame(self.change_email, highlightbackground="magenta", highlightthickness=3)
        self.change_emailframe2.columnconfigure(0, weight=1)
        self.change_emailframe2.columnconfigure(1, weight=1)
        self.change_emaillabel2=tk.Label(self.change_emailframe2, text="Your Email", height=5, font=("Arial", 18), fg="black")
        self.change_emaillabel2.grid(row=0, column=0)
        self.change_emailentry1=tk.Entry(self.change_emailframe2, width=40, font=("Arial", 16))
        self.change_emailentry1.insert(0, self.signupentry2.get())
        self.change_emailentry1.grid(row=0, column=1)
        self.change_emailbutton1=tk.Button(self.change_email, text="Submit Change", height=5, width=15, font=("Arial", 15), fg="black", bg="green", command=self.gotoafteremailchanged)
        self.change_emailbutton1.place(x=900, y=800)
        self.change_emailbutton2=tk.Button(self.change_email, text="Back", height=5, width=15, font=("Arial", 15), bg="red", fg="black", command=self.close6)
        self.change_emailbutton2.place(x=50, y=900)
        self.change_emailframe1.place(x=400, y=100)
        self.change_emailframe2.place(x=700, y=500)
        
    
    def close6(self):
        self.change_email.withdraw()
        self.accountdetails.deiconify()
    
    def gotoafteremailchanged(self):
        if not (self.change_emailentry1.get().endswith("@hotmail.com") or self.change_emailentry1.get().endswith("@gmail.com")):
            messagebox.showerror("Error", "Email must include @hotmail.com or gmail.com")
        
        elif self.change_emailentry1.get()==self.signupentry2.get():
            messagebox.showerror("Error", "You have not changed your email")
        
        elif self.change_emailentry1 in self.userinfo1:
            messagebox.showerror("Error", "Email already Taken")
        
        else:
                self.userinfo1[self.change_emailentry1.get()]=self.userinfo1.pop(self.signupentry2.get())
                self.userinfo2[self.change_emailentry1.get()]=self.userinfo2.pop(self.signupentry2.get())
                self.signupentry2.delete(0, tk.END)
                self.signupentry2.insert(0, self.change_emailentry1.get())
                print(self.userinfo2[self.change_emailentry1.get()], "has changed Email to:", self.change_emailentry1.get())
                self.change_email.withdraw()
                self.gotoaccountdetails()
                self.startemailcooldown()
           

    def startemailcooldown(self):
        self.change_emailbutton1.configure(state=tk.DISABLED)
        self.change_emailentry1.configure(state=tk.DISABLED)
        self.change_email.update_idletasks()
        print(f"Button state after: {self.change_emailbutton1.cget('state')}")
        print(f"Entry state after: {self.change_emailentry1.cget('state')}")
        self.change_email.after(5000, self.endemailcooldown)
        

         
   
    
    def endemailcooldown(self):
        print(f"Button ID: {id(self.change_emailbutton1)}")
        print(f"Entry ID: {id(self.change_emailentry1)}")
        print(f"Button state before enabling: {self.change_emailbutton1.cget('state')}")
        print(f"Entry state before enabling: {self.change_emailentry1.cget('state')}")
        self.change_emailbutton1.configure(state=tk.NORMAL)
        self.change_emailentry1.configure(state=tk.NORMAL)
        self.change_email.update_idletasks()
    
    def gotochangepassword(self):
        self.changepassword=tk.Toplevel(self.main)
        self.changepassword.geometry("1000x1000")
        self.changepassword.title("Change Password")
        self.changepassword.configure(bg="aqua")
        self.changepassword.wm_attributes("-fullscreen", True)
        self.changepasswordframe1=tk.Frame(self.changepassword, highlightbackground="red", highlightthickness=5)
        self.changepasswordlabel1=tk.Label(self.changepasswordframe1, text="Change Password", height=5, width=70, bg="orange", fg="black", font=("Bold", 20))
        self.changepasswordlabel1.pack(padx=10, pady=10)
        self.changepasswordframe2=tk.Frame(self.changepassword, highlightbackground="green", highlightthickness=3)
        self.changepasswordframe2.columnconfigure(0, weight=1)
        self.changepasswordframe2.columnconfigure(1, weight=1)
        self.changepasswordlabel2=tk.Label(self.changepasswordframe2, text="Your Password", height=5, font=("Arial", 18), fg="black")
        self.changepasswordlabel2.grid(row=0, column=0)
        self.changepasswordentry1=tk.Entry(self.changepasswordframe2, font=("Arial", 16))
        self.changepasswordentry1.insert(0, self.signupentry3.get())
        self.changepasswordentry1.grid(row=0, column=1)
        self.changepasswordbutton1=tk.Button(self.changepassword, text="Submit Change", height=5, width=15, font=("Arial", 15), fg="black", bg="green", command=self.gotoafterpasswordchanged)
        self.changepasswordbutton1.place(x=900, y=800)
        self.changepasswordbutton2=tk.Button(self.changepassword, text="Back", height=5, width=15, font=("Arial", 15), fg="black", bg="red", command=self.close7)
        self.changepasswordbutton2.place(x=50, y=900)
        self.changepasswordframe1.place(x=400, y=100)
        self.changepasswordframe2.place(x=700, y=500)
        
    
    def close7(self):
        self.changepassword.withdraw()
        self.accountdetails.deiconify()

    def gotoafterpasswordchanged(self):
        if self.changepasswordentry1.get()==self.signupentry3.get():
            messagebox.showerror("Error", "You have not changed your password")
        else:
            self.userinfo1[self.change_emailentry1.get()]=self.changepasswordentry1.get()
            print(self.userinfo2[self.signupentry2.get()], "has changed password to", self.changepasswordentry1.get())
            self.signupentry3.delete(0, tk.END)
            self.signupentry3.insert(0, self.changepasswordentry1.get())
            self.changepassword.withdraw()
            self.gotoaccountdetails()

    def gotochangeusername(self):
        self.accountdetails.withdraw()
        self.changeusername=tk.Toplevel(self.main)
        self.changeusername.geometry("1000x1000")
        self.changeusername.title("Change Username")
        self.changeusername.wm_attributes("-fullscreen", True)
        self.changeusernameframe1=tk.Frame(self.changeusername, highlightbackground="red", highlightthickness=5)
        self.changeusernamelabel1=tk.Label(self.changeusernameframe1, text="Change Username", height=5, width=70, font=("Bold", 20), bg="purple", fg="black")
        self.changeusernamelabel1.pack(padx=10, pady=10)
        self.changeusernameframe2=tk.Frame(self.changeusername, highlightbackground="green", highlightthickness=3)
        self.changeusernamelabel2=tk.Label(self.changeusernameframe2, text="Your Username", height=5, font=("Arial", 18), fg="black")
        self.changeusernamelabel2.grid(row=0, column=0)
        self.changeusernameentry1=tk.Entry(self.changeusernameframe2, width=40, font=("Arial", 16))
        self.changeusernameentry1.insert(0, self.signupentry1.get())
        self.changeusernameentry1.grid(row=0, column=1)
        self.changeusernamebutton1=tk.Button(self.changeusernameframe2, text="Submit Change", height=5, width=15, font=("Arial", 15), bg="green", fg="black", command=self.gotoafterusernamechanged)
        self.changeusernamebutton1.place(x=900, y=800)
        self.changeusernamebutton2=tk.Button(self.changeusername, text="Back", height=5, width=15, font=("Arial", 15), bg="red", fg="black", command=self.close8)
        self.changeusernamebutton2.place(x=50, y=900)
        self.changeusernameframe1.place(x=400, y=100)
        self.changeusernameframe2.place(x=700, y=500)
        
    
    def close8(self):
        self.changeusername.withdraw()
        self.accountdetails.deiconify()
    
    def gotoafterusernamechanged(self):
        if self.changeusernameentry1.get()==self.signupentry1.get():
            messagebox.showerror("Error", "You have not changed your username")
        elif self.changeusernameentry1.get() in self.userinfo2:
            messagebox.showerror("Error", "Username already taken")
        else:
            self.userinfo2[self.change_emailentry1.get()]=self.changeusernameentry1.get()
            print(self.signupentry1.get(), "has changed username to", self.userinfo2[self.change_emailentry1.get()])
            self.signupentry1.delete(0, tk.END)
            self.signupentry1.insert(0, self.changeusernameentry1.get())
            self.changeusername.withdraw()
            self.gotoaccountdetails()
        
        

        

    def logout(self):
        self.main2.withdraw()
        self.__init__()
        print(self.userinfo2[self.signupentry2.get()], "has logged out")
    
    def deleteaccount(self):
        self.main2.withdraw()
        print(self.userinfo2[self.signupentry2.get()], "account has been deleted")
        del self.userinfo1[self.signupentry2.get()]
        del self.userinfo2[self.signupentry2.get()]
        self.__init__()

    def gotofriends(self):
        self.friendrequests_sent={}
        self.friendrequests_sent[self.userinfo2[self.signupentry2.get()]]=[]
        self.friendrequests_received={}
        self.friendrequests_received[self.userinfo2[self.signupentry2.get()]]=[]
        self.main2.withdraw()
        self.friends=tk.Toplevel(self.main)
        self.friends.geometry("1000x1000")
        self.friends.title("Friends")
        self.friends.wm_attributes("-fullscreen", True)
        self.friendsframe1=tk.Frame(self.friends, highlightbackground="red", highlightthickness=5)
        self.friendslabel1=tk.Label(self.friendsframe1, text="Friends", height=5, width=70, font=("Bold", 20), bg="green", fg="black")
        self.friendslabel1.pack(padx=10, pady=10)
        self.friendsframe2=tk.Frame(self.friends, highlightbackground="purple", highlightthickness=3)
        self.friendsframe2.rowconfigure(0, weight=1)
        self.friendsframe2.rowconfigure(1, weight=1)
        self.friendslabel2=tk.Label(self.friendsframe2, text="Friend Requests Sent", height=5, width=50, font=("Arial", 18), fg="black")
        self.friendslabel2.grid(row=0, column=0)
        self.friendslistbox1=tk.Listbox(self.friendsframe2, height=5)
        self.friendslistbox1.grid(row=1, column=0)
        self.friendsframe3=tk.Frame(self.friends, highlightbackground="green", height=3)
        self.friendsframe3.rowconfigure(0, weight=1)
        self.friendsframe3.rowconfigure(1, weight=1)
        self.friendsframe3.rowconfigure(2, weight=1)
        self.friendslabel4=tk.Label(self.friendsframe3, text="Send a Friend Request", height=5, width=50, font=("Arial", 18), fg="black")
        self.friendslabel4.grid(row=0, column=0)
        self.friendsentry1=tk.Entry(self.friendsframe3, font=("Arial", 15), width=60)
        self.friendsentry1.insert(0, "")
        self.friendsentry1.grid(row=1, column=0)
        self.friendsbutton1=tk.Button(self.friendsframe3, text="Enter", height=5, width=15, font=("Arial", 15), bg="green", fg="black", command=self.sendfriendrequest)
        self.friendsbutton1.grid(row=2, column=0)
        self.friendsframe4=tk.Frame(self.friends, highlightbackground="yellow", highlightthickness=3)
        self.friendsframe4.rowconfigure(0, weight=1)
        self.friendsframe4.rowconfigure(1, weight=1)
        self.friendslabel3=tk.Label(self.friendsframe4, text="Friend Requests Recieved", height=5, width=50, font=("Arial", 18), bg="black")
        self.friendslabel3.grid(row=0, column=0)
        self.friendslistbox2=tk.Listbox(self.friendsframe4, height=5)
        self.friendslistbox2.grid(row=1, column=0)
        self.friendsframe1.place(x=300, y=100)
        self.friendsframe2.place(x=100, y=300)
        self.friendsframe3.place(x=400, y=300)
        self.friendsframe3.place(x=300, y=600)
    
    def sendfriendrequest(self):
        self.selecteditem=self.friendslistbox1.get(tk.ACTIVE)
        if not (self.friendsentry1.get()):
            messagebox.showerror("Error", "You have not typed anything")
        elif self.friendsentry1.get()==self.userinfo1[self.signupentry2.get()]:
            messagebox.showerror("Error", "You can't send a friend request to yourself")
        elif not (self.friendsentry1.get() in self.userinfo1):
            messagebox.showerror("Error", "The username that you have put in does not exist")
        elif self.friendsentry1.get() in self.selecteditem:
            messagebox.showerror("Error", "You already sent a friend request to that username")
        else:
            self.friendslistbox1.insert(tk.END, self.friendsentry1.get())

        


       

    def gotologin(self):
        self.signuporlogin.withdraw()
        self.login=tk.Toplevel(self.main)
        self.login.geometry("1000x1000")
        self.login.title("Log In")
        self.login.configure(bg="aqua")
        self.login.wm_attributes("-fullscreen", True)
        self.loginframe1=tk.Frame(self.login, highlightcolor="purple", highlightthickness=5)
        self.loginlabel1=tk.Label(self.loginframe1, text="Log In", height=5, font=("Bold", 20), bg="green", fg="black", width=70)
        self.loginlabel1.pack(padx=10, pady=10)
        self.loginframe2=tk.Frame(self.login, highlightcolor="green", highlightthickness=3)
        self.loginframe2.columnconfigure(0, weight=1)
        self.loginframe2.columnconfigure(1, weight=1)
        self.loginlabel2=tk.Label(self.loginframe2, text="Email:", height=5, font=("Arial", 18), fg="black")
        self.loginlabel2.grid(row=0, column=0)
        self.loginentry1=tk.Entry(self.loginframe2, width=100, font=("Arial", 20))
        self.loginentry1.insert(0, "")
        self.loginentry1.grid(row=0, column=1)
        self.loginlabel3=tk.Label(self.loginframe2, text="Password:", height=5, font=("Arial", 18), fg="black")
        self.loginlabel3.grid(row=1, column=0)
        self.loginentry2=tk.Entry(self.loginframe2, width=100, font=("Arial", 20))
        self.loginentry2.insert(0, "")
        self.loginentry2.grid(row=1, column=1)
        self.loginbutton1=tk.Button(self.login, text="Log In", height=5, width=50, font=("Arial", 15), bg="green", fg="black", command=self.loginfinished)
        self.loginbutton1.place(x=625, y=800)
        self.loginframe1.place(x=400, y=100)
        self.loginframe2.place(x=200, y=300)
        self.loginbutton2=tk.Button(self.login, text="Back", height=5, width=20, font=("Arial", 15), bg="red", fg="black", command=self.close4)
        self.loginbutton2.place(x=25, y=900)
        self.login.mainloop()
    
    def close4(self):
        self.login.destroy()
        self.signuporlogin.deiconify()
    
    def loginfinished(self):
        
        if not(self.loginentry1.get() and self.loginentry2.get()):
            messagebox.showerror("Error", "Please fill all")
        elif not(self.loginentry1.get().endswith("@hotmail.com") or self.loginentry1.get().endswith("@gmail.com")):
            messagebox.showerror("Error", "Please include @hotmail.com or @gmail.com at the end of your Email")
        elif not(self.loginentry1.get() in self.userinfo1):
            messagebox.showerror("Error", "Email does not exist")
        else:
            if self.loginentry2.get()==self.userinfo1[self.loginentry1.get()]:
                print(self.userinfo2[self.loginentry1.get()], "has logged in")
                print(self.userinfo2[self.loginentry1.get()], "Email:", self.loginentry1.get())
                print(self.userinfo2[self.loginentry1.get()], "Password:", self.userinfo1[self.loginentry1.get()])
                self.login.withdraw()
                self.Home2()
            else:
                messagebox.showerror("Error", "Incorrect Password")


    
           


    def gotocheckentryfilled(self):
            global i
            if i<1:
                self.highestscore=0
                i=i+1
            self.main2.withdraw()
            self.colorgame=tk.Toplevel(self.main)
            self.colorgame.geometry("1000x1000")
            self.colorgame.title("Color Game")
            self.colorgame.configure(bg="aqua")
            self.colorgame.wm_attributes("-fullscreen", True)
            self.colorgameframe1=tk.Frame(self.colorgame, highlightbackground="blue", highlightthickness=5)
            self.colorgamelabel1=tk.Label(self.colorgameframe1, text="Which Color?", height=4, width=70, font=("Bold", 20), bg="navy blue", fg="black")
            self.colorgamelabel1.pack(padx=10, pady=10)
            self.scoreframe=tk.Frame(self.colorgame)
            self.score=0
            self.scorelabel=tk.Label(self.colorgame, text=f"Score: {self.score}", height=3, font=("Arial", 15), fg="black", bg="green", width=20)
            self.scorelabel.place(x=750, y=300)
            self.highestscorelabel=tk.Label(self.colorgame, text=f"Highest Score: {self.highestscore}", height=3, font=("Arial", 15), fg="black", bg="red", width=20)
            self.highestscorelabel.place(x=750, y=200)
            self.colors=["red", "green", "yellow", "blue", "black", "purple", "gray", "orange", "pink", "brown"]
            self.colorsrandom1=random.choice(self.colors)
            self.colorsrandom2=random.choice(self.colors)
            self.colorgamedisplaylabel1=tk.Label(self.colorgame, text=self.colorsrandom1, height=5, font=("Arial", 20), fg=self.colorsrandom2, width=25)
            self.colorgamedisplaylabel1.place(x=670, y=600)
            self.colorgameframe2=tk.Frame(self.colorgame)
            self.colorgameframe2.columnconfigure(0, weight=1)
            self.colorgameframe2.columnconfigure(1, weight=1)
            self.colorgameentry1=tk.Entry(self.colorgameframe2, font=("Arial", 20))
            self.colorgameentry1.insert(0, "")
            self.colorgameentry1.grid(row=0, column=0)
            self.colorgamebutton1=tk.Button(self.colorgameframe2, text="Enter", height=3, font=("Arial", 15), fg="black", bg="green", command=self.receivepoints)
            self.colorgamebutton1.grid(row=0, column=1)
            self.displaytimer=tk.Label(self.colorgame, text=f"Timer: 60 seconds", height=3, width=25, font=("Arial", 17), fg="black", bg="blue")
            self.displaytimer.place(x=700, y=450)
            self.colorgameframe1.place(x=300, y=25)
            self.colorgameframe2.place(x=680, y=800)
            

        
    def receivepoints(self):
        if not(self.colorgameentry1.get()):
            messagebox.showerror("Error", "Please type in a color name")

        elif self.colorgameentry1.get()==self.colorsrandom2:
            self.score=self.score+100
            self.scorelabel.configure(text=f"Score: {self.score}")
            self.colorgameentry1.delete(0, tk.END)
            self.colorsrandom1=random.choice(self.colors)
            self.colorsrandom2=random.choice(self.colors)
            self.colorgamedisplaylabel1.configure(text=self.colorsrandom1, fg=self.colorsrandom2)
        else:
            self.scorelabel.configure(text=f"Score: {self.score}")
            self.colorgameentry1.delete(0, tk.END)
            self.colorsrandom1=random.choice(self.colors)
            self.colorsrandom2=random.choice(self.colors)
            self.colorgamedisplaylabel1.configure(text=self.colorsrandom1, fg=self.colorsrandom2)

            

            
    
    def start_timer(self):
        self.seconds=60
        self.update_timer()
    
    def update_timer(self):
        self.displaytimer.configure(text=f"Timer: {self.seconds}")
        if self.seconds==0:
           self.gotostartover()
            
        else:
            self.seconds=self.seconds-1
            self.colorgame.after(1000, self.update_timer)
            
    def gotostartover(self):
        self.colorgame.withdraw()
        if self.score>self.highestscore:
            self.highestscore=self.score
            self.highestscorelabel.configure(text=f"Highest Score: {self.highestscore}")
        self.startover=tk.Toplevel(self.main)
        self.startover.geometry("1000x1000")
        self.startover.title("Start Over")
        self.startover.configure(bg="aqua")
        self.startover.wm_attributes("-fullscreen", True)
        self.startoverframe1=tk.Frame(self.startover, highlightbackground="maroon", highlightthickness=5)
        self.startoverlabel1=tk.Label(self.startoverframe1, text="Start Over", height=5, font=("Bold", 20), fg="black", bg="green", width=70)
        self.startoverlabel1.pack(padx=10, pady=10)
        self.displayhighestscore=tk.Label(self.startover, text=f"Highest Score: {self.highestscore}", height=3, font=("Arial", 13), fg="black", width=30, bg="purple")
        self.displayhighestscore.place(x=800, y=400)
        self.displayfinalscore=tk.Label(self.startover, text=f"Score: {self.score}", height=3, font=("Arial", 18), fg="black", width=30, bg="orange")
        self.displayfinalscore.place(x=750, y=500)
        self.startoverbutton1=tk.Button(self.startover, text="Play Again", height=5, command=lambda:[self.start_timer(), self.gotocheckentryfilled()], width=50, bg="green")
        self.startoverbutton1.place(x=780, y=700)
        self.startoverbutton2=tk.Button(self.startover, text="Rate Us", height=5, command=self.gotorateus, width=50, bg="yellow")
        self.startoverbutton2.place(x=780, y=800)
        self.startoverframe1.place(x=400, y=100)
       
    def gotorateus(self):
        self.startover.withdraw()
        self.rateus=tk.Toplevel(self.main)
        self.rateus.geometry("1000x1000")
        self.rateus.title("Rate Us")
        self.rateus.configure(bg="aqua")
        self.rateus.wm_attributes("-fullscreen", True)
        self.rateusframe1=tk.Frame(self.rateus, highlightbackground="purple", highlightthickness=5)
        self.rateuslabel1=tk.Label(self.rateusframe1, text="Rate Us", height=5, font=("Bold", 20), bg="green", fg="black")
        self.rateuslabel1.pack(padx=10, pady=10)
        self.rateusframe2=tk.Frame(self.rateus, highlightbackground="green", highlightthickness=5)
        self.rateusframe2.columnconfigure(0, weight=1)
        self.rateusframe2.columnconfigure(1, weight=1)
        self.rateusframe2.columnconfigure(2, weight=1)
        self.rateusframe2.columnconfigure(3, weight=1)
        self.rateusframe2.columnconfigure(4, weight=1)
        self.rateusframe2.columnconfigure(5, weight=1)
        self.rateuslabel2=tk.Label(self.rateusframe2, text="From 1-5, how much did you enjoy using this application?", height=5, font=("Arial", 18), fg="black")
        self.rateuslabel2.grid(row=0, column=0)
        self.checkvar1=tk.BooleanVar()
        self.checkvar2=tk.BooleanVar()
        self.checkvar3=tk.BooleanVar()
        self.checkvar4=tk.BooleanVar()
        self.checkvar5=tk.BooleanVar()
        self.rateuscheckbutton1=tk.Checkbutton(self.rateusframe2, text="1", height=5, variable=self.checkvar1, command=self.toggle1)
        self.rateuscheckbutton1.grid(row=0, column=1)
        self.rateuscheckbutton2=tk.Checkbutton(self.rateusframe2, text="2", height=5, variable=self.checkvar2, command=self.toggle2)
        self.rateuscheckbutton2.grid(row=0, column=2)
        self.rateuscheckbutton3=tk.Checkbutton(self.rateusframe2, text="3", height=5, variable=self.checkvar3, command=self.toggle3)
        self.rateuscheckbutton3.grid(row=0, column=3)
        self.rateuscheckbutton4=tk.Checkbutton(self.rateusframe2, text="4", height=5, variable=self.checkvar4, command=self.toggle4)
        self.rateuscheckbutton4.grid(row=0, column=4)
        self.rateuscheckbutton5=tk.Checkbutton(self.rateusframe2, text="5", height=5, variable=self.checkvar5, command=self.toggle5)
        self.rateuscheckbutton5.grid(row=0, column=5)
        self.rateuslabel3=tk.Label(self.rateusframe2, text="Provide feeback", height=5, font=("Arial", 18), fg="black")
        self.rateuslabel3.grid(row=1, column=0)
        self.rateustextbox1=tk.Text(self.rateusframe2, height=10, width=15, font=("Arial", 15), fg="black")
        self.rateustextbox1.grid(row=1, column=1)
        self.rateusbutton1=tk.Button(self.rateus, text="Submit", height=5, font=("Arial", 15), bg="green", fg="black", command=self.gotofinishedrateus)
        self.state=self.rateusbutton1["state"]
        if self.state==tk.DISABLED:
            messagebox.showinfo("24 Day Cooldown", "Please wait for 24 days until you recieve a new form request")
        self.rateusbutton1.place(x=500, y=500)
        self.rateusframe1.place(x=500, y=100)
        self.rateusframe2.place(x=500, y=300)
        
    
    def toggle1(self):
        self.rateuscheckbutton2.deselect()
        self.rateuscheckbutton3.deselect()
        self.rateuscheckbutton4.deselect()
        self.rateuscheckbutton5.deselect()
    def toggle2(self):
        self.rateuscheckbutton1.deselect()
        self.rateuscheckbutton3.deselect()
        self.rateuscheckbutton4.deselect()
        self.rateuscheckbutton5.deselect()
    def toggle3(self):
        self.rateuscheckbutton1.deselect()
        self.rateuscheckbutton2.deselect()
        self.rateuscheckbutton4.deselect()
        self.rateuscheckbutton5.deselect()
    def toggle4(self):
        self.rateuscheckbutton1.deselect()
        self.rateuscheckbutton2.deselect()
        self.rateuscheckbutton3.deselect()
        self.rateuscheckbutton5.deselect()
    def toggle5(self):
        self.rateuscheckbutton1.deselect()
        self.rateuscheckbutton2.deselect()
        self.rateuscheckbutton3.deselect()
        self.rateuscheckbutton4.deselect()
    
    def rateusstartcooldown(self):
        print(self.userinfo2[self.signupentry2.get()], "has received a cooldown(24 hours) for the rate us button")
        self.rateusbutton1.configure(state=tk.DISABLED)
        self.rateus.after(2073600000, self.rateusendcooldown)
    
    def rateusendcooldown(self):
        print(self.userinfo2[self.signupentry2.get()], "cooldown for the rate us button has ended")
        self.rateusbutton1.configure(state=tk.NORMAL)
    
    def gotofinishedrateus(self):
        if self.checkvar1.get() or self.checkvar2.get() or self.checkvar3.get() or self.checkvar4.get() or self.checkvar5.get() and self.rateustextbox1.get(1.0, tk.END):
            self.rateus.withdraw()
            self.finishedrateus=tk.Toplevel(self.main)
            self.finishedrateus.geometry("1000x1000")
            self.finishedrateus.title("Rate Us Finished")
            self.finishedrateus.configure(bg="aqua")
            self.finishedrateus.wm_attributes("-fullscreen", True)
            self.finishedrateusframe1=tk.Frame(self.finishedrateus, highlightbackground="pink", highlightthickness=5)
            self.finishedrateuslabel1=tk.Label(self.finishedrateusframe1, text="Thank you for rating us!", height=5, font=("Bold", 20), bg="yellow", fg="black")
            self.finishedrateuslabel1.pack(padx=10, pady=10)
            self.finishedrateusframe2=tk.Frame(self.finishedrateus)
            self.finishedrateusframe2.columnconfigure(0, weight=1)
            self.finishedrateusframe2.columnconfigure(1, weight=1)
            self.finishedrateusbutton1=tk.Button(self.finishedrateusframe2, text="Home", height=5, font=("Arial", 15), bg="green", fg="black", command=self.close2)
            self.finishedrateusbutton1.grid(row=0, column=0)
            self.finishedrateusbutton2=tk.Button(self.finishedrateusframe2, text="CLOSE", height=5, font=("Arial", 15), bg="red", fg="black", command=self.destroyfinishedrateus)
            self.finishedrateusbutton2.grid(row=0, column=1)
            self.finishedrateusframe1.place(x=500, y=900)
            self.finishedrateusframe2.place(x=500, y=500)
            if self.checkvar1.get():
                print("User Rating(out of 5): 1")
            elif self.checkvar2:
                print("User Rating(out of 5): 2")
            elif self.checkvar3.get():
                print("User Rating(out of 5): 3")
            elif self.checkvar4.get():
                print("User Rating(out of 5): 4")
            else:
                print("User Rating(out of 5): 5")
            print("User Feedback:", self.rateustextbox1.get(1.0, tk.END))
            
        else:
            messagebox.showerror("Error", "Please fill all")
    def destroyfinishedrateus(self):
        self.finishedrateus.destroy()
    def close2(self):
        self.finishedrateus.withdraw()
        self.main2.deiconify()
    
GUI()

            



        
        
       

    
    



        
