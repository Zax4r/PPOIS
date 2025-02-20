from Interface import Interface
from MyOwnException import MyOwnException
from AdministrationTest import AdministrationTest
from MarksTest import MarksTest
import unittest
import pickle

FILE_NAME = r"C:\Users\user\Desktop\PPOIS\LAB1\FirstLab\src\SAVE.pkl"

def save(ui: Interface):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(ui, file)

def load():
    try:
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return Interface()

def main():
    ui = load()
    cycle = True
    while cycle:
        try:
            ui.menu()
            save(ui)
        except MyOwnException:
            cycle = False

if __name__ == '__main__':
    unittest.main()