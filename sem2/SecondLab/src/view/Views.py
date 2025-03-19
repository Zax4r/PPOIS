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
            
            
class TreeView(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.tree = ttk.Treeview(self,show="tree")
        self.tree.pack(expand=True,fill="both")
        
    def insert_data(self,data):
        self.data = data
        for row in self.tree.get_children():
            self.tree.delete(row)
        for i,row in enumerate(data,start=1):
            d_row = row.to_tuple()
            id = self.tree.insert("","end",iid = i,text=d_row[0])
            self.tree.insert(id,"end",text=f"Группа {d_row[1]}")
            id_2 = self.tree.insert(id,"end",text="Общественная работа")
            for j in range(10):
                self.tree.insert(id_2,"end",text=f"Семестр {j+1}: {d_row[j+2]}")
            self.tree.insert(id_2,"end",text=f"Суммарная работа: {d_row[12]}")

    def get_data(self):
        return self.data
        