import tkinter as tk
from tkinter import ttk

class TableView(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        columns = ["ФИО","Группа"]
        for i in range(10):
            columns.append(f"Семестр {i+1}")
        columns.append("Сумма работ")
        self.columns = tuple(columns)
        
        self.table = ttk.Treeview(self,columns=self.columns,show="headings")
        
        total_width = self.table.winfo_width()
        num_columns = len(self.columns)
        width_per_column = total_width // num_columns
        
        fake_table = ttk.Frame(self)
        tk.Label(fake_table,padx=30,text='Общественная работа').pack(fill='x')
        fake_table.pack()        
        
        for col in self.columns:
            self.table.heading(col,text = col)
            self.table.column(column=col,stretch=True,width=width_per_column)
        self.table.pack(fill="both",expand=True)
    
    def insert_data(self,data): 
        self.data = data
        for row in self.table.get_children():
            self.table.delete(row)
        for row in data:
            d_row = row.to_tuple()
            self.table.insert(parent="",index = "end",values=d_row)
            
    def get_data(self):
        return self.data

        