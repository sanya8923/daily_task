from tkinter import Tk, Frame, Label, Button, Entry, Listbox, Scrollbar
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
        self.app.title(NAME_APP)
        frame = Frame(self.app, background='#242424')
        frame.pack(expand=True)
        self.title(frame)
        self.entry(frame)
        self.tasks_list(frame)
        self.menu(frame)
        self.footer(frame)

        self.app.mainloop()

    def title(self, frame):
        label = Label(frame, text=self.name_app, padx=300, pady=50, font=('arial', 50), background='#242424')
        label.grid(row=0, column=0, sticky='nsew')

    def entry(self, frame):
        entry = Entry(frame)
        entry.grid(row=1, column=0, sticky='nsew', padx=50)

    def tasks_list(self, frame):
        container = Frame(frame)
        container.grid(row=2, column=0, sticky='nsew', padx=50)

        scrollbar = Scrollbar(container)
        list_box = Listbox(container, yscrollcommand=scrollbar.set)

        list_box.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        scrollbar.config(command=list_box.yview)

        for i in range(24):
            list_box.insert(i, f'Task {i}')

    def menu(self, frame):
        button_add = Button(frame, text="Add", bg='#1f69a4', activebackground='#1f69a4')
        button_add.grid(row=3, column=0, sticky='nsew', padx=50)
        button_edit = Button(frame, text="Edit", bg='#1f69a4', activebackground='#1f69a4')
        button_edit.grid(row=4, column=0, sticky='nsew', padx=50)
        button_delete = Button(frame, text="Delete", bg='#1f69a4', activebackground='#1f69a4')
        button_delete.grid(row=5, column=0, sticky='nsew', padx=50)

    def footer(self, frame):
        label = Label(frame, pady=20, background='#242424')
        label.grid(row=6, column=0, sticky='nsew', padx=20)

