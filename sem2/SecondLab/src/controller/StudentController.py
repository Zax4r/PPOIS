from view.GUIview import GUI
from typing import Tuple
import model.DB.StudentSQLite as db
import model.XML.StudentXML as xml


class Controller:
    
    def __init__(self):
        self.view = GUI(self)
        self.current_page = 1
        self.records_per_page = 5

    
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
    def calculate_total_pages(self,data = None):
        self.curr_data = self.model.get_data()
        return max(((self.curr_data + self.records_per_page -1)//self.records_per_page),1)
    
    def change_pagination(self, new_pages: int,window):
        try:
                new_pages = int(new_pages)
        except ValueError:
                self.view.print_message("Должно быть натуральное число")
                window.destroy()
                return    
        if new_pages < 1:
                self.view.print_message("Должно быть натуральным")
                window.destroy()
                return
        window.destroy()
        self.records_per_page = new_pages
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
    
    def add_data(self,info: Tuple,window = None):
        if window:
            window.destroy()
            
        if info is not None:
            if self.validate_info(info):
                for i in range(len(info[2])):
                    info[2][i] = int(info[2][i])
                self.model.add_info(info)
            else:
                return
        else:
            self.model.add_info(info)
        self.total_pages = self.calculate_total_pages()
        self.update_view()
    
    #getting info
    def get_data(self):
        return self.model.get_data()
    
    def get_all_groups(self):
        groups = set(self.model.get_groups())
        return groups        
    
    #deleting
    def delete_by_group(self,group: int,window):
        self.model.delete_by_group(group)
        self.update_view_delition()
        window.destroy()
        
    def delete_by_FIO(self,FIO: str,window):
        if self.validate_FIO(FIO):
            self.model.delete_by_FIO(FIO)
            self.update_view_delition()
        window.destroy()
    
    def delete_by_FIO_hours(self,FIO: str,l_hours: str,h_hours: str,window):
        if self.validate_FIO(FIO) and self.validate_hours(l_hours,h_hours):
            self.model.delete_by_FIO_hours(FIO,int(l_hours),int(h_hours))
            self.update_view_delition()
        window.destroy()
        
    def delete_by_group_hours(self,group: int,l_hours: int,h_hours: int,window):
        if self.validate_hours(l_hours,h_hours):
            self.model.delete_by_group_hours(group,int(l_hours),int(h_hours))
            self.update_view_delition()
        window.destroy()
             
    #searching    
    def search_by_FIO_hours(self,FIO,l_hours,h_hours,window):
        if self.validate_FIO(FIO) and self.validate_hours(l_hours,h_hours):
            students = self.model.search_by_FIO_hours(FIO,int(l_hours),int(h_hours))

            self.view.show_find(students)
        window.destroy()
        
    def search_by_group_hours(self,group: int,l_hours: int,h_hours: int,window):
        if self.validate_hours(l_hours,h_hours):
            students = self.model.search_by_group_hours(group,int(l_hours),int(h_hours))

            self.view.show_find(students)
        window.destroy()
        
    def search_by_group(self,group: int,window):
        students = self.model.search_by_group(group)

        self.view.show_find(students)
        window.destroy()
    
    def search_by_FIO(self,FIO: str,window):
        if self.validate_FIO(FIO):
            students = self.model.search_by_FIO(FIO)

            self.view.show_find(students)
        window.destroy()
        
    #validations
    def validate_FIO(self,FIO):
        for i in FIO:
            if i.isdigit():
                self.view.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
                return False
            
        if not FIO:
            self.view.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
            return False
        
        return True
    
    def validate_hours(self,l_hours,h_hours):
        if not(l_hours.isdecimal() and h_hours.isdecimal()):
            self.view.print_message("Ошибка ввода\n Часы работы должны быть неотриц числами")
            return False
        return True

    def validate_info(self,info):
        
        name,group = info[0],info[1]
        entries = info[2]
        for i in range(len(entries)):
            if entries[i] == "":
                self.view.print_message("Ошибка ввода\nЧасы работы должны быть неотриц числами")
                return False
            
        check = "".join(entries)
        
        if not group.isdecimal():
            self.view.print_message("Ошибка ввода\nГруппа должнa быть неотриц числoм")
            return False
        elif  not check.isdigit():
            self.view.print_message("Ошибка ввода\n Часы работы должны быть неотриц числами")
            return False
        else:
            return self.validate_FIO(name)