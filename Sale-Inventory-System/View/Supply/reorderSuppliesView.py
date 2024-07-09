import tkinter as tk
from tkinter import *
from tkinter import ttk,font,messagebox
from tkcalendar import DateEntry
from Utils import Functions
class ReorderSuppliesView(tk.Toplevel):
    def __init__(self,reorderSuppliesController,item_order):
        super().__init__(backgroun="GhostWhite")
        self.reorderSuppliesController = reorderSuppliesController
        self.item_order = item_order
        self.item_id = item_order[0]
        self.item_name = item_order[1]
        self._window_attributes()
        self.mainBg = "Grey90"

        self.reorder_lbls_with_colspan = {
            "Quantity to Add":1,
            "Expected Payment":1,
            "Arrival Date":1
        }
        self.item_entry_boxes = []

    def main(self):
        self._item_id_frame()
        self._item_id_lbl()
        self._item_entry_frame()
        self._item_reorder_widgets()
        self._expiry_date_entry(2,0)
        self._confirm_button(3,1)
        self._back_button(3,0)
        self.mainloop()

    def _window_attributes(self):
        self.h = 420
        self.w = 580
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - (self.w / 2)) - 12
        y = int((screen_height / 2) - (self.h / 2)) - 40

        
        self.title(f'Item Reorder')
        self.geometry(f"{self.w}x{self.h}+{x}+{y}")
        self.resizable(False, False)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.quit())

    def _item_entry_frame(self):
        self.entryFrame = tk.Frame(self,background=self.mainBg,padx=20,pady=80)
        self.entryFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _item_id_frame(self):
        self.idFrame = tk.Frame(self,background=self.mainBg,width=580,height=40)
        self.idFrame.place(relx=0,rely=0)

    def _item_id_lbl(self):
        self.itemIdLbl = tk.Label(self.idFrame,font=font.Font(family='Courier New',size=14,weight='bold'),
                              text=f"Item ID:{self.item_id} | Item Name:{self.item_name}",background=self.mainBg)
        self.itemIdLbl.place(relx=0.5,rely=0.5,anchor=CENTER)

    def _item_reorder_widgets(self):
        entrywidth = 23
        Functions.create_entry_box_using_grid(
            frame=self.entryFrame,
            labels=self.reorder_lbls_with_colspan,
            bgColor=self.mainBg,
            entryList=self.item_entry_boxes,
            borderW=1,
            max_columns=1,
            shortEntryWidth=entrywidth,
            side='e'
        )

    def _expiry_date_entry(self,current_r=0,current_c=0): #2,0
        self.expiry_date_lbl = tk.Label(self.entryFrame,text="Arrival Date:",background=self.mainBg)
        self.expiry_date_lbl.grid(row=current_r,column=current_c,padx=2,pady=2,sticky='e')

        self.expiry_date = DateEntry(self.entryFrame,width=20,borderwidth=0,year=2000,date_pattern='YYYY-MM-DD')
        self.expiry_date.set_date(Functions.get_current_date())
        self.expiry_date.grid(row=current_r,column=current_c+1,padx=2,pady=2)

        self.item_entry_boxes.append(self.expiry_date)

    def _confirm_button(self,current_r=0,current_c=0,status=None):#4,3 item #5,3 Supply
        register_btn = tk.Button(self.entryFrame,font=font.Font(family='Courier New',size=9,weight='bold'), 
                                 text="Register", command=lambda:self._checkInput(self.item_entry_boxes))
        register_btn.grid(row=current_r,column=current_c,sticky='e',padx=5,pady=5)

    def _back_button(self,current_r,current_c):#4,2 item #5,2 supply
        back_btn = tk.Button(self.entryFrame, text="Back",font=font.Font(family='Courier New',size=9,weight='bold'), command=lambda: self.destroy())
        back_btn.grid(row=current_r,column=current_c,sticky='w',padx=5,pady=5)

    def _checkInput(self,data:list):
        entryData = Functions.format_reorder_item_data(data = [entry.get().strip() for entry in data])
        check_input = self.reorderSuppliesController.checkInput(entryData)
        if check_input == 0:
            entryData.append(self.item_id)
            entryData.append(self.item_name)
            self.reorderSuppliesController.supplierController.view.add_to_cart.register(entryData)
            messagebox.showinfo('Cart Addition', 'Item added to cart!')
            self.destroy()
        else:
            messagebox.showerror('Item Order Error', check_input)
