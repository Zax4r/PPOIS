from view.GUIview import GUI
import model.DB.StudentSQLite as db
import model.XML.StudentXML as xml
from typing import Tuple


class Controller:
    
    def __init__(self):
        self.view = GUI(self)
        self.current_page = 1
        self.records_per_page = 5
        self.deleted = 0
        self.find = 0
    
    def show(self):
        self.view.mainloop()
    
    #Choosing model
    def choose_db(self):
        self.model = db.Student()
        self.curr_data = self.get_data()
        self.current_page = 1
        self.total_pages = self.calculate_total_pages()
        self.update_view()
    
    def choose_xml(self,path):
        self.model = xml.Model(path)
        self.curr_data = self.get_data()
        self.current_page = 1
        self.total_pages = self.calculate_total_pages()
        self.update_view()

    #updating view
    def update_view_delition(self):
        amount = self.curr_data - self.get_data()
        self.deleted +=amount
        if amount:
            self.view.print_message(f"Удалено записей {amount}")
        else:
            self.view.print_message("Таких записей не найдено")
        self.curr_data = self.get_data()
        self.total_pages = self.calculate_total_pages()
        self.current_page = 1
        self.update_view()

    def update_view(self):
        info = self.model.get_info_paged(self.current_page,self.records_per_page)
        self.view.update_table(info)
        self.view.update_page_label(self.current_page,self.total_pages)
        self.view.update_infos_label(len(info),self.get_data())
    
    #pagination
    def calculate_total_pages(self):
        self.curr_data = self.model.get_data()
        return max(((self.curr_data + self.records_per_page -1)//self.records_per_page),1)
    
    def change_pagination(self, new_numb: int):
        self.records_per_page = new_numb
        self.current_page = 1
        self.total_pages = self.calculate_total_pages()
        self.update_view()
    
    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page +=1
        self.update_view()        
    
    def prev_page(self):
        if self.current_page > 1:
            self.current_page -=1
        self.update_view()  
    
    def end_page(self):
        self.current_page = self.total_pages
        self.update_view()
        
    def start_page(self):
        self.current_page = 1
        self.update_view()
    
    #addding data
    def add_random(self):
        for _ in range(50):
            self.model.add_info(None)
        self.total_pages = self.calculate_total_pages()
        self.update_view()
    
    def add_data(self,info: Tuple):
        self.model.add_info(info)
        self.total_pages = self.calculate_total_pages()
        self.update_view()
    
    #getting info
    def get_data(self):
        return self.model.get_data()
    
    def get_info(self):
        return f"Найдено: {self.find}\nУдалено: {self.deleted}"
    
    def get_all_groups(self):
        groups = set(self.model.get_groups())
        return groups        
    
    #deleting
    def delete_by_group(self,group: int):
        self.model.delete_by_group(group)
        self.update_view_delition()
        
    def delete_by_FIO(self,FIO: str):
        self.model.delete_by_FIO(FIO)
        self.update_view_delition()
    
    def delete_by_FIO_hours(self,FIO: str,l_hours: int,h_hours: int):
        self.model.delete_by_FIO_hours(FIO,l_hours,h_hours)
        self.update_view_delition()
    
    def delete_by_group_hours(self,group: int,l_hours: int,h_hours: int):
        self.model.delete_by_group_hours(group,l_hours,h_hours)
        self.update_view_delition()
             
    #searching    
    def search_by_FIO_hours(self,FIO: str,l_hours: int,h_hours: int):
        students = self.model.search_by_FIO_hours(FIO,l_hours,h_hours)
        self.find +=len(students)
        self.view.show_find(students)
        
    def search_by_group_hours(self,group: int,l_hours: int,h_hours: int):
        students = self.model.search_by_group_hours(group,l_hours,h_hours)
        self.find +=len(students)
        self.view.show_find(students)
    
    def search_by_group(self,group: int):
        students = self.model.search_by_group(group)
        self.find +=len(students)        
        self.view.show_find(students)
    
    def search_by_FIO(self,FIO: str):
        students = self.model.search_by_FIO(FIO)
        self.find +=len(students)
        self.view.show_find(students)