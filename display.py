import tkinter
from abc import ABC, abstractmethod

NAME_APP = 'Daily Tasks'


class Display(ABC):
    def __init__(self):
        self.app = tkinter.Tk()

    @abstractmethod
    def main_frame(self):
        pass


class MainDisplay(Display):
    def __init__(self):
        super().__init__()
        self.name_app = NAME_APP

    def main_frame(self):
        pass

    def entry(self):
        pass

    def tasks_list(self):
        pass

    def menu(self):
        pass
