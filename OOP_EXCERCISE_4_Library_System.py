
from abc import ABC,abstractmethod

class LibraryItem(ABC):
    def __init__(self,title, item_id,is_available):
        self.title = title
        self.item_id = item_id
        self.is_available = is_available

    @abstractmethod
    def check_out():
        pass

    @abstractmethod
    def check_in():
        pass

class Book(LibraryItem):
    def __init__(self,author,title, item_id,is_available=True):
        self.author=author
        self.title = title
        self.item_id = item_id
        self.is_available = is_available

    def check_in(self):
        if not self.is_available:
            self.is_available = True
            return f" The Book {self.title} is checked In!"
        return f"The Book {self.title} is already checked In!"

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return f"The Book {self.title} is checked out!"
        return f"The Book {self.title} is already checked out!"

class DVD(LibraryItem):

    def __init__(self,director,title, item_id,is_available=True):
        super().__init__(title, item_id,is_available)
        self.director = director

    def check_in(self):
        if not self.is_available:
            self.is_available = True
            return f" The DVD {self.title} is checked In!"
        return f"The DVD {self.title} is already checked In!"
    
    def check_out(self):
        if self.is_available:
            self.is_available = False
            return f"The DVD {self.title} is checked out!"
        return f"The DVD {self.title} is already checked out!"

class Journal(LibraryItem):

    def __init__(self,issue_number,title, item_id,is_available=True):
        super().__init__(title, item_id,is_available)
        self.issue_number = issue_number

    def check_in(self):
        if not self.is_available:
            self.is_available = True
            return f" The Journal {self.title} is checked In!"
        return f"The Journal {self.title} is already checked In!"

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return f"The Journal {self.title} is checked out!"
        return f"The Journal {self.title} is already checked out!"


class LibraryCatalog():

    def __init__(self) -> None:
        self.LibraryItems=[]
    
    def add_items(self,item_name):
        self.item_name = item_name
        self.LibraryItems.append(item_name)
        return f"The Library Item \"{item_name.title}\" has been added Successfully !"

    def remove_items(self,item_id):
        self.item_id = item_id
        for item in self.LibraryItems:
            if self.item_id == item.item_id:
                self.LibraryItems.remove(item)
                return f"The Library Item \"{item.title}\" has been Removed Successfully !"
            return f"The Library Item id \"{item_id}\" are not in your system !"

    def available_items(self):

        AllItems = [item for item in self.LibraryItems if item.is_available]
        return [item.title for item in AllItems]

'''
print(Test Programm..)
'''

book = Book(author="Ripon",title="Python",item_id=1)
dvd = DVD(director="Mr. Ripon",title="Python Tutorial",item_id=1)
journal = Journal(issue_number="100201",title="Implementation of OOP",item_id=1)

library_catalog = LibraryCatalog()

library_catalog.add_items(book)
print(library_catalog.add_items(dvd))
library_catalog.add_items(journal)

print(library_catalog.available_items())
print(book.check_in())
print(library_catalog.available_items())

print("-----------------------------------")

book = Book(author="Ripon1",title="Python1",item_id=2)
print(library_catalog.add_items(book))

print(library_catalog.available_items())
print(book.check_out())
print(library_catalog.available_items())

print("-----------------------------------")

print(library_catalog.remove_items(1))
print(library_catalog.available_items())