from abc import ABC, abstractmethod


class DisplayElement(ABC):
    @abstractmethod
    def add_element(self):
        pass


class Header(DisplayElement):
    def add_element(self):
        pass


class Entry(DisplayElement):
    def add_element(self):
        pass


class TasksList(DisplayElement):
    def add_element(self):
        pass


class Menu(DisplayElement):
    def add_element(self):
        pass

    def add_task(self):
        pass

    def edit_task(self):
        pass

    def delete_task(self):
        pass


class Footer(DisplayElement):
    def add_element(self):
        pass

