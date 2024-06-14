import tkinter as tk
from tkinter import *
from tkinter import font, ttk, messagebox

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        #main window
        w = 580
        h = 420
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width/2) - (w/2))-12
        y = int((screen_height/2)-(h/2))-40

        self.title('S.I.M.S')
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.resizable(False,False)

        #variables
        #login 
        self.l_username_val = tk.StringVar()
        self.l_password_val = tk.StringVar()

        #register
        self.name_val = tk.StringVar()
        self.number_val = tk.IntVar()
        self.address_val = tk.StringVar()
        self.access_val = tk.StringVar()
        self.email_val = tk.StringVar()
        self.r_username_val = tk.StringVar()
        self.r_password_val = tk.StringVar()
        
        self._win_frame()

    def main(self):
        self.mainloop()


    def register(self,name,number,address,access,email,username,password):
        register_var = [name, number, address, access, email, username, password]

        self.controller.register(register_var)

        messagebox.showinfo('Registrion', 'Registraion Successful!')
        self._switch_page(self._login_page)

    def _switch_page(self,page):
        for child in self.windowFrame.winfo_children():
            child.destroy()
        page()

    def _manager_page(self):
        self.managerFrame = tk.Frame(self.windowFrame,background="GhostWhite")
        self.managerFrame.pack(fill=tk.BOTH,expand=True)
        temp_label = tk.Label(self.managerFrame,text="COMING SOON")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _staff_page(self):
        self.staffFrame = tk.Frame(self.windowFrame,background="GhostWhite")
        self.staffFrame.pack(fill=tk.BOTH,expand=True)
        temp_label = tk.Label(self.staffFrame,text="COMING SOON")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _invalid_input_page(self):
        messagebox.showerror('Invalid Input', 'no such user was found')
        self._switch_page(self._login_page)

    def checkInput(self,user,password):
        value = self.controller.checkInput(user,password)
        if value == False:
            self._invalid_input_page()
        elif value == "Admin" or value == "Manager":
            self._switch_page(self._manager_page)
        elif value == "Staff":
            self._switch_page(self._staff_page)
        else:
            self._invalid_input_page()



    def _win_frame(self):
        self.windowFrame = tk.Frame(self)
        self.windowFrame.pack(fill=tk.BOTH,expand=True)
        self._login_page()
    
    def _login_page(self):
        self.loginFrame = tk.Frame(self.windowFrame,background="GhostWhite")
        self.loginFrame.pack(fill=tk.BOTH,expand=True)
        self.loginFrame.tkraise()

        #center frame
        entryFrame = tk.Frame(self.loginFrame,background="Gray82")
        entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

        #widgets/buttons/lbls
        username_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Username ")
        password_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Password ")
        username_entry = tk.Entry(entryFrame,textvariable=self.l_username_val)
        password_entry = tk.Entry(entryFrame,textvariable=self.l_password_val)
        register_btn = tk.Button(entryFrame,font=font.Font(family='Poppins',weight='bold'),text="Register",borderwidth=0,background="Gray82", command=lambda:self._switch_page(self._register_page))
        login_btn = tk.Button(entryFrame, text="Login",borderwidth=1,background="AntiqueWhite1", command=lambda:self.checkInput(self.l_username_val.get(),self.l_password_val.get()))

        username_lbl.grid(row=0,column=0,padx=5,pady=5)
        password_lbl.grid(row=1,column=0,padx=5,pady=5)
        username_entry.grid(row=0,column=1,padx=5,pady=5)
        password_entry.grid(row=1,column=1,padx=5,pady=5)
        register_btn.grid(row=2,columnspan=2,sticky='e',padx=5,pady=5)
        login_btn.grid(row=3,columnspan=2,sticky='e',padx=5,pady=5)
    
    def _register_page(self):
        self.registerFrame = tk.Frame(self.windowFrame,background="GhostWhite")
        self.registerFrame.pack(fill=tk.BOTH,expand=True)

        entryFrame = tk.Frame(self.registerFrame,background="Gray82")
        entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

        name_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Name ")
        number_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Number ")
        address_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Address ")
        access_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Access ")
        email_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Email ")
        username_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Username ")
        password_lbl = tk.Label(entryFrame,borderwidth=0,background="Gray82", text="Password ")
        name_entry = tk.Entry(entryFrame,width=22,textvariable=self.name_val)
        number_entry = tk.Entry(entryFrame,textvariable=self.number_val)
        address_entry = tk.Entry(entryFrame,width=55,textvariable=self.address_val)
        access_entry = ttk.Combobox(entryFrame,values=["Manager", "Staff"],textvariable=self.access_val)
        email_entry = tk.Entry(entryFrame,textvariable=self.email_val)
        username_entry = tk.Entry(entryFrame,textvariable=self.r_username_val)
        password_entry = tk.Entry(entryFrame,textvariable=self.r_password_val)
        register_btn = tk.Button(entryFrame,font=font.Font(family='Poppins',weight='bold'), text="Register", command=lambda:self.register(self.name_val.get(),self.number_val.get(),self.address_val.get(),self.access_val.get(),self.email_val.get(),self.r_username_val.get(),self.r_password_val.get()))

        name_lbl.grid(row=0,column=0,padx=5,pady=5)
        name_entry.grid(row=0,column=1,padx=5,pady=5)
        number_lbl.grid(row=0,column=2,padx=5,pady=5)
        number_entry.grid(row=0,column=3,padx=5,pady=5)
        address_lbl.grid(row=1,column=0,padx=5,pady=5)
        address_entry.grid(row=1,column=1, columnspan=3,padx=5,pady=5)
        access_lbl.grid(row=2,column=0,padx=5,pady=5)
        access_entry.grid(row=2,column=1,padx=5,pady=5)
        email_lbl.grid(row=2,column=2,padx=5,pady=5)
        email_entry.grid(row=2,column=3,padx=5,pady=5)
        username_lbl.grid(row=3,column=0,padx=5,pady=5)
        username_entry.grid(row=3,column=1,padx=5,pady=5)
        password_lbl.grid(row=3,column=2,padx=5,pady=5)
        password_entry.grid(row=3,column=3,padx=5,pady=5)
        register_btn.grid(row=4,columnspan=4,sticky='e',padx=5,pady=5)







        