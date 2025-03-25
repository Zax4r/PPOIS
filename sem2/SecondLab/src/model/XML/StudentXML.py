import os
from xml.dom import minidom 
import xml.sax
from faker import Faker
from typing import List,Tuple
from .MyStudent import MyStudent
from .MyHandler import MyHandler

class Model():
    def __init__(self,path:str):
        self.path = path
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            with open(path, 'w') as f:
                f.write('<students></students>')
        try:
            self.doc = minidom.parse(path)
        except Exception as e:
            print(e)
            return
           
        self.handler = MyHandler()
        self.update_data()
    
    
    def update_data(self):
        self.handler.data = []
        with open(self.path,"r",encoding="UTF-8") as file:
            xml.sax.parse(file,handler=self.handler)
            self.data = self.handler.data.copy()
        if self.data:
             self.last_id = self.data[-1].id
        else:
            self.last_id = "0"
    
    
    def remove_whitespace_nodes(self,node):
        for child in list(node.childNodes):
            if child.nodeType == child.TEXT_NODE and not child.data.strip():
                node.removeChild(child)
            elif child.hasChildNodes():
                self.remove_whitespace_nodes(child)
    
    
    def add_info(self, info:Tuple[str,int,List[int]]=None):
        self.last_id = str(int(self.last_id)+1)
        fake = Faker()
        if info is None:
            info = []
            info.append(fake.name())
            info.append(fake.random_int(min=1, max=10))
            work = []
            for i in range(10):
                work.append(fake.random_int(min=1,max=14))
            info.append(work)
        info = list(info)
        info.append(sum(info[2]))
        info = tuple(info)

        self.data.append(MyStudent(self.last_id,info[0],info[1],info[2],info[3]))

        new_student = self.doc.createElement("student")
        new_student.setAttribute("id",f"{self.last_id}")
        
        fio = self.doc.createElement("FIO")
        fio.appendChild(self.doc.createTextNode(f"{info[0]}"))
        new_student.appendChild(fio)
        
        group = self.doc.createElement("group")
        group.appendChild(self.doc.createTextNode(f"{info[1]}"))
        new_student.appendChild(group)
        
        for i in range(10):
            semester = self.doc.createElement(f"semester_{i+1}")
            semester.appendChild(self.doc.createTextNode(f"{info[2][i]}"))
            new_student.appendChild(semester)
            
        total = self.doc.createElement(f"total")
        total.appendChild(self.doc.createTextNode(f"{info[3]}"))
        new_student.appendChild(total)
    
        self.remove_whitespace_nodes(self.doc)
        
        root = self.doc.documentElement
        root.appendChild(new_student)
        
        with open(self.path,"w",encoding="UTF-8") as file:
            file.write(self.doc.toprettyxml())
        self.remove_whitespace_nodes(self.doc)
        
    def get_info_paged(cls,page: int,per_page: int) -> List[MyStudent]:
        offset = (page - 1) * per_page
        end = page*per_page
        return cls.data[offset:end]
    
    def get_groups(self) -> List[int]:
        groups = []
        for stud in self.data:
            groups.append(stud.group)

        return groups
    
    
    def get_data(self) -> int:
        return len(self.data)
    
    
    def search_by_FIO_hours(self,FIO: str,l_hours: int,h_hours: int) -> List[MyStudent]:
        res = []
        for stud in self.data:
            if FIO == stud.FIO and stud.total >= l_hours and stud.total<=h_hours:
                res.append(stud)
        
        return res
    
    
    def search_by_group_hours(self,group: int,l_hours: int,h_hours: int) -> List[MyStudent]:
        res = []
        for stud in self.data:
            if stud.group == group and stud.total >= l_hours and stud.total<=h_hours:
                res.append(stud)
        
        return res
    
    
    def search_by_group(self,group: int) -> List[MyStudent] :
        res = []
        for stud in self.data:
            if stud.group == group:
                res.append(stud)
        return res
 
    
    def search_by_FIO(self,FIO: str)-> List[MyStudent]:
        res = []
        for stud in self.data:
            if FIO == stud.FIO:
                res.append(stud)
        
        return res
        
        
        
    def delete_by_FIO_hours(self,FIO: str,l_hours: int,h_hours: int):
        to_del = self.search_by_FIO_hours(FIO,l_hours,h_hours)
        self.delete(to_del)

    
    def delete_by_group_hours(self,group: int,l_hours: int,h_hours: int):
        to_del = self.search_by_group_hours(group,l_hours,h_hours)
        self.delete(to_del)
        
        
    def delete_by_group(self,group: int):
        to_del = self.search_by_group(group)
        self.delete(to_del)

    
    def delete_by_FIO(self,FIO: str):
        to_del = self.search_by_FIO(FIO)
        self.delete(to_del)   
    
    
    def delete(self,to_delete:List[MyStudent]):
        to_delete_id = []
        for i in to_delete:
            to_delete_id.append(i.id)
            
        root = self.doc.documentElement
        students = root.getElementsByTagName("student")
        for stud in students:
            if stud.getAttribute('id') in to_delete_id:
                root.removeChild(stud)

        self.remove_whitespace_nodes(self.doc)
        with open(self.path,'w',encoding="UTF-8") as f:
            f.write(self.doc.toprettyxml())
        self.remove_whitespace_nodes(self.doc)
        self.update_data()
        
        
    