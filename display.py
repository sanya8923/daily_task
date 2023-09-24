from tkinter import (Tk,
                     Frame)
from display_element import (DisplayElement,
                             Header,
                             EntryTask,
                             TasksList,
                             Menu,
                             Footer)
from abc import (ABC,
                 abstractmethod)

NAME_APP = 'Daily Tasks'
BACKGROUND = '#242424'


class Display(ABC):
    def __init__(self):
        self.app = Tk()

    @abstractmethod
    def make(self):
        pass


class MainDisplay(Display):
    def __init__(self):
        super().__init__()
        self.name_app = NAME_APP

    def make(self):
        self.app.title(NAME_APP)
        frame = Frame(self.app, background=BACKGROUND)
        frame.pack(expand=True)

        self.add_element(Header(), frame)
        self.add_element(EntryTask(), frame)
        self.add_element(TasksList(), frame)
        self.add_element(Menu(), frame)
        self.add_element(Footer(), frame)

        self.app.mainloop()

    def add_element(self, display_element: DisplayElement, frame: Frame):
        return display_element.add(frame)

