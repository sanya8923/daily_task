from abc import ABC, abstractmethod
from tkinter import Label, Entry, Listbox, Button, Frame, Scrollbar


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


class EntryTask(DisplayElement):
    def add_element(self, frame):
        entry = Entry(frame)
        entry.grid(row=1, column=0, sticky='nsew', padx=50)


class TasksList(DisplayElement):
    def add_element(self, frame):
        container = Frame(frame)
        container.grid(row=2, column=0, sticky='nsew', padx=50)

        scrollbar = Scrollbar(container)
        list_box = Listbox(container, yscrollcommand=scrollbar.set)

        list_box.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        scrollbar.config(command=list_box.yview)

        for i in range(24):
            list_box.insert(i, f'Task {i}')


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

