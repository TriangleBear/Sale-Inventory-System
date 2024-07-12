import shutil
from tkinter import messagebox, CENTER
import tkinter as tk
from Utils import Functions
import os
from datetime import datetime
from PIL import Image,ImageTk

class BackupDatabaseView(tk.Toplevel):
    def __init__(self, backupDatabaseController, master=None):
        super().__init__(master, background="GhostWhite")  # Initialize the Toplevel widget first
        self.master = master
        self.backupDatabaseController = backupDatabaseController
        self.mainBg = "Gray89"
        self._window_attributes()

        self.btn_names = ["Backup", "Restore"]
        self.btns = []

    def main(self):
        self._update_frame()
        self._entry_frame()
        self._buttons()
        self.mainloop()

    def _window_attributes(self):
        self.h = 100
        self.w = 300
        image = Image.open('Assets\\icon.jpg')
        photo_image = ImageTk.PhotoImage(image)
        self.iconphoto(False, photo_image)
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        self.title('Backup/Restore Database')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _update_frame(self):
        self.updateFrame = tk.Frame(self,background="GhostWhite")
        self.updateFrame.pack(fill=tk.BOTH,expand=True)

    def _entry_frame(self):
        self.entryFrame = tk.Frame(self.updateFrame,background=self.mainBg,padx=40,pady=45)
        self.entryFrame.place(relx =0.5,rely=0.5,anchor=CENTER)

    def _center_frame(self):
        self.btn_frame = tk.Frame(self.bodyFrame,background=self.mainBg)
        self.btn_frame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _buttons(self):
        Functions.create_buttons_using_grid(self.entryFrame,
                                            labels=self.btn_names,
                                            entryList=self.btns,
                                            bgColor=self.mainBg,
                                            max_columns=2,
                                            w=15,
                                            h=2,
                                            cmd=self._backup_restore)


    def _backup_restore(self, btn_name):
        if btn_name == "Backup":
            if self.backupDatabaseController.backupDatabase():
                messagebox.showinfo("Backup Database", f"Database backup successful.")
        elif btn_name == "Restore":
            self.backupDatabaseController.restoreDatabase()
            messagebox.showinfo("Restore Database", "Database restore successful.")
        