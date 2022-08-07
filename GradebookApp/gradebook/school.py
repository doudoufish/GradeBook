from os import name


class Student:
    def __init__(self,id:int,name:str) -> None:
        self.__id = id
        self.__name = name
    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id


    def display(self):
        print("Student ID: ",self.__id)
        print("Student name:",self.__name)
    
    
