from abc import ABC, abstractmethod
from tkinter import (Label,
                     Entry,
                     Listbox,
                     Button,
                     Frame,
                     Scrollbar,
                     END)
from typing import Optional
from db.db import MongoDb
from db.db_manager import DbManager
from model import Task

# Constants representing various UI elements and configurations.
NAME_APP = 'Daily Tasks'
ENTRY_TEXT = 'Enter a task...'
BUTTON_ADD = 'Add'
BUTTON_EDIT = 'Edit'
BUTTON_DELETE = 'Delete'
BACKGROUND = '#242424'
TEXT_COLOR = '#FFFFFF'
BACKGROUND_BUTTON = '#1f69a4'


class DisplayElement(ABC):
    """
    Abstract base class representing a display element in the UI.
    """
    @abstractmethod
    def add(self, frame):
        """
        Abstract method to add the display element to the given frame.
        """
        pass


class Header(DisplayElement):
    """
    Class representing the header of the application.
    """
    def add(self, frame):
        """
        Adds the header to the given frame.
        """
        label = Label(frame,
                      text=NAME_APP,
                      fg='white',
                      relief="flat",
                      padx=300,
                      pady=50,
                      font=('arial', 50),
                      background=BACKGROUND)
        label.grid(row=0,
                   column=0,
                   sticky='nsew')


class EntryTask(DisplayElement):
    """
    Class representing the task entry field in the application.
    """
    def __init__(self):
        self.entry: Optional[Entry] = None

    def add(self, frame):
        """
        Adds the task entry field to the given frame.
        """
        self.entry = Entry(frame,
                           relief="groove",
                           highlightcolor='black',
                           highlightbackground='black',
                           highlightthickness=1,
                           background=BACKGROUND,
                           fg='white', insertbackground='white')
        self.entry.insert(0, ENTRY_TEXT)
        self.entry.bind('<FocusIn>', self.clear)
        self.entry.grid(row=1,
                        column=0,
                        sticky='nsew',
                        padx=50)

    def bind(self, *args, **kwargs):
        return self.entry.bind(*args, **kwargs)

    def clear(self, *args, **kwargs):
        """
        When receiving focus, if the text in Entry is equal to the placeholder, clear the Entry.

        :param event: Command from event.bind (Entry)
        :return: None
        """
        if len(self.entry.get()) > 0:
            self.entry.delete(0, 'end')

    def get_text(self) -> Optional[str]:
        """
        Retrieves the text entered in the task entry field.

        :return: The text entered in the task entry field or None.
        """
        text = self.entry.get()
        if len(text) > 0:
            return text
        else:
            return None

    def get_task(self):
        """
        Alias for the get_text method.
        """
        return self.entry.get()

    def insert(self, *args, **kwargs):
        """
        Alias for the insert method.
        """
        return self.entry.insert(*args, **kwargs)


class TasksList(DisplayElement):
    """
    Class representing the list of tasks in the application.
    """
    def __init__(self, entry_task):
        self.list_box = Optional[Listbox]
        self.db = MongoDb()
        self.db_manager = DbManager(self.db)
        self.entry_task: EntryTask = entry_task

    def add(self, frame):
        """
        Adds the task list to the given frame.
        """
        container = Frame(frame,
                          relief="ridge",
                          background=BACKGROUND)
        container.grid(row=2,
                       column=0,
                       sticky='nsew',
                       padx=50)

        scrollbar = Scrollbar(container,
                              bg=BACKGROUND,
                              border=1)
        self.list_box = Listbox(container,
                                yscrollcommand=scrollbar.set,
                                background='white')
        self.list_box.bind('<<ListboxSelect>>', self.on_select)

        self.list_box.pack(side='left',
                           fill='both',
                           expand=True)
        scrollbar.pack(side='right',
                       fill='y')

        scrollbar.config(command=self.list_box.yview)

    def add_task(self, task_text: str):
        """
        Adds a task to the task list.

        :param task_text: The text of the task to be added.
        """
        self.list_box.insert(END, task_text)

    def get_selected_task(self):
        """
        Retrieves the selected task from the task list.

        :return: A tuple containing the text of the selected task and its index, or (None, None) if no task is selected.
        """
        selected_index = self.list_box.curselection()

        if selected_index:
            return self.list_box.get(selected_index[0]), selected_index[0]
        return None, None

    def update_task(self, index, new_task):
        """
        Updates the task at the given index with the new task text.

        :param index: The index of the task to be updated.
        :param new_task: The new task text.
        """
        self.list_box.delete(index)
        self.list_box.insert(index, new_task)

    def delete_selected_task(self):
        """
        Deletes the selected task(s) from the task list.
        """
        selected_indexes = self.list_box.curselection()

        for index in selected_indexes[::1]:
            self.list_box.delete(index)

    def load_tasks_from_db(self):
        """
        Loads tasks from the database and adds them to the task list.
        """
        tasks = self.db_manager.get_many()

        if tasks:
            for task in tasks:
                task_model = Task.deserialize(task)
                self.add_task(task_model.task)

    def on_select(self, *args, **kwargs):
        index = self.list_box.curselection()
        print(f'index: {index}')

        if index:
            selected_text = self.list_box.get(index)
            print(f'selected_text: {selected_text}')
            self.entry_task.clear()
            self.entry_task.insert(0, selected_text)


