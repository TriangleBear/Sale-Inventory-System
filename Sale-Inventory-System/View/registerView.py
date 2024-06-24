from tkinter import *
import tkinter as tk
from Utils import Functions
from tkinter import font

class RegisterView:
    def __init__(self,registerController,frame):
        self.registerController = registerController
        self.frame = frame

    def main(self):
            self.register_labels_with_colspan = {"Name":1,"Number":1,"Address":3,"Access":1,"Email":1,"Username":1,"Password":1}
            self.register_entry_boxes = []
            self.register_inputs = []
            
            self.registerFrame = tk.Frame(self.frame,background="GhostWhite")
            self.registerFrame.pack(fill=tk.BOTH,expand=True)

            entryFrame = tk.Frame(self.registerFrame,background="Gray82")
            entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

            self.create_entry_box_using_grid(frame=entryFrame,labels=self.register_labels_with_colspan,entryList=self.register_entry_boxes,max_columns=2,entryWidth=54)

            register_btn = tk.Button(entryFrame,font=font.Font(family='Poppins',weight='bold'), text="Register", command=lambda:self.register(self.register_entry_boxes))

            register_btn.grid(row=4,columnspan=4,sticky='e',padx=5,pady=5)