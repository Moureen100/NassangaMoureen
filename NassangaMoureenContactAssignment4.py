# Assignment ; Use Function-based Project to create a contact management system

'''
Your Tasks
Your job is to extend the functionality of the ContactManager class by 
implementing the following requirements. Ensure you do not break the existing features.

Task 1: Data Validation (20 Points)
Currently, a user can enter any text for a phone number or email. 
Modify the code to add basic validation:

Phone Validation: In add_contact and update_contact, 
ensure the phone number contains only digits and hyphens (e.g., "+256-701"). 
If it contains illegal characters, print an error message and cancel the operation.

Email Validation: Ensure that if an email is provided, it contains an @ symbol and a . (period).


Task 2: Advanced Search (25 Points)
The current Contacts method only filters by name and phone number.

Modify Contactss so that it can also search by email.

Write a helper method or modify the search printout so it displays the search results in a clean, 
user-friendly format rather than just returning a raw Python list of tuples.


Task 3: Interactive CLI Menu (35 Points)
Create an interactive Command Line Interface (CLI) loop inside a function called main(). 
When run, the program should present the user with a recurring menu until they choose to exit.

The menu should look similar to this:

=== Contact Manager Menu ===CRUD
1. Add Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. Search Contacts
6. List All Contacts
7. Exit
Choose an option (1-7):

Implement proper input handling for each menu item, 
prompting the user for necessary arguments (like name, phone, etc.) 
and passing them to your class methods.

Submission Guidelines:
1. Add a single python script to your github link, 
2. Submit a single Python file named name_contact_assignment.py.
'''

import re

class ContactManager:
    def __init__(self):
        # Storing contacts as a list of dictionaries for easier searching/formatting
        self.contacts = []

    def _validate_phone(self, phone):
        """Validates that phone contains only digits and hyphens."""
        pattern = r'^[0-9-]+$'
        return re.match(pattern, phone) is not None

    def _validate_email(self, email):
        """Validates that email contains @ and a period."""
        if not email:
            return True  # Email is optional
        return '@' in email and '.' in email

    def add_contact(self, name, phone, email=""):
        if not self._validate_phone(phone):
            print("Error: Invalid phone number. Only digits and hyphens are allowed.")
            return
        if not self._validate_email(email):
            print("Error: Invalid email address. Must include '@' and '.'.")
            return
        
        self.contacts.append({"name": name, "phone": phone, "email": email})
        print(f"Success: Contact '{name}' added.")

    def view_contact(self, name):
        results = [c for c in self.contacts if c['name'].lower() == name.lower()]
        if results:
            self.display_results(results)
        else:
            print(f"No contact found with the name '{name}'.")

    def update_contact(self, name, new_phone=None, new_email=None):
        for c in self.contacts:
            if c['name'].lower() == name.lower():
                if new_phone and not self._validate_phone(new_phone):
                    print("Error: Invalid phone number. Only digits and hyphens are allowed.")
                    return
                if new_email and not self._validate_email(new_email):
                    print("Error: Invalid email address. Must include '@' and '.'.")
                    return
                
                if new_phone:
                    c['phone'] = new_phone
                if new_email:
                    c['email'] = new_email
                print(f"Success: Contact '{name}' updated.")
                return
        print(f"No contact found with the name '{name}' to update.")

    def delete_contact(self, name):
        for i, c in enumerate(self.contacts):
            if c['name'].lower() == name.lower():
                del self.contacts[i]
                print(f"Success: Contact '{name}' deleted.")
                return
        print(f"No contact found with the name '{name}' to delete.")

    def search_contacts(self, query):
        """Searches by name, phone, or email and displays user-friendly results."""
        query = query.lower()
        results = []
        for c in self.contacts:
            if query in c['name'].lower() or query in c['phone'] or query in c['email'].lower():
                results.append(c)
        
        self.display_results(results)

    def display_results(self, results):
        """Helper method to print contacts in a clean, user-friendly format."""
        if not results:
            print("No matching contacts found.")
            return
        
        print("\n" + "="*45)
        print(f"{'Name':<15} | {'Phone':<12} | {'Email':<15}")
        print("="*45)
        for c in results:
            email_display = c['email'] if c['email'] else "N/A"
            print(f"{c['name']:<15} | {c['phone']:<12} | {email_display:<15}")
        print("="*45 + "\n")

    def list_all(self):
        self.display_results(self.contacts)


def main():
    manager = ContactManager()
    
    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == '1':
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone (digits & hyphens only): ").strip()
            email = input("Enter Email (optional): ").strip()
            manager.add_contact(name, phone, email)
            
        elif choice == '2':
            name = input("Enter Name to view: ").strip()
            manager.view_contact(name)
            
        elif choice == '3':
            name = input("Enter Name of contact to update: ").strip()
            print("Leave blank if you don't want to update a specific field.")
            new_phone = input("Enter New Phone: ").strip()
            new_email = input("Enter New Email: ").strip()
            manager.update_contact(name, new_phone if new_phone else None, new_email if new_email else None)
            
        elif choice == '4':
            name = input("Enter Name of contact to delete: ").strip()
            manager.delete_contact(name)
            
        elif choice == '5':
            query = input("Search by Name, Phone, or Email: ").strip()
            manager.search_contacts(query)
            
        elif choice == '6':
            manager.list_all()
            
        elif choice == '7':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()
