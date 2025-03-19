from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker
from typing import List,Tuple

DB_NAME = "model/DB/students.db"
engine = create_engine(f"sqlite:///{DB_NAME}",echo=False)
BASE = declarative_base()

class Student(BASE):
    
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    FIO = Column(String, nullable=False)
    group = Column(Integer, nullable=False, default=0)
    semester_1 = Column(Integer, default=0)
    semester_2 = Column(Integer, default=0)
    semester_3 = Column(Integer, default=0)
    semester_4 = Column(Integer, default=0)
    semester_5 = Column(Integer, default=0)
    semester_6 = Column(Integer, default=0)
    semester_7 = Column(Integer, default=0)
    semester_8 = Column(Integer, default=0)
    semester_9 = Column(Integer, default=0)
    semester_10 = Column(Integer, default=0)
    total_work = Column(Integer,default=0)
    
    @classmethod
    def add_info(cls, info:Tuple[str,int,List[int]]=None):
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
        session = Session()
        new_student = cls(FIO = info[0],
        group = info[1],
        **{f'semester_{i + 1}': info[2][i] for i in range(10)},
        total_work = info[3])
        session.add(new_student)
        session.commit()
        session.close()
    
    @classmethod
    def get_info_paged(cls, page:int, per_page: int):
        offset = (page - 1) * per_page
        session = Session()
        students = session.query(cls).offset(offset).limit(per_page).all()
        session.close()
        return students
    
    @classmethod
    def get_data(cls) -> int:
        session = Session()
        count = session.query(cls).count()
        session.close()
        return count
    
    def to_tuple(self) -> Tuple:
        values = (self.FIO, self.group, self.semester_1, self.semester_2, 
                  self.semester_3, self.semester_4, self.semester_5, self.semester_6, 
                  self.semester_7, self.semester_8, self.semester_9, self.semester_10,self.total_work)
        return values
    
    @classmethod
    def get_groups(cls) -> List[int]:
        session = Session()
        students = session.query(cls).all()
        session.close()
        groups = []
        for student in students:
            groups.append(student.group)
        return groups
    
    @classmethod
    def delete_by_FIO_hours(cls, FIO: str,l_hours: int,h_hours: int):
        session = Session()
        students = session.query(cls).filter(cls.FIO.like(f"{FIO}"),cls.total_work<=h_hours,cls.total_work>=l_hours).all()
        for student in students:
            session.delete(student)
        session.commit()
        session.close()
    
    @classmethod
    def delete_by_group_hours(cls, group: int,l_hours: int,h_hours: int):
        session = Session()
        students = session.query(cls).filter(cls.group.like(f"{group}"),cls.total_work>=l_hours,cls.total_work<=h_hours).all()
        for student in students:
            session.delete(student)
        session.commit()
        session.close()
    
    @classmethod
    def delete_by_group(cls,group: int):
        session = Session()
        students = session.query(cls).filter(cls.group == group)
        for student in students:
            session.delete(student)
        session.commit()
        session.close()
    
    @classmethod
    def delete_by_FIO(cls,FIO: str):
        session = Session()
        students = session.query(cls).filter(cls.FIO.like(f"{FIO}")).all()
        for student in students:
            session.delete(student)
        session.commit()
        session.close()
    
    @classmethod
    def search_by_FIO_hours(cls,FIO: str,l_hours: int,h_hours: int):
        session = Session()
        students = session.query(cls).filter(cls.FIO.like(f"{FIO}"),cls.total_work<=h_hours,cls.total_work>=l_hours).all()
        session.close()
        return students
    
    @classmethod
    def search_by_group_hours(cls,group: int,l_hours: int,h_hours: int):
        session = Session()
        students = session.query(cls).filter(cls.group == group,cls.total_work<=h_hours,cls.total_work>=l_hours).all()
        session.close()
        return students
    
    @classmethod
    def search_by_group(cls,group: int):
        session = Session()
        students = session.query(cls).filter(cls.group == group).all()
        session.close()
        return students
    
    @classmethod
    def search_by_FIO(cls,FIO: str):
        session = Session()
        students = session.query(cls).filter(cls.FIO.like(f"{FIO}")).all()
        session.close()
        return students
        
    @classmethod
    def delete_students(cls,students: List):
        session = Session()
        for student in students:
            session.delete(student)
        session.commit()
        session.close()
    
    def __repr__(self):
        return f"Student(id={self.id}, FIO='{self.FIO}',group={self.group})"

BASE.metadata.create_all(engine)

Session = sessionmaker(bind=engine)