import tkinter as tk
from tkinter import CENTER, font, ttk, messagebox
from Utils import Functions
from Utils import CustomDialog
from PIL import Image, ImageTk
from tkPDFViewer import tkPDFViewer as pdf
import fitz
class UserManualView(tk.Frame):
    def __init__(self, userManualController, master,pdf_path):
        self.master = master
        self.mainBg = "Gray89"
        super().__init__(self.master, background=self.mainBg)
        self.userManualController = userManualController
        self.pdf_path = pdf_path
        self.scale = 0.5
        self.pack(fill=tk.BOTH, expand=True)

    def main(self):
        self.view_pdf()

    def view_pdf(self):
            v1 = pdf.ShowPdf()
            v2 = v1.pdf_view(self, pdf_location=r"Sale-Inventory-System\Controller\HelpAbout\User-manual-pero-di-pa-tapos-pero-pwede-na-muna.pdf",
            )
            v2.pack(fill=tk.BOTH, expand=True)