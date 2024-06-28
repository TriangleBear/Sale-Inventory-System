import tkinter as tk
from View import AuditView
from Model import AuditLog

class AuditController:
    def __init__(self):
        self.model = AuditLog()
        self.root = tk.Tk()
        self.root.title("Audit Trail")
        self.view = AuditView(self.root)
        
    def add_entry(self, user_id, username, action, timestamp):
        self.model.add_entry(user_id, username, action, timestamp)
        # Update the view with entries from the model
        self.view.display_entries(self.model.get_entries())

if __name__ == "__main__":
    controller = AuditController()
    controller.run()