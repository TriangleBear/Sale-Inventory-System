from tkinter import *
import tkinter as tk
class StaffDashboard(tk.Tk):
    def __init__(self,frame):
        self.frame = frame
        self.staffFrame = tk.Frame(self.frame,background="GhostWhite")
        self.staffFrame.pack(fill=tk.BOTH,expand=True)
        temp_label = tk.Label(self.staffFrame,text="COMING SOON")
        temp_label.place(relx=0.5,rely=0.5,anchor=CENTER)