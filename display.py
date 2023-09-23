from tkinter import Tk, Frame, Label, Button
from abc import ABC, abstractmethod

NAME_APP = 'Daily Tasks'


class Display(ABC):
    def __init__(self):
        self.app = Tk()

    @abstractmethod
    def main_frame(self):
        pass


class MainDisplay(Display):
    def __init__(self):
        super().__init__()
        self.name_app = NAME_APP

    def main_frame(self):
        frame = Frame(self.app)
        frame.pack(padx=100, pady=200)
        self.title()
        self.entry()
        self.tasks_list()
        self.menu()

        self.app.mainloop()

    def title(self):
        label = Label(self.app, text="Это метка внутри Frame", background='blue')
        label.pack()

    def entry(self):
        pass

    def tasks_list(self):
        pass

    def menu(self):
        button = Button(self.main_frame(), text="Это кнопка внутри Frame")
        button.pack()


