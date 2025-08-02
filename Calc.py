import tkinter as tk
from tkinter import messagebox
import math

class calc:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("500x1500")
        self.window.configure(bg="navy")
        self.window.title("Calc")
        self.windowtitle=tk.Label(self.window, text="Press the button to access calulator!", bg="gold", fg="black", font=("Arial", 20)) 
        self.windowtitle.pack(padx=10, pady=10)
        self.click=tk.Button(self.window, text="CLICK ME", fg="black", bg="gold", font=("Arial", 15), command=self.open_calc)
        self.click.place(x=200, y=300)
        self.window.mainloop()
    def open_calc(self):
        self.window.withdraw()
        self.calc_window=tk.Toplevel(self.window)
        self.calc_window.geometry("500x1500")
        self.calc_window.title("Calc")
        self.calc_window.configure(bg="navy")
        self.calc_frame=tk.Frame(self.calc_window, bg="black")
        self.calc_frame.columnconfigure(0, weight=1)
        self.calc_frame.columnconfigure(1, weight=1)
        self.calc_frame.columnconfigure(2, weight=1)
        self.calc_frame.columnconfigure(3, weight=1)
        self.calc_frame.columnconfigure(4, weight=1)
        self.calc_frame.columnconfigure(5, weight=1)
        self.create_entry()
        self.create_AC_button()
        self.create_delete_button()
        self.create_percent_button()
        self.create_divide_button()
        self.create_7_button()
        self.create_8_button()
        self.create_9_button()
        self.create_X_button()
        self.create_4_button()
        self.create_5_button()
        self.create_6_button()
        self.create_subtract_button()
        self.create_1_button()
        self.create_2_button()
        self.create_3_button()
        self.create_add_button()
        self.created_log_button()
        self.create_0_button()
        self.create_dot_button()
        self.create_equal_button()
        self.create_cos_button()
        self.create_sin_button()
        self.create_tan_button()
        self.create_rad_or_degree_button()
        self.calc_frame.place(x=10, y=100)
    def create_entry(self):
        self.entry=tk.Entry(self.calc_window, font=("Arial", 30), justify="right", width=22)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
        self.entry.place(x=1, y=25)
    def create_AC_button(self):
        self.AC_button=tk.Button(self.calc_frame, text="AC", width=10, height=5, bg="grey", font=("Arial", 15), command=self.AC_button_cicked)
        self.AC_button.grid(row=0, column=0)
    def AC_button_cicked(self):
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
    def create_delete_button(self):
        self.delete_button=tk.Button(self.calc_frame, text="del", width=10, height=5, font=("Arial", 15 ), bg="grey", command=self.delete_button_clicked)
        self.delete_button.grid(row=0, column=1)
    def delete_button_clicked(self):
        self.entry.config(state="normal")
        if self.entry.get()!="0":
            if len(self.entry.get())==1:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "0")
            else:
                self.entry.delete(len(self.entry.get())-1, tk.END)
        self.entry.config(state="readonly")
    def create_percent_button(self):
        self.percent_button=tk.Button(self.calc_frame, text="%", width=10, height=5, bg="grey", font=("Arial", 15), command=self.percent_button_clicked)
        self.percent_button.grid(row=0, column=2)
    def percent_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("%"))
        else:
            self.entry.insert(tk.END, "%")
        self.entry.config(state="readonly")
    def create_divide_button(self):
        self.divide_button=tk.Button(self.calc_frame, text="÷", width=10, height=5, bg="orange", font=("Arial", 15), command=self.divide_button_clicked)
        self.divide_button.grid(row=0, column=3)
    def divide_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("÷"))
        else:
            self.entry.insert(tk.END, "÷")
        self.entry.config(state="readonly")
    def create_7_button(self):
        self.seven_button=tk.Button(self.calc_frame, text="7", width=10, height=5, bg="grey", font=("Arial", 15), command=self.seven_button_clicked)
        self.seven_button.grid(row=1, column=0)
    def seven_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("7"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "7")
            else:
                self.entry.insert(tk.END, "7")
        self.entry.config(state="readonly")
    def create_8_button(self):
        self.eight_button=tk.Button(self.calc_frame, text="8", width=10, height=5, bg="grey", font=("Arial", 15), command=self.eight_button_clicked)
        self.eight_button.grid(row=1, column=1)
    def eight_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("8"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "8")
            else:
                self.entry.insert(tk.END, "8")
        self.entry.config(state="readonly")
    def create_9_button(self):
        self.nine_button=tk.Button(self.calc_frame, text="9", width=10, height=5, bg="grey", font=("Arial", 15), command=self.nine_button_clicked)
        self.nine_button.grid(row=1, column=2)
    def nine_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            
            self.entry.insert(text.index(")"), ("9"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "9")
            else:
                self.entry.insert(tk.END, "9")
        self.entry.config(state="readonly")
    def create_X_button(self):
        self.X_button=tk.Button(self.calc_frame, text="x", width=10, height=5, bg="orange", font=("Arial", 15), command=self.X_button_clicked)
        self.X_button.grid(row=1, column=3)
    def X_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("x"))
        else:
            self.entry.insert(tk.END, "x")
        self.entry.config(state="readonly")
    def create_4_button(self):
        self.four_button=tk.Button(self.calc_frame, text="4", width=10, height=5, bg="grey", font=("Arial", 15), command=self.four_button_clicked)
        self.four_button.grid(row=2, column=0)
    def four_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("4"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "4")
            else:
                self.entry.insert(tk.END, "4")
        self.entry.config(state="readonly")
    def create_5_button(self):
        self.five_button=tk.Button(self.calc_frame, text="5", width=10, height=5, bg="grey", font=("Arial", 15), command=self.five_button_clicked)
        self.five_button.grid(row=2, column=1)
    def five_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("5"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "5")
            else:
                self.entry.insert(tk.END, "5")
        self.entry.config(state="readonly")
    def create_6_button(self):
        self.six_button=tk.Button(self.calc_frame, text="6", width=10, height=5, bg="grey", font=("Arial", 15), command=self.six_button_clicked)
        self.six_button.grid(row=2, column=2)
    def six_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("6"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "6")
            else:
                self.entry.insert(tk.END, "6")
        self.entry.config(state="readonly")
    def create_subtract_button(self):
        self.subtract_button=tk.Button(self.calc_frame, text="-", width=10, height=5, bg="orange", font=("Arial", 15), command=self.subtract_button_clicked)
        self.subtract_button.grid(row=2, column=3)
    def subtract_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("-"))
        else:
            self.entry.insert(tk.END, "-")
        self.entry.config(state="readonly")
    def create_1_button(self):
        self.one_button=tk.Button(self.calc_frame, text="1", width=10, height=5, bg="gray", font=("Arial", 15), command=self.one_button_clicked)
        self.one_button.grid(row=3, column=0)
    def one_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("1"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "1")
            else:
                self.entry.insert(tk.END, "1")
        self.entry.config(state="readonly")
    def create_2_button(self):
        self.two_button=tk.Button(self.calc_frame, text="2", width=10, height=5, bg="gray", font=("Arial", 15), command=self.two_button_clicked)
        self.two_button.grid(row=3, column=1)
    def two_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("2"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "2")
            else:
                self.entry.insert(tk.END, "2")
            self.entry.config(state="readonly")
    def create_3_button(self):
        self.three_button=tk.Button(self.calc_frame, text="3", width=10, height=5, bg="gray", font=("Arial", 15), command=self.three_button_clicked)
        self.three_button.grid(row=3, column=2)
    def three_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("3"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "3")
            else:
                self.entry.insert(tk.END, "3")
            self.entry.config(state="readonly")
    def create_add_button(self):
        self.add_button=tk.Button(self.calc_frame, text="+", width=10, height=5, bg="orange", font=("Arial", 15), command=self.add_button_clicked)
        self.add_button.grid(row=3, column=3)
    def add_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("+"))
        else:
            self.entry.insert(tk.END, "+")
        self.entry.config(state="readonly")
    def created_log_button(self):
        self.log_button=tk.Button(self.calc_frame, text="LOG", height=5, width=10, bg="grey", font=("Arial", 15), command=self.log_button_clicked)
        self.log_button.grid(row=4, column=0)
    def log_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if self.entry.get()=="0":
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "LOG()")
        else:
            if "(" in text and ")" in text:
                self.entry.insert(text.index(")"), ("LOG()"))
            else:
                self.entry.insert(tk.END, "LOG()")
        self.entry.config(state="readonly")
      
    def create_0_button(self):
        self.zero_button=tk.Button(self.calc_frame, text="0", width=10, height=5, bg="gray", font=("Arial", 15), command=self.zero_button_clicked)
        self.zero_button.grid(row=4, column=1)
    def zero_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("0"))
        else:
            if self.entry.get()=="0":
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "0")
            else:
                self.entry.insert(tk.END, "0")
        self.entry.config(state="readonly")
    def create_dot_button(self):
        self.dot_button=tk.Button(self.calc_frame, text=".", width=10, height=5, bg="gray", font=("Arial", 15), command=self.dot_button_clicked)
        self.dot_button.grid(row=4, column=2)
    def dot_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if "(" in text and ")" in text:
            self.entry.insert(text.index(")"), ("."))
        else:
            self.entry.insert(tk.END, ".")
        self.entry.config(state="readonly")
    def create_equal_button(self):
        self.equal_button=tk.Button(self.calc_frame, text="=", width=10, height=5, bg="orange", font=("Arial", 15), command=self.equal_button_clicked)
        self.equal_button.grid(row=4, column=3)
    def equal_button_clicked(self):
        self.entry.config(state="normal")
        try:
            self.expression=self.entry.get()
            print(f"Updated expression: {repr(self.expression)}")
            self.entry.delete(0, tk.END)
            if "x" in self.expression:
                print("Hello")
                self.expression=self.expression.replace("x", "*")
            
            if "÷" in self.expression:
                self.expression=self.expression.replace("÷", "/")
            if "%" in self.expression:
                self.expression=self.expression.replace("%", "/100")
            if "LOG" in self.expression:
                self.index_of_first=self.expression.index("L")
                self.index_of_last=self.expression.index(")")
                self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1],str(math.log10(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")]))))
                print(self.expression)
            if "COS" in self.expression:
                self.index_of_first=self.expression.index("C")
                self.index_of_last=self.expression.index(")")
                if self.rad_or_degree_button.cget("text")=="DEG":
                    if "e-" in str(math.cos(math.degrees(int(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")]))))):
                        self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1], "0")
                        print(self.expression)
                        
                    else:
                        print("hi")
                        self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1],str(math.cos(math.degrees(int(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")]))))))
                else:
                    self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1],str(math.cos(math.radians(int(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")]))))))
                print(self.expression)
            if "SIN" in self.expression:
                self.index_of_first=self.expression.index("S")
                self.index_of_last=self.expression.index(")")
                if self.rad_or_degree_button.cget("text")=="DEG":
                    self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1],str(math.sin(math.degrees(int(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")]))))))
                else:
                    self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1],str(math.sin(math.radians(int(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")]))))))
                print(self.expression)
            if "TAN" in self.expression:
                self.index_of_first=self.expression.index("T")
                self.index_of_last=self.expression.index(")")
                if self.rad_or_degree_button.cget("text")=="DEG":
                    
                    self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1],str(math.tan(math.degrees(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")])))))
                else:
                    self.expression=self.expression.replace(self.expression[self.index_of_first:self.index_of_last+1],str(math.tan(math.radians(eval(self.expression[self.expression.index("(")+1:self.expression.index(")")])))))
                print(self.expression)
            
            self.entry.insert(0, eval(self.expression))


            
        except SyntaxError:
                messagebox.showerror("Error", "SYNTAX ERROR")
                self.entry.insert(0, "0")
        except ZeroDivisionError:
            messagebox.showerror("Error", "ZERO DIVISION ERROR")
            self.entry.insert(0, "0")
        except ValueError:
            messagebox.showerror("Error", "MATH DOMAIN ERROR")
            self.entry.insert(0, "0")
        self.entry.config(state="readonly")
    def create_cos_button(self):
        self.cos_button=tk.Button(self.calc_frame, text="COS", height=5, width=10, font=("Arial", 15), bg="grey", command=self.cos_button_clicked)
        self.cos_button.grid(row=5, column=0)
    def cos_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if self.entry.get()=="0":
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "COS()")
        else:
            if "(" in text and ")" in text:
                self.entry.insert(text.index(")"), ("COS()"))
            else:
                self.entry.insert(tk.END, "COS()")
        self.entry.config(state="readonly")
    def create_sin_button(self):
        self.sin_button=tk.Button(self.calc_frame, text="SIN", height=5, width=10, font=("Arial", 15), bg="grey", command=self.sin_button_clicked)
        self.sin_button.grid(row=5, column=1)
    def sin_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if self.entry.get()=="0":
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "SIN()")
        else:
            if "(" in text and ")" in text:
                self.entry.insert(text.index(")"), ("SIN()"))
            else:
                self.entry.insert(tk.END, "SIN()")
        self.entry.config(state="readonly")
    def create_tan_button(self):
        self.tan_button=tk.Button(self.calc_frame, text="TAN", height=5, width=10, font=("Arial", 15), bg="grey", command=self.tan_button_clicked)
        self.tan_button.grid(row=5, column=2)
    def tan_button_clicked(self):
        self.entry.config(state="normal")
        text=self.entry.get()
        if self.entry.get()=="0":
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "TAN()")
        else:
            if "(" in text and ")" in text:
                self.entry.insert(text.index(")"), ("TAN()"))
            else:
                self.entry.insert(tk.END, "TAN()")
        self.entry.config(state="readonly")
    def create_rad_or_degree_button(self):
        self.rad_or_degree_button=tk.Button(self.calc_frame, text="DEG", height=5, width=10, font=("Arial", 15), bg="grey", command=self.rad_or_degree_button_clicked)
        self.rad_or_degree_button.grid(row=5, column=3)
    def rad_or_degree_button_clicked(self):
        if self.rad_or_degree_button.cget("text")=="DEG":
            self.rad_or_degree_button.config(text="RAD")
        else:
            self.rad_or_degree_button.config(text="DEG")

      
      
calc()