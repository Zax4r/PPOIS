import xml
from .MyStudent import MyStudent



class MyHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        self.data = []
        self.stud = None
    
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "student":
            self.stud = MyStudent(attrs['id'])
    
    def characters(self, content):
        if not content.strip():
            return
        if self.current == "FIO":
            self.stud.FIO = content
        elif self.current == "group":
            self.stud.group = int(content.strip())
        elif self.current.startswith("semester"):
            index = int(self.current.split('_')[1]) -1
            self.stud.work[index] = int(content.strip())
        elif self.current == 'total':
            self.stud.total = int(content.strip())
    
    def endElement(self, name):
        if name == "student":
            self.data.append(self.stud)   