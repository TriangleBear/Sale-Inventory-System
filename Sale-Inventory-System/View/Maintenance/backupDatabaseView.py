import shutil
from tkinter import Label, Button, messagebox
class BackupDatabaseView:
    def __init__(self, master):
        self.master = master
        self.master.title("Backup Database")
        self.master.geometry("400x200")
        self.master.resizable(False, False)

        self.backupDatabaseLabel = Label(self.master, text="Backup Database")
        self.backupDatabaseLabel.pack()

        self.backupDatabaseButton = Button(self.master, text="Backup Database", command=self.backupDatabase)
        self.backupDatabaseButton.pack()

    def backupDatabase(self):
        try:
            shutil.copyfile("database.db", "database_backup.db")
            messagebox.showinfo("Success", "Database backup successful")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    