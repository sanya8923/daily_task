import tkinter
from abc import ABC, abstractmethod

NAME_APP = 'Daily Tasks'


class Display(ABC):
    def __init__(self):
        self.app = tkinter.Tk()

    @abstractmethod
    def main_frame(self):
        pass

    @abstractmethod
    def entry(self):
        pass

    @abstractmethod
    def tasks_list(self):
        pass

    @abstractmethod
    def menu(self):
        pass
