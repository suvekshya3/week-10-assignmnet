from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def _init_(self, title, item_id):
        self.__title = title
        self.__item_id = item_id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_item_id(self):
        return self.__item_id

    def set_item_id(self, item_id):
        self.__item_id = item_id

    @abstractmethod
    def display_details(self):
        pass

class Book(LibraryItem):
    def _init_(self, title, item_id, author, isbn, publication_year):
        super()._init_(title, item_id)
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def display_details(self):
        print(f"Book ID: {self.get_item_id()} | Title: {self.get_title()} | Author: {self.author} | ISBN: {self.isbn} | Year: {self.publication_year}")

class Magazine(LibraryItem):
    def _init_(self, title, item_id, issue_number, publisher):
        super()._init_(title, item_id)
        self.issue_number = issue_number
        self.publisher = publisher

    def display_details(self):
        print(f"Magazine ID: {self.get_item_id()} | Title: {self.get_title()} | Issue: {self.issue_number} | Publisher: {self.publisher}")

class LibraryMember:
    def _init_(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_items = []

    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_borrowed_items(self):
        return self.__borrowed_items

    def borrow_item(self, item):
        if item in self.__borrowed_items:
            print(f"{self.__name} has already borrowed '{item.get_title()}'.")
        else:
            self.__borrowed_items.append(item)
            print(f"{self.__name} borrowed '{item.get_title()}'.")

    def return_item(self, item):
        if item in self.__borrowed_items:
            self.__borrowed_items.remove(item)
            print(f"{self.__name} returned '{item.get_title()}'.")
        else:
            print(f"{self.__name} has not borrowed '{item.get_title()}'.")

class Library:
    def _init_(self):
        self.items = {}
        self.members = {}

    def add_item(self, item):
        self.items[item.get_item_id()] = item
        print(f"Item '{item.get_title()}' added to the library.")

    def register_member(self, member):
        self.members[member.get_member_id()] = member
        print(f"Member '{member.get_name()}' registered with ID {member.get_member_id()}.")

    def borrow_item(self, member_id, item_id):
        if member_id in self.members and item_id in self.items:
            member = self.members[member_id]
            item = self.items[item_id]
            member.borrow_item(item)
        else:
            print("Invalid member ID or item ID.")

    def return_item(self, member_id, item_id):
        if member_id in self.members and item_id in self.items:
            member = self.members[member_id]
            item = self.items[item_id]
            member.return_item(item)
        else:
            print("Invalid member ID or item ID.")

    def display_all_items(self):
        print("\nLibrary Collection:")
        for item in self.items.values():
            item.display_details()

def main():
    library = Library()
    book1 = Book("1984", "B1", "George Orwell", "9780451524935", 1949)
    magazine1 = Magazine("Time", "M1", "March 2025", "Time Inc.")
    library.add_item(book1)
    library.add_item(magazine1)
    member1 = LibraryMember("M101", "Alice")
    library.register_member(member1)
    library.borrow_item("M101", "B1")
    library.borrow_item("M101", "M1")
    library.return_item("M101", "B1")
    library.display_all_items()

main()
