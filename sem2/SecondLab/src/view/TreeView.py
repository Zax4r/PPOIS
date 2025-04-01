import tkinter as tk
from tkinter import ttk


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