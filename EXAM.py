#mohammad zarif it
#number 31
# the first code
#class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person = person("yakuza ikari", 22)
# print(f"name: {person.name}, age: {person.age} ")


#code number tow
# class person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"hello my name is {self.name} and im {self.age} years old")
# person = person("yakuza ikari", 22)
# person.greet()


#code number three
# class car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_details(self):
#         print(f"car detail: make in {self.make} in {self.model} company and in {self.year} year")
# car = car("japan", "toyota", 2021)
# car.print_details()


#cod number four
# import math
# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
# circle = circle(2)
# print(f" the are is: {circle.area()}")



#cod number five
# class rectangle:
#     def __init__(self, lenght, wieth):
#         self.lenght = lenght
#         self.wieth = wieth
#     def area(self):
#         return self.wieth * self.lenght
#     def primeter(self):
#         return 2 * (self.lenght + self.wieth)
# rectangle = rectangle(4, 2)
# print(f" the area of rectangle is : {rectangle.area()}")
# print(f"the primeter of rectangle is : {rectangle.primeter()}")




#cod number six
# class animal:
#     def speak(self):
#         pass
# class dog(animal):
#     def speak(self):
#         return "wooof"
# class cat(animal):
#     def speak(self):
#         return "meeeoww"
# akaza = dog()
# jim = cat()
# print(akaza.speak())
# print(jim.speak())



#COD NUMBER SEVEN
# class shap:
#     def area(self):
#         pass
# class square(shap):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side **2
# class tringle(shap):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.height * self.base
# square = square(5)
# tringle = tringle(2, 4)
# print(f"area of the squar : {square.area()}")
# print(f"the area of tringle : {tringle.area()}")



#cod number eight
# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# class manager(employee):
#     def __init__(self, name, salary, departement):
#         super().__init__(name, salary)
#         self.departement =departement
# manager = manager("qasem", 10000, "HR")
# print(f'"manager name : {manager.name} '
#       f'manager salary : {manager.salary} AF '
#       f'manager departement : {manager.departement}"')



#cod number nine
# class vehicle:
#     def drive(self):
#         pass
# class bike(vehicle):
#     def drive(self):
#         return "riding the bike "
# class truck(vehicle):
#     def drive(self):
#         return "driving the truck"
# bike = bike()
# truck = truck()
# print(bike.drive())
# print(truck.drive())



#cod nmber ten
# class bird:
#     def fly(self):
#         pass
# class eagle(bird):
#     def fly(self):
#         return " the eagle can fly too fast"
# class penguin(bird):
#     def fly(self):
#         return "the penguin can not fly instead they swim too fast"
# eagle = eagle()
# penguin = penguin()
# print(f"eagle :{eagle.fly()}  and  penguing : {penguin.fly()}")



# #number 11
# class Account:
#     def __init__(self, initial_balance = 0):
#         self.__balance = initial_balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("amount must be positive")
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("insufficint funds")
#     def get_balance(self):
#         return self.__balance
# account = Account(1000)
# account.deposit(500)
# account.withdraw(200)
# print("curent balance : ",account.get_balance())

#number 12
# class book:
#     def __init__(self, title, author, pages):
#         self.__title = title
#         self.__author = author
#         self.__pages = pages
#     def get_title(self):
#         return self.__title
#     def set_title(self):
#         self.__title = title
#     def get_author(self):
#         return self.__author
#     def set_author(self):
#         self.__auyhor = auyhor
#     def get_pages(self):
#         return self.__pages
#     def set_pages(self):
#         self.__pages = pages
# book = book("1984", "davinchi", 421)
# print("title :",book.get_title())
# print("author: ", book.get_author())
# print("pages: ",book.get_pages())



#number 13
# class laptop:
#     def __init__(self, brand="", model="", price=0.0):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price
#     def apply_discount(self, discount_percentage):
#         if 0 < discount_percentage < 100:
#             discount_amount = self.__price * (discount_percentage / 100)
#             self.__price -= discount_amount
#         else:
#             print("invalid discount percentage")
#     def get_details(self):
#         return f"Brand: {self.__brand}, model: {self.__model}, price: {self.__price}"
# laptop = laptop("dell", "xps 16", 15000)
# laptop.apply_discount(10)
# print(laptop.get_details())


