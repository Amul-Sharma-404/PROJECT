# conatct book using python oop
'''
this is the basic project done in python we can improve it by appling the frontend code
for front end code
using html,css,js,and some bootstrap

for backend use python 

@t 2024 this code contain copyright statament if you use it without asling the owner 
'''
import os
import requests

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print(f"Found contact - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                return contact
        print("Contact not found.")
        return None

    def edit_contact(self, name, new_name=None, new_phone=None, new_email=None):
        contact = self.search_contact(name)
        if contact:
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            print(f"Contact {name} updated successfully.")

    def delete_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact {name} deleted successfully.")


def main():
    book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("SELECT: ")

        if choice == '1':
            name = input("ENTER THE NAME: ")
            phone = input("ENTER THE PHONE NUMBER : ")
            email = input("ENTER YOUR EMAIL : ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to edit: ")
            new_name = input("Enter new name (or leave blank to keep current): ")
            new_phone = input("Enter new phone (or leave blank to keep current): ")
            new_email = input("Enter new email (or leave blank to keep current): ")
            book.edit_contact(name, new_name, new_phone, new_email)
        elif choice == '5':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
