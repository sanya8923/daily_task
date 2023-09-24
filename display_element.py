from abc import ABC, abstractmethod
from tkinter import Label


NAME_APP = 'Daily Tasks'
BUTTON_ADD = 'Add'
BUTTON_EDIT = 'Edit'
BUTTON_DELETE = 'Delete'


class DisplayElement(ABC):
    @abstractmethod
    def add_element(self, frame):
        pass


class Header(DisplayElement):
    def add_element(self, frame):
        label = Label(frame, text=NAME_APP, padx=300, pady=50, font=('arial', 50), background='#242424')
        label.grid(row=0, column=0, sticky='nsew')


class Entry(DisplayElement):
    def add_element(self, frame):
        pass


class TasksList(DisplayElement):
    def add_element(self, frame):
        pass


class Menu(DisplayElement):
    def add_element(self, frame):
        pass

    def add_task(self):
        pass

    def edit_task(self):
        pass

    def delete_task(self):
        pass


class Footer(DisplayElement):
    def add_element(self, frame):
        pass