#number 14
# class BankAccount:
#     def __init__(self, acount_num, balance=0):
#         self.__acount_num = acount_num
#         self.__balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("deposit amount must be positive")
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("invalid withdrawal amount or insufficient balance.")
#     def chek_balance(self):
#         return self.__balance
# bank_account = BankAccount("12345678", 1000)
# bank_account.deposit(500)
# bank_account.withdraw(200)
# print("Accont Balance: ",bank_account.chek_balance())



#number 15
# class Student:
#     def __init__(self, name="", grade=0, age=0):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age
#     def set_name(self, name):
#         self.__name = name
#     def set_grade(self,grage):
#         self.__grade = grage
#     def set_age(self, age):
#         self.__age = age
#     def get_name(self):
#         return self.__name
#     def get_grade(self):
#         return self.__grade
#     def get_age(self):
#         return self.__age
# student = Student("karim", 12, 16)
# print("name:",student.get_name())
# print("grade:",student.get_grade())
# print("age:",student.get_age())


#number 16
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#         print(f'Book "{book}" added to the library.')
#
#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             print(f'Book "{book}" removed from the library.')
#         else:
#             print(f'Book "{book}" not found in the library.')
#
#     def __str__(self):
#         return f"Library: {self.name}, Books: {', '.join(str(book) for book in self.books)}"
#
# library = Library("City Library")
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
#
# library.add_book(book1)
# library.add_book(book2)
# print(library)
#
# library.remove_book(book1)
# print(library)


#number 17
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def __str__(self):
#         return f"{self.name} (Grade {self.grade})"

# class School:
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#
#     def add_student(self, student):
#         self.students.append(student)
#         print(f'Student "{student}" added to the school.')
#
#     def remove_student(self, student):
#         if student in self.students:
#             self.students.remove(student)
#             print(f'Student "{student}" removed from the school.')
#         else:
#             print(f'Student "{student}" not found in the school.')
#
#     def __str__(self):
#         return f"School: {self.name}, Students: {', '.join(str(student) for student in self.students)}"
#
# school = School("Greenwood High")
# student1 = Student("Alice", 10)
# student2 = Student("Bob", 12)
#
# school.add_student(student1)
# school.add_student(student2)
# print(school)
#
# school.remove_student(student1)
# print(school)


#number 18
# class Person:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#     def __str__(self):
#         return f"{self.name} ({self.role})"
#
# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.members = []
#
#     def add_member(self, person):
#         self.members.append(person)
#         print(f'Member "{person}" added to the team.')
#
#     def remove_member(self, person):
#         if person in self.members:
#             self.members.remove(person)
#             print(f'Member "{person}" removed from the team.')
#         else:
#             print(f'Member "{person}" not found in the team.')
#
#     def __str__(self):
#         return f"Team: {self.name}, Members: {', '.join(str(member) for member in self.members)}"
# team = Team("Red Dragons")
# member1 = Person("Charlie", "Leader")
# member2 = Person("Dana", "Support")
#
# team.add_member(member1)
# team.add_member(member2)
# print(team)
#
# team.remove_member(member1)
# print(team)



#number 19
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def __str__(self):
#         return f"{self.name} ({self.position})"
#
# class Company:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#         print(f'Employee "{employee}" added to the company.')
#
#     def remove_employee(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#             print(f'Employee "{employee}" removed from the company.')
#         else:
#             print(f'Employee "{employee}" not found in the company.')
#
#     def __str__(self):
#         return f"Company: {self.name}, Employees: {', '.join(str(employee) for employee in self.employees)}"
# company = Company("TechCorp")
# employee1 = Employee("Eve", "Engineer")
# employee2 = Employee("Frank", "Designer")
#
# company.add_employee(employee1)
# company.add_employee(employee2)
# print(company)
#
# company.remove_employee(employee1)
# print(company)



#number 20
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def __str__(self):
#         return f"{self.name} ({self.species})"
#
# class Zoo:
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#         print(f'Animal "{animal}" added to the zoo.')
#
#     def remove_animal(self, animal):
#         if animal in self.animals:
#             self.animals.remove(animal)
#             print(f'Animal "{animal}" removed from the zoo.')
#         else:
#             print(f'Animal "{animal}" not found in the zoo.')
#
#     def __str__(self):
#         return f"Zoo: {self.name}, Animals: {', '.join(str(animal) for animal in self.animals)}"
# zoo = Zoo("Wildlife Park")
# animal1 = Animal("Leo", "Lion")
# animal2 = Animal("Ella", "Elephant")
#
# zoo.add_animal(animal1)
# zoo.add_animal(animal2)
# print(zoo)
#
# zoo.remove_animal(animal1)
# print(zoo)



