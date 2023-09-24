from abc import ABC, abstractmethod
from tkinter import (Label,
                     Entry,
                     Listbox,
                     Button,
                     Frame,
                     Scrollbar,
                     END)
from typing import Optional

NAME_APP = 'Daily Tasks'
BUTTON_ADD = 'Add'
BUTTON_EDIT = 'Edit'
BUTTON_DELETE = 'Delete'
BACKGROUND = '#242424'
ACTIVE_BACKGROUND_BUTTON = '#1f69a4'


class DisplayElement(ABC):
    @abstractmethod
    def add(self, frame):
        pass


class Header(DisplayElement):
    def add(self, frame):
        label = Label(frame,
                      text=NAME_APP,
                      padx=300,
                      pady=50,
                      font=('arial', 50),
                      background=BACKGROUND)
        label.grid(row=0,
                   column=0,
                   sticky='nsew')


class EntryTask(DisplayElement):
    def __init__(self):
        self.entry: Optional[Entry] = None

    def add(self, frame):
        self.entry = Entry(frame)
        self.entry.grid(row=1,
                        column=0,
                        sticky='nsew',
                        padx=50)

    def get_text(self):
        try:
            return self.entry.get()
        except Exception as e:
            print(e)


class TasksList(DisplayElement):
    def __init__(self):
        self.list_box = Optional[Listbox]

    def add(self, frame):
        container = Frame(frame)
        container.grid(row=2,
                       column=0,
                       sticky='nsew',
                       padx=50)

        scrollbar = Scrollbar(container)
        self.list_box = Listbox(container,
                                yscrollcommand=scrollbar.set)

        self.list_box.pack(side='left',
                           fill='both',
                           expand=True)
        scrollbar.pack(side='right',
                       fill='y')

        scrollbar.config(command=self.list_box.yview)

    def add_task(self, task_text: str):
        self.list_box.insert(END, task_text)

    def delete_selected_task(self):
        selected_indexes = self.list_box.curselection()

        for index in selected_indexes[::1]:
            self.list_box.delete(index)


class Menu(DisplayElement):
    def __init__(self, entry_task: EntryTask, task_list: TasksList):
        self.entry_task: EntryTask = entry_task
        self.task_list: TasksList = task_list

    def add(self, frame):
        button_add = Button(frame,
                            text=BUTTON_ADD,
                            background=BACKGROUND,
                            activebackground=ACTIVE_BACKGROUND_BUTTON,
                            command=self.add_task)
        button_add.grid(row=3,
                        column=0,
                        sticky='nsew',
                        padx=50)

        button_edit = Button(frame,
                             text=BUTTON_EDIT,
                             background=BACKGROUND,
                             activebackground=ACTIVE_BACKGROUND_BUTTON,
                             command=self.edit_task)
        button_edit.grid(row=4,
                         column=0,
                         sticky='nsew',
                         padx=50)

        button_delete = Button(frame,
                               text=BUTTON_DELETE,
                               background=BACKGROUND,
                               activebackground=ACTIVE_BACKGROUND_BUTTON,
                               command=self.delete_task)
        button_delete.grid(row=5,
                           column=0,
                           sticky='nsew',
                           padx=50)

    def add_task(self):
        task_text = self.entry_task.get_text()
        self.task_list.add_task(task_text)

    def edit_task(self):
        pass

    def delete_task(self):
        self.task_list.delete_selected_task()


class Footer(DisplayElement):
    def add(self, frame):
        label = Label(frame,
                      pady=20,
                      background=BACKGROUND)
        label.grid(row=6,
                   column=0,
                   sticky='nsew',
                   padx=20)
