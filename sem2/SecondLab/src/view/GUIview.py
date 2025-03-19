import tkinter as tk
from tkinter import messagebox,ttk,filedialog
from .Views import TableView,TreeView
from typing import List

class GUI(tk.Tk):
    
    def __init__(self, contr):
       super().__init__()
       self.controller = contr
       self.title("MVC")
       self.geometry("1920x1080")
       self.withdraw()
       self.create_menu()
       self.create_widgets()
       self.choose_model()
    
    def choose_model(self):
        model = tk.Toplevel(self)
        model.geometry("600x200")
        model.title("Выбор модели")
        DB = tk.Button(model,text="База данных",command=lambda: self.choose_db(model))
        XML = tk.Button(model,text="XML",command=lambda: self.choose_xml(model))
        DB.pack(fill="both",anchor='w')
        XML.pack(fill="both",anchor='e')
        model.protocol("WM_DELETE_WINDOW",lambda: self.end())
    
    def end(self):
        self.destroy()

    def choose_db(self,window):
        self.controller.choose_db()
        window.destroy()
        self.wm_deiconify()
    
    def choose_xml(self,window):
        xml_path = filedialog.askopenfilename(filetypes=[("XML",'.xml')])
        if not xml_path:
                window.destroy()
                self.destroy()
                return
        self.controller.choose_xml(xml_path)
        window.destroy()
        self.wm_deiconify()
    
    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        add_menu = tk.Menu(menu_bar)
        add_menu.add_command(label="Ввести самостоятельно",command=self.add_student) 
        add_menu.add_command(label="Автоматические 50 записей",command=self.add_random)  
        menu_bar.add_cascade(label="Добавление",menu=add_menu)     
        
        search_menu = tk.Menu(menu_bar)
        search_menu.add_command(label="Найти по ФИО и границам ОПТ",command=self.get_FIO_hours_to_search)
        search_menu.add_command(label="Найти по группе и границам ОПТ",command=self.get_group_hours_to_search)
        search_menu.add_command(label="Найти по группе",command=self.get_group_to_search)
        search_menu.add_command(label="Найти по ФИО",command=self.get_FIO_to_search)
        menu_bar.add_cascade(label="Поиск информации",menu=search_menu)
        
        delete_menu = tk.Menu(menu_bar)
        delete_menu.add_command(label = "Удалить по ФИО и границам ОПТ",command=self.get_FIO_hours_to_del)
        delete_menu.add_command(label = "Удалить по группе и границам ОПТ",command=self.get_group_hours_to_del)
        delete_menu.add_command(label = "Удалить по группе",command=self.get_group_to_del)
        delete_menu.add_command(label = "Удалить по ФИО",command=self.get_FIO_to_del)
        menu_bar.add_cascade(label="Удаление",menu=delete_menu)
        
        menu_bar.add_command(label="Изменить кол-во записей на странице",command=self.change_pagination)
        menu_bar.add_command(label="Посмотреть информацию",command=lambda: self.print_message(self.controller.get_info()))
        menu_bar.add_command(label="Изменить представление",command=self.change_view)
        menu_bar.add_command(label='Изменить хранилище для данных',command=self.choose_model)
        
        
    def create_widgets(self):
        self.fram = tk.Frame(self)
        self.table = TableView(self.fram)
        self.table.pack(fill = "both",expand=True)
        self.fram.pack(fill = "both",expand=True)
        navigation_frame = tk.Frame(self)
        self.to_the_start = tk.Button(navigation_frame,text="<<",command=self.controller.start_page)
        self.to_the_start.pack(side=tk.LEFT,padx=5)
        self.prev_button = tk.Button(navigation_frame,text="<",command=self.controller.prev_page)
        self.prev_button.pack(side=tk.LEFT,padx=5)
        navigation_frame.pack(pady=10)
        self.page_label = tk.Label(navigation_frame,text="1")
        self.page_label.pack(side=tk.LEFT,padx = 5)
        self.next_button = tk.Button(navigation_frame,text=">",command=self.controller.next_page)
        self.next_button.pack(side=tk.LEFT,padx=5)
        self.to_the_finish = tk.Button(navigation_frame,text=">>",command=self.controller.end_page)
        self.to_the_finish.pack(side=tk.LEFT,padx=5)
        self.infos_label = tk.Label(self,text="Записей на странице")
        self.infos_label.pack(anchor="se",padx=50,pady=20)
    
    def add_random(self):
        self.controller.add_random()
     
    def update_table(self, data: List):
        self.table.insert_data(data)
        
    def update_page_label(self,current_page,total_pages):
        self.page_label.config(text=f"{current_page}/{total_pages}")

    def update_infos_label(self,curr_len,overall_len):
        self.infos_label.config(text=f"Записей на странице: {curr_len}/{overall_len}")
    
    def change_view(self):
        data = self.table.get_data()
        if self.table.__class__ == TableView:
            self.table.destroy()
            self.table = TreeView(self.fram)
            self.table.pack(fill="both",expand=True)
        else:
            self.table.destroy()
            self.table = TableView(self.fram)
            self.table.pack(fill="both",expand=True)
        self.table.insert_data(data)

    
    def add_student(self):
        add_data = tk.Toplevel(self)
        add_data.title("Новая запись")
        add_data.geometry("400x340")
        tk.Label(add_data,text="Имя").grid(row=0)
        tk.Label(add_data,text="Группа").grid(row=1)
        name_entry = tk.Entry(add_data)
        group_entry = tk.Entry(add_data)
        name_entry.grid(row=0,column=1)
        group_entry.grid(row=1,column=1)
        semestr_entry = []
        for i in range(10):
            tk.Label(add_data, text=f"Семестр {i+1}").grid(row=i+2, column=0)
            entry = tk.Entry(add_data)
            entry.insert(-1,'0')
            entry.grid(row=i+2, column=1)
            semestr_entry.append(entry)
        add_button = tk.Button(add_data,text="Добавить",command= lambda: self.add_record(name_entry.get(),group_entry.get(),[entry.get().strip() for entry in semestr_entry],add_data))
        add_button.grid(row=13,column=5,columnspan=2)  
    
    def add_record(self,name:str,group:str,entries:List,window):
        name,group = name.strip(),group.strip()
        for i in range(len(entries)):
            if entries[i] == "":
                entries[i] = "0"
        check = "".join(entries)
        for i in name:
            if i.isdigit():
                self.print_message("Ошибка ввода\nФИО должно состоять из букв")
                window.destroy()
                return
            
        if not name: 
            self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
            window.destroy()
        elif not group.isdecimal():
            self.print_message("Ошибка ввода\nГруппа должнa быть неотриц числoм")
            window.destroy()
        elif  not check.isdigit():
            self.print_message("Ошибка ввода\Часы работы должны быть неотриц числами")
            window.destroy()
        else:
            for i in range(len(entries)):
                entries[i] = int(entries[i])
            self.controller.add_data((name,int(group),entries))
            window.destroy()
    
    def change_pagination(self):
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
            self.controller.change_pagination(new_pages)
        window.destroy()
        
    def get_FIO_hours_to_search(self):
        search = tk.Toplevel(self)
        search.title("Поиск")
        search.geometry("400x100")
        tk.Label(search,text="Имя").grid(row=0)
        FIO_entry = tk.Entry(search)
        FIO_entry.grid(row=0,column=1)
        tk.Label(search,text="нижняя граница ОПТ").grid(row=1)
        hours_L_entry = tk.Entry(search)
        hours_L_entry.grid(row=1,column=1)
        tk.Label(search,text="верхняя граница ОПТ").grid(row=2)
        hours_H_entry = tk.Entry(search)
        hours_H_entry.grid(row=2,column=1)
        search_button = tk.Button(search,text="Ввод",command=lambda: self.search_by_FIO_hours(FIO_entry.get().strip(),hours_L_entry.get().strip(),hours_H_entry.get().strip(),search))
        search_button.grid(row=3,column=2)
        
    def search_by_FIO_hours(self,FIO,l_hours,h_hours,window):
        for i in FIO:
            if i.isdigit():
                self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
                window.destroy()
                return
            
        if not FIO:
            self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
            window.destroy()
        elif not(l_hours.isdecimal() and h_hours.isdecimal()):
            self.print_message("Ошибка ввода\n Часы работы должны быть неотриц числами")
            window.destroy()
        else:
            self.controller.search_by_FIO_hours(FIO,int(l_hours),int(h_hours))
            window.destroy()
            
                  
    
    def get_group_hours_to_search(self):
        groups = self.controller.get_all_groups()
        groups = list(groups)
        groups.sort()
        if len(groups) == 0:
            self.print_message("Нет студентов")
            return None
        for i in range(len(groups)):
            groups[i] = str(groups[i])
            
        search = tk.Toplevel(self)
        search.title("Поиск")
        search.geometry("400x100")
        groups_label = tk.Label(search,text = "Группа")
        groups_label.grid(row=0,column=0)
        combobox = ttk.Combobox(search,values=groups,state="readonly")
        combobox.current(0)
        combobox.grid(row=0,column=1)
        tk.Label(search,text="нижняя граница ОПТ").grid(row=1)
        hours_L_entry = tk.Entry(search)
        hours_L_entry.grid(row=1,column=1)
        tk.Label(search,text="верхняя граница ОПТ").grid(row=2)
        hours_H_entry = tk.Entry(search)
        hours_H_entry.grid(row=2,column=1)
        search_button = tk.Button(search,text="Ввод",command=lambda: self.search_by_group_hours(combobox.get().strip(),hours_L_entry.get().strip(),hours_H_entry.get().strip(),search))
        search_button.grid(row=3,column=2)
            
    def search_by_group_hours(self,group,l_hour,h_hour,window): 
        if l_hour.isdecimal() and h_hour.isdecimal():
            self.controller.search_by_group_hours(int(group),int(l_hour),int(h_hour))
            window.destroy()
        else:
            self.print_message("Ошибка ввода\nЧасы работы должны быть неотриц. числами")
            window.destroy()
    
    def get_group_to_search(self):
        groups = self.controller.get_all_groups()
        groups = list(groups)
        groups.sort()
        if len(groups) == 0:
            self.print_message("Нет студентов")
            return None
        for i in range(len(groups)):
            groups[i] = str(groups[i])
        search = tk.Toplevel(self)
        search.geometry("400x100")
        search.title("Поиск")
        groups_label = tk.Label(search,text = "Группа")
        groups_label.grid(row=0,column=0)
        combobox = ttk.Combobox(search,values=groups,state="readonly")
        combobox.current(0)
        combobox.grid(row=1,column=0)
        button = tk.Button(search,text="Искать",command=lambda: self.search_by_group(combobox.get().strip(),search))
        button.grid(row=1,column=2)
        
    def search_by_group(self,group,window):
        self.controller.search_by_group(int(group))
        window.destroy()
    
    def get_FIO_to_search(self):
        search = tk.Toplevel(self)
        search.title("Поиск")
        tk.Label(search,text="ФИО").grid(row=0)
        FIO_entry = tk.Entry(search)
        FIO_entry.grid(row=1,column=0)
        button = tk.Button(search,text="Искать",command=lambda: self.search_by_FIO(FIO_entry.get().strip(),search))
        button.grid(row=1,column=2)
        
    def search_by_FIO(self,FIO,window):
        for i in FIO:
            if i.isdigit():
                self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
                window.destroy()
                return
            
        if FIO:
            self.controller.search_by_FIO(FIO)
            window.destroy()
        else:
            self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
            window.destroy()  
    
    def show_find(self,info: List):
        show_table = tk.Toplevel(self)
        show_table.geometry("1920x600")
        table = TableView(show_table)
        show_table.title(f"Найдено {len(info)} записей")
        table.pack(fill = "both",expand=True)
        table.insert_data(info)
        b = tk.Button(show_table,text="Close",command= show_table.destroy)
        b.pack()    
    
    def print_message(self,message):
        messagebox.showwarning(message=message)
        
        
    def get_FIO_hours_to_del(self):
        delition = tk.Toplevel(self)
        delition.title("Удаление студента")
        delition.geometry("400x100")
        tk.Label(delition,text="Имя").grid(row=0)
        FIO_entry = tk.Entry(delition)
        FIO_entry.grid(row=0,column=1)
        tk.Label(delition,text="нижняя граница ОПТ").grid(row=1)
        hours_L_entry = tk.Entry(delition)
        hours_L_entry.grid(row=1,column=1)
        tk.Label(delition,text="верхняя граница ОПТ").grid(row=2)
        hours_H_entry = tk.Entry(delition)
        hours_H_entry.grid(row=2,column=1)
        delition_button = tk.Button(delition,text="Ввод",command=lambda: self.delete_by_FIO_hours(FIO_entry.get().strip(),hours_L_entry.get().strip(),hours_H_entry.get().strip(),delition))
        delition_button.grid(row=3,column=2)
        
    def delete_by_FIO_hours(self,FIO,l_hour,h_hour,window):
        for i in FIO:
            if i.isdigit():
                self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
                window.destroy()
                return
            
        if not FIO:
            self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
            window.destroy()
        elif not(l_hour.isdecimal() and h_hour.isdecimal()):
            self.print_message("Ошибка ввода\n Часы работы должны быть неотриц числами")
            window.destroy()
        else:
            self.controller.delete_by_FIO_hours(FIO,int(l_hour),int(h_hour))
            window.destroy()
            
    def get_group_hours_to_del(self):
        groups = self.controller.get_all_groups()
        groups = list(groups)
        groups.sort()
        if len(groups) == 0:
            self.print_message("Нет студентов")
            return None
        for i in range(len(groups)):
            groups[i] = str(groups[i])
            
        delition = tk.Toplevel(self)
        delition.title("Удаление студента")
        delition.geometry("400x100")
        groups_label = tk.Label(delition,text = "Группа")
        groups_label.grid(row=0,column=0)
        combobox = ttk.Combobox(delition,values=groups,state="readonly")
        combobox.current(0)
        combobox.grid(row=0,column=1)
        tk.Label(delition,text="нижняя граница ОПТ").grid(row=1)
        hours_L_entry = tk.Entry(delition)
        hours_L_entry.grid(row=1,column=1)
        tk.Label(delition,text="верхняя граница ОПТ").grid(row=2)
        hours_H_entry = tk.Entry(delition)
        hours_H_entry.grid(row=2,column=1)
        delition_button = tk.Button(delition,text="Ввод",command=lambda: self.delete_by_group_hours(combobox.get(),hours_L_entry.get(),hours_H_entry.get(),delition))
        delition_button.grid(row=3,column=2)
            
    def delete_by_group_hours(self,group,l_hour,h_hour,window): 
        l_hour,h_hour = l_hour.strip(),h_hour.strip()
        if l_hour.isdecimal() and h_hour.isdecimal():
            self.controller.delete_by_group_hours(int(group),int(l_hour),int(h_hour))
            window.destroy()
        else:
            self.print_message("Ошибка ввода\nЧасы работы должны быть неотриц. числами")
            window.destroy()
            
    def get_group_to_del(self):
        groups = self.controller.get_all_groups()
        groups = list(groups)
        groups.sort()
        if len(groups) == 0:
            self.print_message("Нет студентов")
            return None
        for i in range(len(groups)):
            groups[i] = str(groups[i])
        delition = tk.Toplevel(self)
        delition.geometry("400x100")
        delition.title("Удаление студента")
        groups_label = tk.Label(delition,text = "Группа")
        groups_label.grid(row=0,column=0)
        combobox = ttk.Combobox(delition,values=groups,state="readonly")
        combobox.current(0)
        combobox.grid(row=1,column=0)
        insert_button = tk.Button(delition,text="Удалить",command=lambda: self.delete_by_group(combobox.get(),delition))
        insert_button.grid(row=2,column=1)
    
    def delete_by_group(self,group,window):
        self.controller.delete_by_group(int(group))
        window.destroy()
    
    def get_FIO_to_del(self):
        delition = tk.Toplevel(self)
        delition.title("Удаление студента")
        name_label = tk.Label(delition,text="ФИО")
        name_label.grid(row=0,column=0)
        name_entry = tk.Entry(delition)
        name_entry.grid(row=1,column=0)
        entry_button = tk.Button(delition,text='Удалить',command=lambda: self.delete_by_FIO(name_entry.get().strip(),delition))
        entry_button.grid(row=2,column=1)
    
    def delete_by_FIO(self,FIO,window):
        if FIO:
            self.controller.delete_by_FIO(FIO)
        else:
            self.print_message("Ошибка ввода\nФИО должно состоять из букв (и пробельных символов)")
        window.destroy()