#number 21
# class FileManager:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def write_to_file(self, content):
#         with open(self.file_name, 'w') as file:
#             file.write(content)
#         print(f"Content written to {self.file_name}")
#
#     def read_from_file(self):
#         try:
#             with open(self.file_name, 'r') as file:
#                 content = file.read()
#             return content
#         except FileNotFoundError:
#             print(f"The file {self.file_name} does not exist.")
#             return None
# file_manager = FileManager('example.txt')
# file_manager.write_to_file("Hello, world!")
# output = file_manager.read_from_file()
# print(f"Content of the file: {output}")


#number 22
# class Log:
#     def __init__(self, log_file):
#         self.log_file = log_file
#     def write_error(self, error_message):
#         with open(self.log_file, 'a') as file:
#             file.write(f"ERROR: {error_message}\n")
#         print(f"Error written to {self.log_file}")
# log = Log('errors.log')
# log.write_error("File not found")
# log.write_error("Connection timed out")


#number 23
#
# class Config:
#     def __init__(self, config_file):
#         self.config_file = config_file
#         self.settings = self._read_config()
#
#     def _read_config(self):
#         settings = {}
#         try:
#             with open(self.config_file, 'r') as file:
#                 for line in file:
#                     key, value = line.strip().split('=')
#                     settings[key] = value
#         except FileNotFoundError:
#             print(f"The config file {self.config_file} does not exist.")
#         return settings
#     def get_setting(self, key):
#         return self.settings.get(key, None)
# config = Config('config.txt')
# db_user = config.get_setting('db_user')
# db_password = config.get_setting('db_password')
# print(f"DB User: {db_user}")
# print(f"DB Password: {db_password}")



#number 24
# import sqlite3
#
# class Database:
#     def __init__(self, db_name):
#         self.db_name = db_name
#         self.connection = None
#
#     def connect(self):
#         try:
#             self.connection = sqlite3.connect(self.db_name)
#             print(f"Connected to {self.db_name} successfully.")
#         except sqlite3.Error as e:
#             print(f"Failed to connect to database. Error: {e}")
#             return None
#
#     def execute_query(self, query):
#         if self.connection:
#             try:
#                 cursor = self.connection.cursor()
#                 cursor.execute(query)
#                 self.connection.commit()
#                 print("Query executed successfully.")
#             except sqlite3.Error as e:
#                 print(f"Failed to execute query. Error: {e}")
#         else:
#             print("No active database connection.")
#     def close(self):
#         if self.connection:
#             self.connection.close()
#             print(f"Connection to {self.db_name} closed.")
# db = Database('example.db')
# db.connect()
# db.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
# db.execute_query("INSERT INTO users (name) VALUES ('Alice')")
# db.close()



#number 25
# class Report:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def generate_report(self):
#         try:
#             with open(self.file_name, 'r') as file:
#                 data = file.read()
#                 print("Report generated successfully.")
#                 return data
#         except FileNotFoundError:
#             print(f"The file {self.file_name} does not exist.")
#             return None
#         except Exception as e:
#             print(f"Failed to generate report. Error: {e}")
#             return None
# report = Report('report.txt')
# report_data = report.generate_report()
# if report_data:
#     print(f"Report Content:\n{report_data}")



#number 26
# class Ticket:
#     def __init__(self, movie_name, seat_number, price):
#         self.movie_name = movie_name
#         self.seat_number = seat_number
#         self.price = price
#
#     def display_ticket(self):
#         print(f"Movie: {self.movie_name}")
#         print(f"Seat Number: {self.seat_number}")
#         print(f"Price: ${self.price:.2f}")
#     def apply_discount(self, discount_percentage):
#         discount_amount = self.price * (discount_percentage / 100)
#         self.price -= discount_amount
#         print(f"Discount applied: {discount_percentage}%")
#         print(f"New Price: ${self.price:.2f}")
# ticket = Ticket("Inception", "A12", 15.00)
# ticket.display_ticket()
# ticket.apply_discount(10)



# #number 27
# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name}: ${self.price:.2f}"
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#         print(f"Added {item.name} to the cart.")
#
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item.name == item_name:
#                 self.items.remove(item)
#                 print(f"Removed {item_name} from the cart.")
#                 return
#         print(f"Item {item_name} not found in the cart.")
#
#     def display_items(self):
#         if self.items:
#             print("Items in the cart:")
#             for item in self.items:
#                 print(f"- {item}")
#         else:
#             print("The cart is empty.")
# cart = ShoppingCart()
# item1 = Item("Apple", 0.99)
# item2 = Item("Banana", 0.59)
#
# cart.add_item(item1)
# cart.add_item(item2)
# cart.display_items()
#
# cart.remove_item("Apple")
# cart.display_items()



