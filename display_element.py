from abc import ABC, abstractmethod
from tkinter import (Label,
                     Entry,
                     Listbox,
                     Button,
                     Frame,
                     Scrollbar,
                     END)
from typing import Optional
from db import MongoDb
from db_manager import DbManager
from base import Task

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

    def get_task(self):
        return self.entry.get()


class TasksList(DisplayElement):
    def __init__(self):
        self.list_box = Optional[Listbox]
        self.db = MongoDb()
        self.db_manager = DbManager(self.db)

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

    def get_selected_task(self):
        selected_index = self.list_box.curselection()

        if selected_index:
            return self.list_box.get(selected_index[0]), selected_index[0]
        return None, None

    def update_task(self, index, new_task):
        self.list_box.delete(index)
        self.list_box.insert(index, new_task)

    def delete_selected_task(self):
        selected_indexes = self.list_box.curselection()

        for index in selected_indexes[::1]:
            self.list_box.delete(index)

    def load_tasks_from_db(self):
        tasks = self.db_manager.get_many()

        if tasks:
            for task in tasks:
                self.add_task(task['task'])


class Menu(DisplayElement):
    def __init__(self, entry_task: EntryTask, task_list: TasksList):
        self.entry_task: EntryTask = entry_task
        self.task_list: TasksList = task_list
        self.db = MongoDb()
        self.db_manager = DbManager(self.db)

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

        task_model = Task(task=task_text)
        serialized_data = task_model.serialize()
        self.db_manager.load_one(serialized_data)

        self.task_list.add_task(task_text)

    def edit_task(self):
        task, index = self.task_list.get_selected_task()

        if task is not None:
            new_task = self.entry_task.get_task()

            task_model = Task(task=new_task)
            serialized_data = task_model.serialize()
            fltr = {'task': task}
            update = {'$set': serialized_data}
            self.db_manager.update_one(fltr, update)

            self.task_list.update_task(index, new_task)

    def delete_task(self):
        selected_task = (self.task_list.get_selected_task())[0]
        fltr = {'task': selected_task}
        print(self.db_manager.delete_one(fltr))
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
