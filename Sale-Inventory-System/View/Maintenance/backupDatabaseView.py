import shutil
from tkinter import Label, Button, messagebox
class BackupDatabaseView:
    def __init__(self, master):
        self.master = master
        self.master.title("Backup Database")
        self.master.geometry("400x200")
        self.master.resizable(False, False)


    def createWidgets(self):
        self.label = Label(self.master, text="Backup Database")
        self.label.pack()

        self.backupButton = Button(self.master, text="Backup Database", command=self.backupDatabase)
        self.backupButton.pack()

        self.restoreButton = Button(self.master, text="Restore Database", command=self.restoreDatabase)
        self.restoreButton.pack()

    def backupDatabase(self):
        try:
            shutil.copyfile("database.db", "database_backup.db")
            messagebox.showinfo("Success", "Database backup successful")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    