#number 28
# class Restaurant:
#     def __init__(self, name):
#         self.name = name
#         self.menu = []
#
#     def add_item(self, item):
#         self.menu.append(item)
#         print(f"Added {item.name} to the menu.")
#
#     def remove_item(self, item_name):
#         for item in self.menu:
#             if item.name == item_name:
#                 self.menu.remove(item)
#                 print(f"Removed {item_name} from the menu.")
#                 return
#         print(f"Item {item_name} not found in the menu.")
#
#     def display_menu(self):
#         if self.menu:
#             print(f"Menu for {self.name}:")
#             for item in self.menu:
#                 print(f"- {item}")
#         else:
#             print("The menu is empty.")
# restaurant = Restaurant("Gourmet Bistro")
# item1 = Item("Pasta", 12.99)
# item2 = Item("Salad", 7.99)
#
# restaurant.add_item(item1)
# restaurant.add_item(item2)
# restaurant.display_menu()
#
# restaurant.remove_item("Salad")
# restaurant.display_menu()




#number 29
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
# class Flight:
#     def __init__(self, flight_number, destination):
#         self.flight_number = flight_number
#         self.destination = destination
#         self.passengers = []
#
#     def add_passenger(self, person):
#         self.passengers.append(person)
#         print(f"Added {person.name} to flight {self.flight_number}.")
#
#     def remove_passenger(self, person_name):
#         for person in self.passengers:
#             if person.name == person_name:
#                 self.passengers.remove(person)
#                 print(f"Removed {person_name} from flight {self.flight_number}.")
#                 return
#         print(f"Passenger {person_name} not found on flight {self.flight_number}.")
#
#     def display_passengers(self):
#         if self.passengers:
#             print(f"Passengers on flight {self.flight_number} to {self.destination}:")
#             for person in self.passengers:
#                 print(f"- {person}")
#         else:
#             print(f"No passengers on flight {self.flight_number}.")
# flight = Flight("AF123", "Paris")
# person1 = Person("John Doe")
# person2 = Person("Jane Smith")
# flight.add_passenger(person1)
# flight.add_passenger(person2)
# flight.display_passengers()
# flight.remove_passenger("John Doe")
# flight.display_passengers()



#number 30
# class Room:
#     def __init__(self, room_number):
#         self.room_number = room_number
#         self.is_occupied = False
#
#     def __str__(self):
#         status = "Occupied" if self.is_occupied else "Available"
#         return f"Room {self.room_number}: {status}"
#
# class Hotel:
#     def __init__(self, name):
#         self.name = name
#         self.rooms = []
#
#     def add_room(self, room):
#         self.rooms.append(room)
#         print(f"Added room {room.room_number} to {self.name}.")
#
#     def book_room(self, room_number):
#         for room in self.rooms:
#             if room.room_number == room_number:
#                 if not room.is_occupied:
#                     room.is_occupied = True
#                     print(f"Room {room_number} has been booked.")
#                 else:
#                     print(f"Room {room_number} is already occupied.")
#                 return
#         print(f"Room {room_number} not found in {self.name}.")
#
#     def checkout_room(self, room_number):
#         for room in self.rooms:
#             if room.room_number == room_number:
#                 if room.is_occupied:
#                     room.is_occupied = False
#                     print(f"Room {room_number} has been checked out.")
#                 else:
#                     print(f"Room {room_number} is not currently occupied.")
#                 return
#         print(f"Room {room_number} not found in {self.name}.")
#
#     def display_rooms(self):
#         if self.rooms:
#             print(f"Rooms in {self.name}:")
#             for room in self.rooms:
#                 print(f"- {room}")
#         else:
#             print(f"{self.name} has no rooms available.")
# hotel = Hotel("Grand Plaza")
# room1 = Room(101)
# room2 = Room(102)
# hotel.add_room(room1)
# hotel.add_room(room2)
# hotel.display_rooms()
# hotel.book_room(101)
# hotel.display_rooms()
# hotel.checkout_room(101)
# hotel.display_rooms()
# import tkinter as tk



