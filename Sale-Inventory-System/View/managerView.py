from tkinter import *
import tkinter as tk
class ManagerDashboard:
    def __init__(self,frame):
        self.frame = frame
    
    def manager_page(self):
        self.managerFrame = tk.Frame(self.frame,background="GhostWhite")
        self.managerFrame.pack(fill=tk.BOTH,expand=True)
        temp_label = tk.Label(self.managerFrame,text="COMING SOON")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)