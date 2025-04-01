import tkinter as tk
from tkinter import messagebox,ttk,filedialog
from .TableView import TableView
from .TreeView import TreeView
from typing import List
from .ShowFind import ShowFind

class GUI(tk.Tk):
    
    def __init__(self, contr):
       super().__init__()
       self.controller = contr
       self.title("MVC")
       self.geometry("1920x1080")
       self.withdraw()
       self.create_menu()
       self.create_widgets()
       self.choose_model(close=True)
    
    def choose_model(self,close: bool):
        model = tk.Toplevel(self)
        model.geometry("600x200")
        model.title("Выбор модели")
        DB = tk.Button(model,text="База данных",command=lambda: self.choose_db(model))
        XML = tk.Button(model,text="XML",command=lambda: self.choose_xml(model))
        DB.pack(fill="both",anchor='w')
        XML.pack(fill="both",anchor='e')
        if close:
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
        search_menu.add_command(label="Найти по ФИО и границам ОПТ",command=self.get_FIO_hours)
        search_menu.add_command(label="Найти по группе и границам ОПТ",command=self.get_group_hours)
        search_menu.add_command(label="Найти по группе",command=self.get_group)
        search_menu.add_command(label="Найти по ФИО",command=self.get_FIO)
        menu_bar.add_cascade(label="Поиск информации",menu=search_menu)
        
        delete_menu = tk.Menu(menu_bar)
        delete_menu.add_command(label = "Удалить по ФИО и границам ОПТ",command=lambda: self.get_FIO_hours(to_del=True))
        delete_menu.add_command(label = "Удалить по группе и границам ОПТ",command=lambda: self.get_group_hours(to_del=True))
        delete_menu.add_command(label = "Удалить по группе",command=lambda: self.get_group(to_del=True))
        delete_menu.add_command(label = "Удалить по ФИО",command=lambda: self.get_FIO(to_del=True))
        menu_bar.add_cascade(label="Удаление",menu=delete_menu)
        
        menu_bar.add_command(label="Изменить представление",command=self.change_view)
        menu_bar.add_command(label='Изменить хранилище для данных',command=lambda: self.choose_model(close=False))
        
        
        
    def create_widgets(self):
        self.fram = tk.Frame(self)
        self.table = TableView(self.fram)
        self.table.pack(fill = "both",expand=True)
        self.fram.pack(fill = "both",expand=True)
        navigation_frame = tk.Frame(self)
        self.change_pagin_button = tk.Button(navigation_frame,text='Изменить кол-во записей на странице',command=self.change_pagination)
        self.change_pagin_button.pack(side=tk.LEFT,padx=5)    
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
        self.infos_label = tk.Label(navigation_frame,text="Записей на странице")
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
        add_button = tk.Button(add_data,text="Добавить",command= lambda: self.controller.add_data((name_entry.get(),group_entry.get(),[entry.get().strip() for entry in semestr_entry]),add_data))
        add_button.grid(row=13,column=5,columnspan=2)  
    
    def change_pagination(self):
        changing = tk.Toplevel(self)
        changing.geometry("250x100")
        changing.title("Количество записей на странице")
        new_label = tk.Label(changing,text="Новое значение")
        new_label.grid(row=0,column=0)
        new_entry = tk.Entry(changing)
        new_entry.grid(row=1,column=0)
        entry_button = tk.Button(changing,text="Изменить",command=lambda: self.controller.change_pagination(new_entry.get().strip(),changing))
        entry_button.grid(row=2,column=1)
        
    def get_FIO_hours(self,to_del:bool = False):
        search = tk.Toplevel(self)
        search.title("Ввод данных")
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
        if to_del:
            search_button = tk.Button(search,text="Удалить",command=lambda: self.controller.delete_by_FIO_hours(FIO_entry.get().strip(),(hours_L_entry.get().strip()),(hours_H_entry.get().strip()),search))
        else:
            search_button = tk.Button(search,text="Ввод",command=lambda: self.controller.search_by_FIO_hours(FIO_entry.get().strip(),(hours_L_entry.get().strip()),(hours_H_entry.get().strip()),search))

        search_button.grid(row=3,column=2)                 
    
    def get_group_hours(self,to_del: bool = False):
        groups = self.controller.get_all_groups()
        groups = list(groups)
        groups.sort()
        if len(groups) == 0:
            self.print_message("Нет студентов")
            return None
        for i in range(len(groups)):
            groups[i] = str(groups[i])
            
        search = tk.Toplevel(self)
        search.title("Ввод данных")
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
        if to_del:
            search_button = tk.Button(search,text="Удалить",command=lambda: self.controller.delete_by_group_hours(int(combobox.get().strip()),(hours_L_entry.get().strip()),(hours_H_entry.get().strip()),search))
        else:
            search_button = tk.Button(search,text="Ввод",command=lambda: self.controller.search_by_group_hours(int(combobox.get().strip()),(hours_L_entry.get().strip()),(hours_H_entry.get().strip()),search))

        search_button.grid(row=3,column=2)
    
    def get_group(self,to_del:bool = False):
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
        search.title("Ввод данных")
        groups_label = tk.Label(search,text = "Группа")
        groups_label.grid(row=0,column=0)
        combobox = ttk.Combobox(search,values=groups,state="readonly")
        combobox.current(0)
        combobox.grid(row=1,column=0)
        if to_del:
            button = tk.Button(search,text="Удалить",command=lambda: self.controller.delete_by_group(int(combobox.get().strip()),search))
        else:
            button = tk.Button(search,text="Ввод",command=lambda: self.controller.search_by_group(int(combobox.get().strip()),search))
        button.grid(row=1,column=2)
    
    def get_FIO(self,to_del:bool = False):
        search = tk.Toplevel(self)
        search.title("Ввод данных")
        tk.Label(search,text="ФИО").grid(row=0)
        FIO_entry = tk.Entry(search)
        FIO_entry.grid(row=1,column=0)
        if to_del:
            button = tk.Button(search,text="Удалить",command=lambda: self.controller.delete_by_FIO(FIO_entry.get().strip(),search))
        else:
            button = tk.Button(search,text="Ввод",command=lambda: self.controller.search_by_FIO(FIO_entry.get().strip(),search))
        button.grid(row=1,column=2)
    
    def show_find(self,info: List):
        show_find = ShowFind(self,info)
    
    def print_message(self,message):
        messagebox.showwarning(message=message)