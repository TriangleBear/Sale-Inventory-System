import tkinter as tk
from tkinter import ttk, messagebox
from Utils import Functions
from Utils import CustomDialog
from PIL import Image, ImageTk
import fitz  # PyMuPDF

class UserManualView(tk.Frame):
    def __init__(self, userManualController, master, pdf_path):
        self.master = master
        self.mainBg = "Gray89"
        super().__init__(self.master, background=self.mainBg)
        self.userManualController = userManualController
        self.pdf_path = pdf_path
        self.scale = 0.565  # Adjust the scale factor as needed
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.main()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg=self.mainBg)
        self.scroll_y = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scroll_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas_frame = tk.Frame(self.canvas, bg=self.mainBg)
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor='nw')

        self.canvas_frame.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def main(self):
        self.view_pdf()

    def view_pdf(self):
        pdf_document = fitz.open(self.pdf_path)
        images = []
        
        for page_num in range(len(pdf_document)):
            pdf_page = pdf_document[page_num]
            zoom_matrix = fitz.Matrix(self.scale, self.scale)
            pix = pdf_page.get_pixmap(matrix=zoom_matrix)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)

        for img in images:
            img_tk = ImageTk.PhotoImage(img)
            label = tk.Label(self.canvas_frame, image=img_tk)
            label.image = img_tk  # Keep a reference to avoid garbage collection
            label.pack()