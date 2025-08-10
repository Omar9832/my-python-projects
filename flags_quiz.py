import tkinter as tk
import random as rm
import tkinter.messagebox as messagebox



class GUI:

    
    def __init__(self):
        self.countries=[
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", 
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", 
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", 
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Congo (Democratic Republic)", 
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", 
    "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", 
    "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", 
    "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", 
    "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", 
    "Kenya", "Kiribati", "Korea (North)", "Korea (South)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", 
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", 
    "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", 
    "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", 
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", 
    "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", 
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", 
    "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", 
    "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", 
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]
        self.points=0
        self.home=tk.Tk()
        self.home.geometry("500x500")
        self.home.attributes("-fullscreen", True)
        self.home.title("Home")
        self.homebackround=tk.PhotoImage(file="Colorful.png")
        self.homebackroundlabel=tk.Label(self.home, image=self.homebackround)
        self.homebackroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.homeheader=tk.Label(self.home, text="Flags Quiz", height=2, width=40, bg="green", fg="black", font=("Helvetica", 20))
        self.homeheader.place(x=636, y=50)
        self.homeplaybuttonbackround=tk.PhotoImage(file="play.png")
        self.homeplaybutton=tk.Button(self.home, image=self.homeplaybuttonbackround, height=80, width=150, command=self.gotoquestion1)
        self.homeplaybutton.place(x=880, y=500)
        self.homeclosebutton=tk.Button(self.home, text="CLOSE", bg="yellow", fg="black", font=("Helvetica", 15), height=5, width=10, command=self.closehome)
        self.homeclosebutton.place(x=900, y=800)
        self.home.mainloop()
    def closehome(self):
        self.home.destroy()
    
    def gotoquestion1(self):
        self.America=tk.PhotoImage(file="America.png")
        self.Spain=tk.PhotoImage(file="Spain.png")
        self.France=tk.PhotoImage(file="France.png")
        self.Germany=tk.PhotoImage(file="Germany.png")
        self.Romania=tk.PhotoImage(file="Romania.png")
        self.Serbia=tk.PhotoImage(file="Serbia.png")
        self.flagslist1=[self.America, self.Spain, self.France, self.Germany, self.Romania, self.Serbia]
        self.flagslist1names=["America", "Spain", "France", "Germany", "Romania", "Serbia"]
        self.randomflag1=rm.choice(self.flagslist1)
        self.random_index=self.flagslist1.index(self.randomflag1)
        self.home.withdraw()
        self.question1=tk.Toplevel(self.home)
        self.question1.attributes("-fullscreen", True)
        self.question1.title("Question 1")
        self.question1.geometry("1000x1000")
        self.question1backround=tk.PhotoImage(file="nice.png")
        self.question1backroundlabel=tk.Label(self.question1, image=self.question1backround)
        self.question1backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.question1label=tk.Label(self.question1, text="Guess the Flag", height=2, width=37, bg="purple", fg="black", font=("Helvetica", 20))
        self.question1label.pack(padx=10, pady=10)
        self.question1scorelabel=tk.Label(self.question1, text=f"Score: {self.points}", height=2, width=10, font=("Helvetica", 15), bg="blue", fg="black")
        self.question1scorelabel.place(x=1140, y=30)
        self.randomflag1label=tk.Label(self.question1, image=self.randomflag1)
        self.randomflag1label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.numbers=[1, 2, 3, 4]
        self.randomnumber=rm.choice(self.numbers)
        self.newcountrieslist1=[]
        self.newcountrieslist1=[country for country in self.countries if country != self.flagslist1names[self.random_index]]

        self.randomcountryname1=rm.choice(self.newcountrieslist1)
        self.randomcountryname2=rm.choice(self.newcountrieslist1)
        self.randomcountryname3=rm.choice(self.newcountrieslist1)
        if self.randomnumber==1:
            self.question1button1=tk.Button(self.question1, text=self.flagslist1names[self.random_index], height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion2(self.flagslist1names[self.random_index]))
            self.question1button1.pack(padx=10, pady=10)
            self.question1button2=tk.Button(self.question1, text=self.randomcountryname1, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion2(self.randomcountryname1))
            self.question1button2.pack(padx=10, pady=10)
            self.question1button3=tk.Button(self.question1, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname2))
            self.question1button3.pack(padx=10, pady=10)
            self.question1button4=tk.Button(self.question1, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname3))
            self.question1button4.pack(padx=10, pady=10)
        elif self.randomnumber==2:
            self.question1button1=tk.Button(self.question1, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname1))
            self.question1button1.pack(padx=10, pady=10)
            self.question1button2=tk.Button(self.question1, text=self.flagslist1names[self.random_index], height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion2(self.flagslist1names[self.random_index]))
            self.question1button2.pack(padx=10, pady=10)
            self.question1button3=tk.Button(self.question1, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname2))
            self.question1button3.pack(padx=10, pady=10)
            self.question1button4=tk.Button(self.question1, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname3))
            self.question1button4.pack(padx=10, pady=10)
        elif self.randomnumber==3:
            self.question1button1=tk.Button(self.question1, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname1))
            self.question1button1.pack(padx=10, pady=10)
            self.question1button2=tk.Button(self.question1, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion2(self.randomcountryname2))
            self.question1button2.pack(padx=10, pady=10)
            self.question1button3=tk.Button(self.question1, text=self.flagslist1names[self.random_index], height=2, font=("Arial", 15), bg=bcolor3, fg=fcolor3, width=40, command=lambda:self.gotoquestion2(self.flagslist1names[self.random_index]))
            self.question1button3.pack(padx=10, pady=10)
            self.question1button4=tk.Button(self.question1, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname3))
            self.question1button4.pack(padx=10, pady=10)
        else:
            self.question1button1=tk.Button(self.question1, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname1))
            self.question1button1.pack(padx=10, pady=10)
            self.question1button2=tk.Button(self.question1, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion2(self.randomcountryname2))
            self.question1button2.pack(padx=10, pady=10)
            self.question1button3=tk.Button(self.question1, text=self.randomcountryname3, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion2(self.randomcountryname3))
            self.question1button3.pack(padx=10, pady=10)
            self.question1button4=tk.Button(self.question1, text=self.flagslist1names[self.random_index], height=2, font=("Arial", 15), bg=bcolor4, fg=fcolor4, width=40, command=lambda:self.gotoquestion2(self.flagslist1names[self.random_index]))
            self.question1button4.pack(padx=10, pady=10)


        

        self.question1button1.bind("<Enter>", lambda event:self.on_enter1(event, bcolor1, fcolor1))
        self.question1button1.bind("<Leave>", lambda event:self.on_leave1(event, bcolor1, fcolor1))
        self.question1button2.bind("<Enter>", lambda event:self.on_enter2(event, bcolor2, fcolor2))
        self.question1button2.bind("<Leave>", lambda event:self.on_leave2(event, bcolor2, fcolor2))
        self.question1button3.bind("<Enter>", lambda event:self.on_enter3(event, bcolor3, fcolor3))
        self.question1button3.bind("<Leave>", lambda event:self.on_leave3(event, bcolor3, fcolor3))
        self.question1button4.bind("<Enter>", lambda event:self.on_enter4(event, bcolor4, fcolor4))
        self.question1button4.bind("<Leave>", lambda event:self.on_leave4(event, bcolor4, fcolor4))
        self.question1.mainloop()
        
    def on_enter1(self, event, bcolor1, fcolor1):
        self.question1button1["background"]=fcolor1
        self.question1button1["foreground"]=bcolor1
    def on_leave1(self, event, bcolor1, fcolor1):
        self.question1button1["background"]=bcolor1
        self.question1button1["foreground"]=fcolor1
    def on_enter2(self, event, bcolor2, fcolor2):
        self.question1button2["background"]=fcolor2
        self.question1button2["foreground"]=bcolor2
    def on_leave2(self, event, bcolor2, fcolor2):
        self.question1button2["background"]=bcolor2
        self.question1button2["foreground"]=fcolor2
    def on_enter3(self, event, bcolor3, fcolor3):
        self.question1button3["background"]=fcolor3
        self.question1button3["foreground"]=bcolor3
    def on_leave3(self, event, bcolor3, fcolor3):
        self.question1button3["background"]=bcolor3
        self.question1button3["foreground"]=fcolor3
    def on_enter4(self, event, bcolor4, fcolor4):
        self.question1button4["background"]=fcolor4
        self.question1button4["foreground"]=bcolor4
    def on_leave4(self, event, bcolor4, fcolor4):
        self.question1button4["background"]=bcolor4
        self.question1button4["foreground"]=fcolor4

    def gotoquestion2(self, userchoice1):
        if userchoice1==self.flagslist1names[self.random_index]:
            self.points=self.points+100
        self.Russia=tk.PhotoImage(file="Russia.png")
        self.Poland=tk.PhotoImage(file="Poland.png")
        self.Italy=tk.PhotoImage(file="Italy.png")
        self.Brazil=tk.PhotoImage(file="Brazil.png")
        self.Netherlands=tk.PhotoImage(file="Netherlands.png")
        self.Lithuania=tk.PhotoImage(file="Lithuania.png")
        self.flagslist2=[self.Russia, self.Poland, self.Italy, self.Brazil, self.Netherlands, self.Lithuania]
        self.flagslist2names=["Russia", "Poland", "Italy", "Brazil", "Netherlands", "Lithuania"]
        self.randomflag2=rm.choice(self.flagslist2)
        self.random_index=self.flagslist2.index(self.randomflag2)
        self.question1.withdraw()
        self.question2=tk.Toplevel(self.home)
        self.question2.attributes("-fullscreen", True)
        self.question2.title("Question 2")
        self.question2.geometry("1000x1000")
        self.question2backround=tk.PhotoImage(file="nice.png")
        self.question2backroundlabel=tk.Label(self.question2, image=self.question2backround)
        self.question2backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.question2label=tk.Label(self.question2, text="Guess the Flag", height=2, width=37, bg="purple", fg="black", font=("Helvetica", 20))
        self.question2label.pack(padx=10, pady=10)
        self.question2scorelabel=tk.Label(self.question2, text=f"Score: {self.points}", height=2, width=10, font=("Helvetica", 15), bg="blue", fg="black")
        self.question2scorelabel.place(x=1140, y=30)
        self.randomflag2label=tk.Label(self.question2, image=self.randomflag2)
        self.randomflag2label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.numbers=[1, 2, 3, 4]
        self.randomnumber=rm.choice(self.numbers)
        self.newcountrieslist2=[]
        self.newcountrieslist2=[country for country in self.countries if country != self.flagslist2names[self.random_index]]

        self.randomcountryname1=rm.choice(self.newcountrieslist2)
        self.randomcountryname2=rm.choice(self.newcountrieslist2)
        self.randomcountryname3=rm.choice(self.newcountrieslist2)
        if self.randomnumber==1:
            self.question2button1=tk.Button(self.question2, text=self.flagslist2names[self.random_index], height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion3(self.flagslist2names[self.random_index]))
            self.question2button1.pack(padx=10, pady=10)
            self.question2button2=tk.Button(self.question2, text=self.randomcountryname1, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion3(self.randomcountryname1))
            self.question2button2.pack(padx=10, pady=10)
            self.question2button3=tk.Button(self.question2, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname2))
            self.question2button3.pack(padx=10, pady=10)
            self.question2button4=tk.Button(self.question2, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname3))
            self.question2button4.pack(padx=10, pady=10)
        elif self.randomnumber==2:
            self.question2button1=tk.Button(self.question2, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname1))
            self.question2button1.pack(padx=10, pady=10)
            self.question2button2=tk.Button(self.question2, text=self.flagslist2names[self.random_index], height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion3(self.flagslist2names[self.random_index]))
            self.question2button2.pack(padx=10, pady=10)
            self.question2button3=tk.Button(self.question2, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname2))
            self.question2button3.pack(padx=10, pady=10)
            self.question2button4=tk.Button(self.question2, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname3))
            self.question2button4.pack(padx=10, pady=10)
        elif self.randomnumber==3:
            self.question2button1=tk.Button(self.question2, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname1))
            self.question2button1.pack(padx=10, pady=10)
            self.question2button2=tk.Button(self.question2, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion3(self.randomcountryname2))
            self.question2button2.pack(padx=10, pady=10)
            self.question2button3=tk.Button(self.question2, text=self.flagslist2names[self.random_index], height=2, font=("Arial", 15), bg=bcolor3, fg=fcolor3, width=40, command=lambda:self.gotoquestion3(self.flagslist2names[self.random_index]))
            self.question2button3.pack(padx=10, pady=10)
            self.question2button4=tk.Button(self.question2, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname3))
            self.question2button4.pack(padx=10, pady=10)
        else:
            self.question2button1=tk.Button(self.question2, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname1))
            self.question2button1.pack(padx=10, pady=10)
            self.question2button2=tk.Button(self.question2, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion3(self.randomcountryname2))
            self.question2button2.pack(padx=10, pady=10)
            self.question2button3=tk.Button(self.question2, text=self.randomcountryname3, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion3(self.randomcountryname3))
            self.question2button3.pack(padx=10, pady=10)
            self.question2button4=tk.Button(self.question2, text=self.flagslist2names[self.random_index], height=2, font=("Arial", 15), bg=bcolor4, fg=fcolor4, width=40, command=lambda:self.gotoquestion3(self.flagslist2names[self.random_index]))
            self.question2button4.pack(padx=10, pady=10)


        

        self.question2button1.bind("<Enter>", lambda event:self.on_enter5(event, bcolor1, fcolor1))
        self.question2button1.bind("<Leave>", lambda event:self.on_leave5(event, bcolor1, fcolor1))
        self.question2button2.bind("<Enter>", lambda event:self.on_enter6(event, bcolor2, fcolor2))
        self.question2button2.bind("<Leave>", lambda event:self.on_leave6(event, bcolor2, fcolor2))
        self.question2button3.bind("<Enter>", lambda event:self.on_enter7(event, bcolor3, fcolor3))
        self.question2button3.bind("<Leave>", lambda event:self.on_leave7(event, bcolor3, fcolor3))
        self.question2button4.bind("<Enter>", lambda event:self.on_enter8(event, bcolor4, fcolor4))
        self.question2button4.bind("<Leave>", lambda event:self.on_leave8(event, bcolor4, fcolor4))
        self.question2.mainloop()
        
    def on_enter5(self, event, bcolor1, fcolor1):
        self.question2button1["background"]=fcolor1
        self.question2button1["foreground"]=bcolor1
    def on_leave5(self, event, bcolor1, fcolor1):
        self.question2button1["background"]=bcolor1
        self.question2button1["foreground"]=fcolor1
    def on_enter6(self, event, bcolor2, fcolor2):
        self.question2button2["background"]=fcolor2
        self.question2button2["foreground"]=bcolor2
    def on_leave6(self, event, bcolor2, fcolor2):
        self.question2button2["background"]=bcolor2
        self.question2button2["foreground"]=fcolor2
    def on_enter7(self, event, bcolor3, fcolor3):
        self.question2button3["background"]=fcolor3
        self.question2button3["foreground"]=bcolor3
    def on_leave7(self, event, bcolor3, fcolor3):
        self.question2button3["background"]=bcolor3
        self.question2button3["foreground"]=fcolor3
    def on_enter8(self, event, bcolor4, fcolor4):
        self.question2button4["background"]=fcolor4
        self.question2button4["foreground"]=bcolor4
    def on_leave8(self, event, bcolor4, fcolor4):
        self.question2button4["background"]=bcolor4
        self.question2button4["foreground"]=fcolor4

    def gotoquestion3(self, userchoice2):
        if userchoice2==self.flagslist2names[self.random_index]:
            self.points=self.points+100
        self.Ukraine=tk.PhotoImage(file="Ukraine.png")
        self.Turkey=tk.PhotoImage(file="Turkey.png")
        self.Denmark=tk.PhotoImage(file="Denmark.png")
        self.Croatia=tk.PhotoImage(file="Croatia.png")
        self.Ireland=tk.PhotoImage(file="Ireland.png")
        self.Estonia=tk.PhotoImage(file="Estonia.png")
        self.flagslist3=[self.Ukraine, self.Turkey, self.Denmark, self.Croatia, self.Ireland, self.Estonia]
        self.flagslist3names=["Ukraine", "Turkey", "Denmark", "Croatia", "Ireland", "Estonia"]
        self.randomflag3=rm.choice(self.flagslist3)
        self.random_index=self.flagslist3.index(self.randomflag3)
        self.question2.withdraw()
        self.question3=tk.Toplevel(self.home)
        self.question3.attributes("-fullscreen", True)
        self.question3.title("Question 3")
        self.question3.geometry("1000x1000")
        self.question3backround=tk.PhotoImage(file="nice.png")
        self.question3backroundlabel=tk.Label(self.question3, image=self.question3backround)
        self.question3backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.question3label=tk.Label(self.question3, text="Guess the Flag", height=2, width=37, bg="purple", fg="black", font=("Helvetica", 20))
        self.question3label.pack(padx=10, pady=10)
        self.question3scorelabel=tk.Label(self.question3, text=f"Score: {self.points}", height=2, width=10, font=("Helvetica", 15), bg="blue", fg="black")
        self.question3scorelabel.place(x=1140, y=30)
        self.randomflag3label=tk.Label(self.question3, image=self.randomflag3)
        self.randomflag3label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.numbers=[1, 2, 3, 4]
        self.randomnumber=rm.choice(self.numbers)
        self.newcountrieslist3=[]
        self.newcountrieslist3=[country for country in self.countries if country != self.flagslist3names[self.random_index]]

        self.randomcountryname1=rm.choice(self.newcountrieslist3)
        self.randomcountryname2=rm.choice(self.newcountrieslist3)
        self.randomcountryname3=rm.choice(self.newcountrieslist3)
        if self.randomnumber==1:
            self.question3button1=tk.Button(self.question3, text=self.flagslist3names[self.random_index], height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion4(self.flagslist3names[self.random_index]))
            self.question3button1.pack(padx=10, pady=10)
            self.question3button2=tk.Button(self.question3, text=self.randomcountryname1, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion4(self.randomcountryname1))
            self.question3button2.pack(padx=10, pady=10)
            self.question3button3=tk.Button(self.question3, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname2))
            self.question3button3.pack(padx=10, pady=10)
            self.question3button4=tk.Button(self.question3, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname3))
            self.question3button4.pack(padx=10, pady=10)
        elif self.randomnumber==2:
            self.question3button1=tk.Button(self.question3, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname1))
            self.question3button1.pack(padx=10, pady=10)
            self.question3button2=tk.Button(self.question3, text=self.flagslist3names[self.random_index], height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion4(self.flagslist3names[self.random_index]))
            self.question3button2.pack(padx=10, pady=10)
            self.question3button3=tk.Button(self.question3, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname2))
            self.question3button3.pack(padx=10, pady=10)
            self.question3button4=tk.Button(self.question3, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname3))
            self.question3button4.pack(padx=10, pady=10)
        elif self.randomnumber==3:
            self.question3button1=tk.Button(self.question3, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname1))
            self.question3button1.pack(padx=10, pady=10)
            self.question3button2=tk.Button(self.question3, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion4(self.randomcountryname2))
            self.question3button2.pack(padx=10, pady=10)
            self.question3button3=tk.Button(self.question3, text=self.flagslist3names[self.random_index], height=2, font=("Arial", 15), bg=bcolor3, fg=fcolor3, width=40, command=lambda:self.gotoquestion4(self.flagslist3names[self.random_index]))
            self.question3button3.pack(padx=10, pady=10)
            self.question3button4=tk.Button(self.question3, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname3))
            self.question3button4.pack(padx=10, pady=10)
        else:
            self.question3button1=tk.Button(self.question3, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname1))
            self.question3button1.pack(padx=10, pady=10)
            self.question3button2=tk.Button(self.question3, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion4(self.randomcountryname2))
            self.question3button2.pack(padx=10, pady=10)
            self.question3button3=tk.Button(self.question3, text=self.randomcountryname3, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion4(self.randomcountryname3))
            self.question3button3.pack(padx=10, pady=10)
            self.question3button4=tk.Button(self.question3, text=self.flagslist3names[self.random_index], height=2, font=("Arial", 15), bg=bcolor4, fg=fcolor4, width=40, command=lambda:self.gotoquestion4(self.flagslist3names[self.random_index]))
            self.question3button4.pack(padx=10, pady=10)


        

        self.question3button1.bind("<Enter>", lambda event:self.on_enter9(event, bcolor1, fcolor1))
        self.question3button1.bind("<Leave>", lambda event:self.on_leave9(event, bcolor1, fcolor1))
        self.question3button2.bind("<Enter>", lambda event:self.on_enter10(event, bcolor2, fcolor2))
        self.question3button2.bind("<Leave>", lambda event:self.on_leave10(event, bcolor2, fcolor2))
        self.question3button3.bind("<Enter>", lambda event:self.on_enter11(event, bcolor3, fcolor3))
        self.question3button3.bind("<Leave>", lambda event:self.on_leave11(event, bcolor3, fcolor3))
        self.question3button4.bind("<Enter>", lambda event:self.on_enter12(event, bcolor4, fcolor4))
        self.question3button4.bind("<Leave>", lambda event:self.on_leave12(event, bcolor4, fcolor4))
        self.question3.mainloop()
        
    def on_enter9(self, event, bcolor1, fcolor1):
        self.question3button1["background"]=fcolor1
        self.question3button1["foreground"]=bcolor1
    def on_leave9(self, event, bcolor1, fcolor1):
        self.question3button1["background"]=bcolor1
        self.question3button1["foreground"]=fcolor1
    def on_enter10(self, event, bcolor2, fcolor2):
        self.question3button2["background"]=fcolor2
        self.question3button2["foreground"]=bcolor2
    def on_leave10(self, event, bcolor2, fcolor2):
        self.question3button2["background"]=bcolor2
        self.question3button2["foreground"]=fcolor2
    def on_enter11(self, event, bcolor3, fcolor3):
        self.question3button3["background"]=fcolor3
        self.question3button3["foreground"]=bcolor3
    def on_leave11(self, event, bcolor3, fcolor3):
        self.question3button3["background"]=bcolor3
        self.question3button3["foreground"]=fcolor3
    def on_enter12(self, event, bcolor4, fcolor4):
        self.question3button4["background"]=fcolor4
        self.question3button4["foreground"]=bcolor4
    def on_leave12(self, event, bcolor4, fcolor4):
        self.question3button4["background"]=bcolor4
        self.question3button4["foreground"]=fcolor4
    
    def gotoquestion4(self, userchoice3):
        if userchoice3==self.flagslist3names[self.random_index]:
            self.points=self.points+100
        self.Portugal=tk.PhotoImage(file="Portugal.png")
        self.Hungary=tk.PhotoImage(file="Hungary.png")
        self.Kosovo=tk.PhotoImage(file="Kosovo.png")
        self.Iceland=tk.PhotoImage(file="Iceland.png")
        self.Belgium=tk.PhotoImage(file="Belgium.png")
        self.Bulgaria=tk.PhotoImage(file="Bulgaria.png")
        self.flagslist4=[self.Portugal, self.Hungary, self.Kosovo, self.Iceland, self.Belgium, self.Bulgaria]
        self.flagslist4names=["Portugal", "Hungary", "Kosovo", "Iceland", "Belgium", "Bulgaria"]
        self.randomflag4=rm.choice(self.flagslist4)
        self.random_index=self.flagslist4.index(self.randomflag4)
        self.question3.withdraw()
        self.question4=tk.Toplevel(self.home)
        self.question4.attributes("-fullscreen", True)
        self.question4.title("Question 4")
        self.question4.geometry("1000x1000")
        self.question4backround=tk.PhotoImage(file="nice.png")
        self.question4backroundlabel=tk.Label(self.question4, image=self.question4backround)
        self.question4backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.question4label=tk.Label(self.question4, text="Guess the Flag", height=2, width=37, bg="purple", fg="black", font=("Helvetica", 20))
        self.question4label.pack(padx=10, pady=10)
        self.question4scorelabel=tk.Label(self.question4, text=f"Score: {self.points}", height=2, width=10, font=("Helvetica", 15), bg="blue", fg="black")
        self.question4scorelabel.place(x=1140, y=30)
        self.randomflag4label=tk.Label(self.question4, image=self.randomflag4)
        self.randomflag4label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.numbers=[1, 2, 3, 4]
        self.randomnumber=rm.choice(self.numbers)
        self.newcountrieslist4=[]
        self.newcountrieslist4=[country for country in self.countries if country != self.flagslist4names[self.random_index]]

        self.randomcountryname1=rm.choice(self.newcountrieslist4)
        self.randomcountryname2=rm.choice(self.newcountrieslist4)
        self.randomcountryname3=rm.choice(self.newcountrieslist4)
        if self.randomnumber==1:
            self.question4button1=tk.Button(self.question4, text=self.flagslist4names[self.random_index], height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion5(self.flagslist4names[self.random_index]))
            self.question4button1.pack(padx=10, pady=10)
            self.question4button2=tk.Button(self.question4, text=self.randomcountryname1, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion5(self.randomcountryname1))
            self.question4button2.pack(padx=10, pady=10)
            self.question4button3=tk.Button(self.question4, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname2))
            self.question4button3.pack(padx=10, pady=10)
            self.question4button4=tk.Button(self.question4, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname3))
            self.question4button4.pack(padx=10, pady=10)
        elif self.randomnumber==2:
            self.question4button1=tk.Button(self.question4, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname1))
            self.question4button1.pack(padx=10, pady=10)
            self.question4button2=tk.Button(self.question4, text=self.flagslist4names[self.random_index], height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion5(self.flagslist4names[self.random_index]))
            self.question4button2.pack(padx=10, pady=10)
            self.question4button3=tk.Button(self.question4, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname2))
            self.question4button3.pack(padx=10, pady=10)
            self.question4button4=tk.Button(self.question4, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname3))
            self.question4button4.pack(padx=10, pady=10)
        elif self.randomnumber==3:
            self.question4button1=tk.Button(self.question4, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname1))
            self.question4button1.pack(padx=10, pady=10)
            self.question4button2=tk.Button(self.question4, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion5(self.randomcountryname2))
            self.question4button2.pack(padx=10, pady=10)
            self.question4button3=tk.Button(self.question4, text=self.flagslist4names[self.random_index], height=2, font=("Arial", 15), bg=bcolor3, fg=fcolor3, width=40, command=lambda:self.gotoquestion5(self.flagslist4names[self.random_index]))
            self.question4button3.pack(padx=10, pady=10)
            self.question4button4=tk.Button(self.question4, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname3))
            self.question4button4.pack(padx=10, pady=10)
        else:
            self.question4button1=tk.Button(self.question4, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname1))
            self.question4button1.pack(padx=10, pady=10)
            self.question4button2=tk.Button(self.question4, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotoquestion5(self.randomcountryname2))
            self.question4button2.pack(padx=10, pady=10)
            self.question4button3=tk.Button(self.question4, text=self.randomcountryname3, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquestion5(self.randomcountryname3))
            self.question4button3.pack(padx=10, pady=10)
            self.question4button4=tk.Button(self.question4, text=self.flagslist4names[self.random_index], height=2, font=("Arial", 15), bg=bcolor4, fg=fcolor4, width=40, command=lambda:self.gotoquestion5(self.flagslist4names[self.random_index]))
            self.question4button4.pack(padx=10, pady=10)


        

        self.question4button1.bind("<Enter>", lambda event:self.on_enter13(event, bcolor1, fcolor1))
        self.question4button1.bind("<Leave>", lambda event:self.on_leave13(event, bcolor1, fcolor1))
        self.question4button2.bind("<Enter>", lambda event:self.on_enter14(event, bcolor2, fcolor2))
        self.question4button2.bind("<Leave>", lambda event:self.on_leave14(event, bcolor2, fcolor2))
        self.question4button3.bind("<Enter>", lambda event:self.on_enter15(event, bcolor3, fcolor3))
        self.question4button3.bind("<Leave>", lambda event:self.on_leave15(event, bcolor3, fcolor3))
        self.question4button4.bind("<Enter>", lambda event:self.on_enter16(event, bcolor4, fcolor4))
        self.question4button4.bind("<Leave>", lambda event:self.on_leave16(event, bcolor4, fcolor4))
        self.question4.mainloop()
        
    def on_enter13(self, event, bcolor1, fcolor1):
        self.question4button1["background"]=fcolor1
        self.question4button1["foreground"]=bcolor1
    def on_leave13(self, event, bcolor1, fcolor1):
        self.question4button1["background"]=bcolor1
        self.question4button1["foreground"]=fcolor1
    def on_enter14(self, event, bcolor2, fcolor2):
        self.question4button2["background"]=fcolor2
        self.question4button2["foreground"]=bcolor2
    def on_leave14(self, event, bcolor2, fcolor2):
        self.question4button2["background"]=bcolor2
        self.question4button2["foreground"]=fcolor2
    def on_enter15(self, event, bcolor3, fcolor3):
        self.question4button3["background"]=fcolor3
        self.question4button3["foreground"]=bcolor3
    def on_leave15(self, event, bcolor3, fcolor3):
        self.question4button3["background"]=bcolor3
        self.question4button3["foreground"]=fcolor3
    def on_enter16(self, event, bcolor4, fcolor4):
        self.question4button4["background"]=fcolor4
        self.question4button4["foreground"]=bcolor4
    def on_leave16(self, event, bcolor4, fcolor4):
        self.question4button4["background"]=bcolor4
        self.question4button4["foreground"]=fcolor4
    
    def gotoquestion5(self, userchoice4):
        if userchoice4==self.flagslist4names[self.random_index]:
            self.points=self.points+100
        self.Malta=tk.PhotoImage(file="Malta.png")
        self.Armenia=tk.PhotoImage(file="Armenia.png")
        self.Latvia=tk.PhotoImage(file="Latvia.png")
        self.Finland=tk.PhotoImage(file="Finland.png")
        self.Belarus=tk.PhotoImage(file="Belarus.png")
        self.Azerbaijan=tk.PhotoImage(file="Azerbaijan.png")
        self.flagslist5=[self.Malta, self.Armenia, self.Latvia, self.Finland, self.Belarus, self.Azerbaijan]
        self.flagslist5names=["Malta", "Armenia", "Latvia", "Finland", "Belarus", "Azerbaijan"]
        self.randomflag5=rm.choice(self.flagslist5)
        self.random_index=self.flagslist5.index(self.randomflag5)
        self.question4.withdraw()
        self.question5=tk.Toplevel(self.home)
        self.question5.attributes("-fullscreen", True)
        self.question5.title("Question 5")
        self.question5.geometry("1000x1000")
        self.question5backround=tk.PhotoImage(file="nice.png")
        self.question5backroundlabel=tk.Label(self.question5, image=self.question5backround)
        self.question5backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.question5label=tk.Label(self.question5, text="Guess the Flag", height=2, width=37, bg="purple", fg="black", font=("Helvetica", 20))
        self.question5label.pack(padx=10, pady=10)
        self.question5scorelabel=tk.Label(self.question5, text=f"Score: {self.points}", height=2, width=10, font=("Helvetica", 15), bg="blue", fg="black")
        self.question5scorelabel.place(x=1140, y=30)
        self.randomflag5label=tk.Label(self.question5, image=self.randomflag5)
        self.randomflag5label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.numbers=[1, 2, 3, 4]
        self.randomnumber=rm.choice(self.numbers)
        self.newcountrieslist5=[]
        self.newcountrieslist5=[country for country in self.countries if country != self.flagslist5names[self.random_index]]

        self.randomcountryname1=rm.choice(self.newcountrieslist5)
        self.randomcountryname2=rm.choice(self.newcountrieslist5)
        self.randomcountryname3=rm.choice(self.newcountrieslist5)
        if self.randomnumber==1:
            self.question5button1=tk.Button(self.question5, text=self.flagslist5names[self.random_index], height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotofinish(self.flagslist5names[self.random_index]))
            self.question5button1.pack(padx=10, pady=10)
            self.question5button2=tk.Button(self.question5, text=self.randomcountryname1, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotofinish(self.randomcountryname1))
            self.question5button2.pack(padx=10, pady=10)
            self.question5button3=tk.Button(self.question5, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname2))
            self.question5button3.pack(padx=10, pady=10)
            self.question5button4=tk.Button(self.question5, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname3))
            self.question5button4.pack(padx=10, pady=10)
        elif self.randomnumber==2:
            self.question5button1=tk.Button(self.question5, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname1))
            self.question5button1.pack(padx=10, pady=10)
            self.question5button2=tk.Button(self.question5, text=self.flagslist5names[self.random_index], height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotofinish(self.flagslist5names[self.random_index]))
            self.question5button2.pack(padx=10, pady=10)
            self.question5button3=tk.Button(self.question5, text=self.randomcountryname2, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname2))
            self.question5button3.pack(padx=10, pady=10)
            self.question5button4=tk.Button(self.question5, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname3))
            self.question5button4.pack(padx=10, pady=10)
        elif self.randomnumber==3:
            self.question5button1=tk.Button(self.question5, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname1))
            self.question5button1.pack(padx=10, pady=10)
            self.question5button2=tk.Button(self.question5, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotofinish(self.randomcountryname2))
            self.question5button2.pack(padx=10, pady=10)
            self.question5button3=tk.Button(self.question5, text=self.flagslist4names[self.random_index], height=2, font=("Arial", 15), bg=bcolor3, fg=fcolor3, width=40, command=lambda:self.gotofinish(self.flagslist5names[self.random_index]))
            self.question5button3.pack(padx=10, pady=10)
            self.question5button4=tk.Button(self.question5, text=self.randomcountryname3, height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname3))
            self.question5button4.pack(padx=10, pady=10)
        else:
            self.question5button1=tk.Button(self.question5, text=self.randomcountryname1, height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname1))
            self.question5button1.pack(padx=10, pady=10)
            self.question5button2=tk.Button(self.question5, text=self.randomcountryname2, height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, width=40, command=lambda:self.gotofinish(self.randomcountryname2))
            self.question5button2.pack(padx=10, pady=10)
            self.question5button3=tk.Button(self.question5, text=self.randomcountryname3, height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotofinish(self.randomcountryname3))
            self.question5button3.pack(padx=10, pady=10)
            self.question5button4=tk.Button(self.question5, text=self.flagslist5names[self.random_index], height=2, font=("Arial", 15), bg=bcolor4, fg=fcolor4, width=40, command=lambda:self.gotofinish(self.flagslist5names[self.random_index]))
            self.question5button4.pack(padx=10, pady=10)


        

        self.question5button1.bind("<Enter>", lambda event:self.on_enter17(event, bcolor1, fcolor1))
        self.question5button1.bind("<Leave>", lambda event:self.on_leave17(event, bcolor1, fcolor1))
        self.question5button2.bind("<Enter>", lambda event:self.on_enter18(event, bcolor2, fcolor2))
        self.question5button2.bind("<Leave>", lambda event:self.on_leave18(event, bcolor2, fcolor2))
        self.question5button3.bind("<Enter>", lambda event:self.on_enter19(event, bcolor3, fcolor3))
        self.question5button3.bind("<Leave>", lambda event:self.on_leave19(event, bcolor3, fcolor3))
        self.question5button4.bind("<Enter>", lambda event:self.on_enter20(event, bcolor4, fcolor4))
        self.question5button4.bind("<Leave>", lambda event:self.on_leave20(event, bcolor4, fcolor4))
        self.question5.mainloop()
        
    def on_enter17(self, event, bcolor1, fcolor1):
        self.question5button1["background"]=fcolor1
        self.question5button1["foreground"]=bcolor1
    def on_leave17(self, event, bcolor1, fcolor1):
        self.question5button1["background"]=bcolor1
        self.question5button1["foreground"]=fcolor1
    def on_enter18(self, event, bcolor2, fcolor2):
        self.question5button2["background"]=fcolor2
        self.question5button2["foreground"]=bcolor2
    def on_leave18(self, event, bcolor2, fcolor2):
        self.question5button2["background"]=bcolor2
        self.question5button2["foreground"]=fcolor2
    def on_enter19(self, event, bcolor3, fcolor3):
        self.question5button3["background"]=fcolor3
        self.question5button3["foreground"]=bcolor3
    def on_leave19(self, event, bcolor3, fcolor3):
        self.question5button3["background"]=bcolor3
        self.question5button3["foreground"]=fcolor3
    def on_enter20(self, event, bcolor4, fcolor4):
        self.question5button4["background"]=fcolor4
        self.question5button4["foreground"]=bcolor4
    def on_leave20(self, event, bcolor4, fcolor4):
        self.question5button4["background"]=bcolor4
        self.question5button4["foreground"]=fcolor4

    def gotofinish(self, userchoice5):
        if userchoice5==self.flagslist5names[self.random_index]:
            self.points=self.points+100
        self.question5.withdraw()
        self.finish=tk.Toplevel(self.home)
        self.finish.attributes("-fullscreen", True)
        self.finish.geometry("500x500")
        self.finish.title("Quiz Finished")
        self.finishbackround=tk.PhotoImage(file="BlackandGold.png")
        self.finishbackroundlabel=tk.Label(self.finish, image=self.finishbackround)
        self.finishbackroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.finishlabel=tk.Label(self.finish, text="Quiz Results", height=2, width=40, fg="black", bg="gold", font=("Helvetica", 20))
        self.finishlabel.place(x=636, y=50)
        self.finalscore=tk.Label(self.finish, text=f"Final Score: {self.points}", height=5, width=20, font=("Helvetica", 15), bg="gold", fg="black")
        self.finalscore.place(x=850, y=500)
        self.homebutton=tk.Button(self.finish, text="Home", height=5, width=10, font=("Helvetica", 15), bg="blue", fg="black", command=self.gobacktohome)
        self.homebutton.place(x=900, y=800)
        self.finish.mainloop()
    
    def gobacktohome(self):
        self.finish.destroy()
        self.points=0
        self.home.deiconify()



GUI()
