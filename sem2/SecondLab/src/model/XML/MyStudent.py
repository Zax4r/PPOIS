from typing import List

class MyStudent:
    
    def __init__(self,id,FIO="",group = 0,work = [0]*10,total = 0):
        self.id: str = id
        self.FIO: str= FIO
        self.group: int = group
        self.work: List[int] = work.copy()
        self.total: int = total
    
    def to_tuple(self):
        res = []
        res.append(self.FIO)
        res.append(self.group)
        for i in range(10):
            res.append(self.work[i])
        res.append(self.total)
        res = tuple(res)
        return res
    
    def __hash__(self):
        return hash((self.id,self.FIO,self.group,self.work,self.total))