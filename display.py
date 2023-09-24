from tkinter import (Tk,
                     Frame,
                     TclError,
                     messagebox)
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
        try:
            self.app.title(NAME_APP)
            frame = Frame(self.app, background=BACKGROUND)
            frame.pack(expand=True)

            entry_task = EntryTask()
            task_list = TasksList()
            menu = Menu(entry_task, task_list)

            self.add_element(Header(), frame)
            self.add_element(entry_task, frame)
            self.add_element(task_list, frame)
            task_list.load_tasks_from_db()
            self.add_element(menu, frame)
            self.add_element(Footer(), frame)

            self.app.mainloop()
        except TclError as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"TclError: {e}\n")
            messagebox.showerror('Error', 'A graphical error occurred. Please try again or contact support.')
            self.app.quit()
        except Exception as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"Exception: {e}\n")
            messagebox.showerror('Error', 'A graphical error occurred. Please try again or contact support.')
            self.app.quit()

    def add_element(self, display_element: DisplayElement, frame: Frame):
        try:
            return display_element.add(frame)
        except Exception as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"Exception: {e}\n")
            messagebox.showerror('Error', 'A graphical error occurred. Please try again or contact support.')
            self.app.quit()