#number 36
# class CounterApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Counter App")
#
#         self.counter = 0
#
#         self.label = tk.Label(master, text="Counter: 0", font=("Arial", 24))
#         self.label.pack()
#
#         self.increment_button = tk.Button(master, text="Increment", command=self.increment, font=("Arial", 14))
#         self.increment_button.pack(side=tk.LEFT, padx=20, pady=20)
#
#         self.decrement_button = tk.Button(master, text="Decrement", command=self.decrement, font=("Arial", 14))
#         self.decrement_button.pack(side=tk.RIGHT, padx=20, pady=20)
#
#     def increment(self):
#         self.counter += 1
#         self.update_label()
#
#     def decrement(self):
#         self.counter -= 1
#         self.update_label()
#     def update_label(self):
#         self.label.config(text=f"Counter: {self.counter}")
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CounterApp(root)
#     root.mainloop()
# import tkinter as tk
# from tkinter import messagebox



#number 37
# class ToDoApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("To-Do List App")
#
#         self.tasks = []
#
#         self.task_entry = tk.Entry(master, width=40)
#         self.task_entry.pack(pady=10)
#
#         self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
#         self.add_button.pack(pady=5)
#
#         self.task_listbox = tk.Listbox(master, width=50, height=10)
#         self.task_listbox.pack(pady=10)
#
#         self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
#         self.remove_button.pack(pady=5)
#
#     def add_task(self):
#         task = self.task_entry.get()
#         if task:
#             self.task_listbox.insert(tk.END, task)
#             self.task_entry.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Warning", "You must enter a task.")
#
#     def remove_task(self):
#         try:
#             selected_index = self.task_listbox.curselection()[0]
#             self.task_listbox.delete(selected_index)
#         except IndexError:
#             messagebox.showwarning("Warning", "You must select a task to remove.")
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ToDoApp(root)
#     root.mainloop()
#
# import tkinter as tk



#number 38
# class CalculatorApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Calculator")
#
#         self.result_var = tk.StringVar()
#         self.result_var.set("0")
#
#         self.result_entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge", justify="right")
#         self.result_entry.grid(row=0, column=0, columnspan=4)
#
#         buttons = [
#             '7', '8', '9', '/',
#             '4', '5', '6', '*',
#             '1', '2', '3', '-',
#             '0', '.', '=', '+'
#         ]
#
#         row = 1
#         col = 0
#         for button in buttons:
#             tk.Button(master, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
#             col += 1
#             if col > 3:
#                 col = 0
#                 row += 1
#
#     def on_button_click(self, button):
#         current_text = self.result_var.get()
#         if button == "=":
#             try:
#                 result = eval(current_text)
#                 self.result_var.set(result)
#             except Exception as e:
#                 self.result_var.set("Error")
#         elif button == "C":
#             self.result_var.set("0")
#         else:
#             if current_text == "0":
#                 self.result_var.set(button)
#             else:
#                 self.result_var.set(current_text + button)
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CalculatorApp(root)
#     root.mainloop()
#
# import tkinter as tk
# from tkinter import messagebox



#number 29
# class LoginApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Login App")
#
#         self.username_label = tk.Label(master, text="Username")
#         self.username_label.pack(pady=5)
#         self.username_entry = tk.Entry(master)
#         self.username_entry.pack(pady=5)
#
#         self.password_label = tk.Label(master, text="Password")
#         self.password_label.pack(pady=5)
#         self.password_entry = tk.Entry(master, show="*")
#         self.password_entry.pack(pady=5)
#
#         self.login_button = tk.Button(master, text="Login", command=self.login)
#         self.login_button.pack(pady=20)
#
#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#         if username == "admin" and password == "password":
#             messagebox.showinfo("Login Successful", "Welcome, admin!")
#         else:
#             messagebox.showerror("Login Failed", "Invalid username or password.")
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LoginApp(root)
#     root.mainloop()
#
# import tkinter as tk



#number 40
# class WeatherApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Weather App")
#
#         self.city_label = tk.Label(master, text="Enter City")
#         self.city_label.pack(pady=5)
#         self.city_entry = tk.Entry(master)
#         self.city_entry.pack(pady=5)
#
#         self.check_button = tk.Button(master, text="Check Weather", command=self.check_weather)
#         self.check_button.pack(pady=10)
#
#         self.weather_label = tk.Label(master, text="", font=("Arial", 16))
#         self.weather_label.pack(pady=20)
#
#     def check_weather(self):
#         city = self.city_entry.get()
#
#         weather_info = f"Weather in {city}: Sunny, 25°C"
#         self.weather_label.config(text=weather_info)
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WeatherApp(root)
#     root.mainloop()

