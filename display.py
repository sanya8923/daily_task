from tkinter import Tk, Frame, Label, Button, Entry, Listbox, ttk
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
        frame = Frame(self.app, background='#242424')
        frame.pack(expand=True, fill='both')
        self.title(frame)
        self.entry(frame)
        self.tasks_list(frame)
        self.menu(frame)

        self.app.mainloop()

    def title(self, frame):
        label = Label(frame, text=self.name_app, padx=300, pady=200, font=('arial', 50), background='#242424')
        label.pack(side='top')

    def entry(self, frame):
        entry = Entry(frame)
        entry.pack()

    def tasks_list(self, frame):
        list_box = Listbox(frame)
        list_box.insert(0, 'First')
        list_box.pack()

    def menu(self, frame):
        button = Button(frame, text="Это кнопка внутри Frame", bg='#1f69a4', activebackground='#1f69a4')
        button.pack()

        # style = ttk.Style()
        # style.configure('Custom.TButton', background='default')
        # print(style.theme_names())