class Menu(DisplayElement):
    """
    Class representing the menu of the application.
    """
    def __init__(self, entry_task: EntryTask, task_list: TasksList):
        self.entry_task: EntryTask = entry_task
        self.task_list: TasksList = task_list
        self.db = MongoDb()
        self.db_manager = DbManager(self.db)

    def add(self, frame):
        """
        Adds the menu buttons to the given frame.
        """
        self.entry_task.entry.bind('<Return>', self.add_task_wrapper)

        button_add = Button(frame,
                            text=BUTTON_ADD,
                            relief='raised',
                            activebackground=BACKGROUND_BUTTON,
                            highlightbackground=BACKGROUND,
                            command=self.add_task)
        button_add.grid(row=3,
                        column=0,
                        sticky='nsew',
                        padx=50)

        button_edit = Button(frame,
                             text=BUTTON_EDIT,
                             relief='raised',
                             activebackground=BACKGROUND_BUTTON,
                             highlightbackground=BACKGROUND,
                             command=self.edit_task)
        button_edit.grid(row=4,
                         column=0,
                         sticky='nsew',
                         padx=50)

        button_delete = Button(frame,
                               text=BUTTON_DELETE,
                               relief='raised',
                               activebackground=BACKGROUND_BUTTON,
                               highlightbackground=BACKGROUND,
                               command=self.delete_task)
        button_delete.grid(row=5,
                           column=0,
                           sticky='nsew',
                           padx=50)

    def add_task_wrapper(self, event):
        """
        Pressing Enter calls the add_task

        :param event: Command from event.bind (Entry)
        :return: None
                """
        self.add_task()

    def add_task(self):
        """
        Adds a new task to the task list and the database.
        """
        task_text = self.entry_task.get_text()
        if task_text:
            task_model = Task(task=task_text)
            serialized_data = task_model.serialize()
            self.db_manager.load_one(serialized_data)

            self.task_list.add_task(task_text)
            self.entry_task.clear()

    def edit_task(self):
        """
        Edits the selected task in the task list and the database.
        """
        task, index = self.task_list.get_selected_task()

        if task is not None:
            new_task = self.entry_task.get_task()

            new_task_model = Task(task=new_task)
            serialized_data = new_task_model.serialize()

            fltr = Task(task=task)
            serialized_fltr = fltr.serialize()

            update = {'$set': serialized_data}
            self.db_manager.update_one(serialized_fltr, update)

            self.task_list.update_task(index, new_task)

    def delete_task(self):
        """
        Deletes the selected task from the task list and the database.
        """
        task, index = self.task_list.get_selected_task()

        if task is not None:
            fltr = Task(task=task)
            serialized_fltr = fltr.serialize()
            self.db_manager.delete_one(serialized_fltr)

            self.task_list.delete_selected_task()


class Footer(DisplayElement):
    """
    Class representing the footer of the application.
    """
    def add(self, frame):
        """
        Adds the footer to the given frame.
        """
        label = Label(frame,
                      pady=20,
                      background=BACKGROUND)
        label.grid(row=6,
                   column=0,
                   sticky='nsew',
                   padx=20)



