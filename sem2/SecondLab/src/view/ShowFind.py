import tkinter as tk
from .TableView import TableView
from tkinter import messagebox


class ShowFind(tk.Toplevel):
    
    def __init__(self,parent,data):
        super().__init__(parent)
        self.data = data
        self.current_page = 1
        self.records_per_page = 5
        self.total_pages = self.calculate_total_pages()
        self.geometry('1920x600')
        self.create_widgets()
        self.update_view()
        
    def create_widgets(self):
        self.table = TableView(self)
        self.table.pack(fill='both',expand=True)
        self.navigation_frame = tk.Frame(self)
        self.navigation_frame.pack()
        self.change_pagin_b = tk.Button(self.navigation_frame,text='Изменить количество записей на странице',command=self.change_pagination_get)
        self.first_page_b = tk.Button(self.navigation_frame,text='<<',command=self.first_page)
        self.prev_page_b = tk.Button(self.navigation_frame,text='<',command=self.prev_page)
        self.next_page_b = tk.Button(self.navigation_frame,text='>',command=self.next_page)
        self.last_page_b = tk.Button(self.navigation_frame,text='>>',command=self.last_page)
        
        self.page_l = tk.Label(self.navigation_frame,text=f"{self.current_page}/{self.total_pages}")
        self.records_on_page = tk.Label(self.navigation_frame,text=f'')
        
        self.change_pagin_b.pack(side=tk.LEFT,padx=5)
        self.first_page_b.pack(side=tk.LEFT,padx=5)
        self.prev_page_b.pack(side=tk.LEFT,padx=5)
        self.page_l.pack(side=tk.LEFT,padx=10)
        self.next_page_b.pack(side=tk.LEFT,padx=5)
        self.last_page_b.pack(side=tk.LEFT,padx=5)
        self.records_on_page.pack(side=tk.LEFT,padx=5)
    
    def calculate_total_pages(self):
        return max(((self.records_per_page + len(self.data) - 1)//self.records_per_page),1)
    
    def first_page(self):
        self.current_page = 1
        self.update_view()
    
    def prev_page(self):
        if self.current_page >1:
            self.current_page -= 1
            self.update_view()
        
    def next_page(self):
        if self.current_page <self.total_pages:
            self.current_page +=1
            self.update_view()
        
    def last_page(self):
        self.current_page = self.total_pages
        self.update_view()
        
    def update_view(self):
        data = self.data[((self.current_page-1)*self.records_per_page):((self.current_page)*self.records_per_page)]
        self.table.insert_data(data)
        self.page_l.configure(text=f"{self.current_page}/{self.total_pages}")
        self.records_on_page.configure(text=f'Количество записей на странице:{len(data)}/{len(self.data)}')
        
    def change_pagination_get(self):
        changing = tk.Toplevel(self)
        changing.geometry("250x100")
        changing.title("Количество записей на странице")
        new_label = tk.Label(changing,text="Новое значение")
        new_label.grid(row=0,column=0)
        new_entry = tk.Entry(changing)
        new_entry.grid(row=1,column=0)
        entry_button = tk.Button(changing,text="Изменить",command=lambda: self.change_pagin(new_entry.get().strip(),changing))
        entry_button.grid(row=2,column=1)
        
    def change_pagin(self,new_pages: str,window):
        try:
            new_pages = int(new_pages)
        except ValueError:
            self.print_message("Должно быть натуральное число")
            window.destroy()
            return    
        if new_pages < 1:
            self.print_message("Должно быть натуральным")
        else:
            self.change_pagination(new_pages)
        window.destroy()
        
    def change_pagination(self, new_numb: int):
        self.records_per_page = new_numb
        self.current_page = 1
        self.total_pages = self.calculate_total_pages()
        self.update_view()
        
    def print_message(self,message):
        messagebox.showwarning(message=message)