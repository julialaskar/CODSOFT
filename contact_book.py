# contact_book.py

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email=None, address=None):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the book.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']}: {contact['phone']}")

    def search_contact(self, search_term):
        found = []
        for contact in self.contacts:
            if (search_term.lower() in contact["name"].lower()) or (search_term in contact["phone"]):
                found.append(contact)
        
        if not found:
            print("No matching contacts found.")
        else:
            print("\nMatching Contacts:")
            for i, contact in enumerate(found, 1):
                print(f"{i}. Name: {contact['name']}")
                print(f"   Phone: {contact['phone']}")
                if contact['email']:
                    print(f"   Email: {contact['email']}")
                if contact['address']:
                    print(f"   Address: {contact['address']}")
                print()

    def update_contact(self, contact_num):
        try:
            if 1 <= contact_num <= len(self.contacts):
                contact = self.contacts[contact_num-1]
                print(f"\nEditing Contact: {contact['name']}")
                print("Leave blank to keep current value.")
                
                name = input(f"Name [{contact['name']}]: ") or contact['name']
                phone = input(f"Phone [{contact['phone']}]: ") or contact['phone']
                email = input(f"Email [{contact['email']}]: ") or contact['email']
                address = input(f"Address [{contact['address']}]: ") or contact['address']
                
                self.contacts[contact_num-1] = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                }
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_contact(self, contact_num):
        try:
            if 1 <= contact_num <= len(self.contacts):
                removed_contact = self.contacts.pop(contact_num-1)
                print(f"Contact '{removed_contact['name']}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            contact_book.add_contact(name, phone, email or None, address or None)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            contact_book.view_contacts()
            contact_num = int(input("Enter contact number to update: "))
            contact_book.update_contact(contact_num)
        elif choice == "5":
            contact_book.view_contacts()
            contact_num = int(input("Enter contact number to delete: "))
            contact_book.delete_contact(contact_num)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
