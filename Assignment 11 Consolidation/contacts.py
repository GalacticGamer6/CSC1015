#Neeraav Ranjit
#12 May 2024
#A simple contacts progam

import os.path

def read_contacts(file_path):

    contacts = []

    if(path_exists(file_path)):
        #read all the contacts as a list, then append it to to a big list
        f = open(file_path,"r")
        for line in f:

            current_contact = []
            current_line = str(line).rstrip().split(",")
            #append the name number and email
            current_contact.append(current_line[0])
            current_contact.append(current_line[1])
            current_contact.append(current_line[2])

            #now we add it to the ovreall lists
            contacts.append(current_contact)

    return contacts

def path_exists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False

def add_contact(file_path,name,phone,email):
    #check if it exists first
    if (contact_exists(file_path,name,phone,email)):
        print("Contact already exists.")
    else:
        file = open(file_path,"a")
        file.write(name+","+phone+","+email+"\n")
        file.close()
        print("Contact added successfully.")

def custom_sort(contacts):
    #cool lambda function shortcut we learnt
    sorted_list = sorted(contacts, key=lambda x: x[0])
    return sorted_list


def contact_exists(file_path,name,phone,email):
    #because phone number and email are unique identidiers, names are not unique
    if not((search_contact(file_path,phone) or search_contact(file_path,email)) == None):
        return True
def print_search(search_results):
    print("Found contact(s):")
    print("="*60)
    print("| "+"{:<21}".format("Name")+"| "+"{:<16}".format("Phone")+"| "+"{:<26}".format("Email")+"|")
    print("="*60)

    for i in range(len(search_results)):
        print("| "+"{:<21}".format(search_results[i][0])+"| "+"{:<16}".format(search_results[i][1])+"| "+"{:<26}".format(search_results[i][2])+"|")
        print("------------------------------------------------------------")

def search_contact(file_path,query):
        #idek why im dual returning, all i know is that its gonna save me hours of suffering
    contacts = custom_sort(read_contacts(file_path))

    #1st, we determine what we need to search for
    if "@" in query:
        #search by email
        for i in range(len(contacts)):
            if contacts[i][2] == query:
                return contacts[i]
    elif query[0] == "0":
        #search by number
        for i in range(len(contacts)):
            if contacts[i][1] == query:
                return contacts[i]
    else:
        #search by name
        output = []
        for i in range(len(contacts)):
            if query in contacts[i][0]:
                output.append(contacts[i])
        return output

#literally just gonna copy this from assignment 5

def list_contacts(file_path):

    contacts = custom_sort(read_contacts(file_path))

    custom_sort(contacts)

    print("List of contacts:")
    print("="*60)
    print("| "+"{:<21}".format("Name")+"| "+"{:<16}".format("Phone")+"| "+"{:<26}".format("Email")+"|")
    print("="*60)

    for i in range(len(contacts)):
        print("| "+"{:<21}".format(contacts[i][0])+"| "+"{:<16}".format(contacts[i][1])+"| "+"{:<26}".format(contacts[i][2])+"|")
        print("------------------------------------------------------------")


def choice():

    print("1. Add Contact\n2. Search Contact\n3. List Contacts\n4. Exit")
    #for some dumb reason this has to be seperated or else automarker goes into cardiac arrest
    choice = eval(input("Enter your choice: "))
    return choice

if __name__ == '__main__':

    file_name = input("Enter the name for the contacts file:\n") + ".txt"
    #if the file dont exist, then make one + some spacing for amaathuba
    if not path_exists(file_name):
        f = open(file_name, "w")
        print("Contacts file \'" + file_name + "\' created.")
    print()

    user_choice = choice()
    while user_choice != 4:

        # add the contact, get the tings
        if user_choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            add_contact(file_name,name,phone, email)
            print()
        #now for a pesky search
        elif user_choice == 2:
            info = input("Enter first name, last name, phone number, or email to search:\n")

            #first check if it exists
            if search_contact(file_name,info) == None or len(search_contact(file_name,info)) == 0:
                print("No contact found.")
                print()
            else:
                print_search(search_contact(file_name,info))
                print()
        elif user_choice == 3:
            print()
            list_contacts(file_name)
            print()

        user_choice = choice()

    print("Exiting program.",end="")
