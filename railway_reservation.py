
'''
Railway Reservation Program in binary format
the function uses the various commands in pickle module for:
1. Ticket booking/reservation
2. Waiting list display
3. Specific ticket display
4. Modification in ticket
5. Cancellation of ticket
'''


import pickle
import random


def menu():
    choice = 0
    while choice != 6:
        print("\n\n\n")
        print("*************************************************************\n")
        print("<<<<<<< WELCOME TO INDIAN RAILWAYS SERVICES >>>>>>>\n")
        print("<< RAILWAY RESERVATION SYSTEM >>\n")
        print("<<<<<<< MAIN MENU >>>>>>>\n\n")
        print("1. Book a ticket.\n")
        print("2. Review Waiting List.\n")
        print("3. Search Ticket.\n")
        print("4. Modify details of your ticket.\n")
        print("5. Cancellation.\n")
        print("6. Quit.\n\n")
        print("**************************************************************\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            book_ticket()
        elif choice == 2:
            waiting_list()
        elif choice == 3:
            search_ticket()
        elif choice == 4:
            modify_ticket()
        elif choice == 5:
            cancel()
        elif choice == 6:
            print(">>>> THANK FOR CHOOSING INDIAN RAILWAYS FOR A SAFE JOURNEY! <<<<")


def book_ticket():

    ticket_list = []

    for i in range(4):
        ticket_num = random.randint(10000,100000)
        name = input("Enter your name: ")
        age = int(input("Enter your age:  "))
        arrive_dest = input("Enter the final destination: ")
        depart_dest = input("Enter your leaving destination: ")
        date_depart = input("Enter the date of departure: ")
        class_travel = int(input("Enter the class you wish to travel by: "))
        railway_data = [ticket_num, name, age, arrive_dest, depart_dest, date_depart, class_travel]

        ticket_list.append(railway_data)
        print("Your ticket number is {}".format(ticket_num))
        print('\n')

        outfile = open("railway.dat", 'wb')
        pickle.dump(ticket_list, outfile)
        outfile.close()


def waiting_list():
    print('\n')
    print("[ticket_num,    name,   age,    arrive_dest,    depart_dest,  date_depart,  class_travel]")
    print('\n')
    infile = open("railway.dat",'rb')
    ticket_list = pickle.load(infile)
    for i in range(len(ticket_list)):
        print(ticket_list[i],'\n')
    infile.close()


def search_ticket():
    found_index = 0
    print("\n\n<< SEARCH MENU >>\n\n")
    print("1. Search by ticket number")
    print("2. Search by name")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ticket_num = int(input("Enter your ticket number: "))
    else:
        name = input("Enter name of the person to search: ")

    while True:
        try:
            infile = open("railway.dat",'rb')
            ticket_list = pickle.load(infile)
            infile.close()
            break
        except:
            ticket_list = []
            break

    print("\n Searched Result:")
    for search_entry in ticket_list:
        if choice == 1 and ticket_num == search_entry[0]:
            print(search_entry)
            found_index = 1
        elif choice == 2 and name == search_entry[1]:
            print(search_entry)
            found_index = 1

    if found_index == 0:
        print("No match found!")


def modify_ticket():

    FoundIndex = -1

    print("\n\n<< MODIFY MENU >>\n\n")
    print("1. Modify Destination of Arrival.\n")
    print("2. Modify Destination of Departure\n")
    print("3. Modify Date of Departure.\n")
    print("4. Modify Class of travelling ")
    Ch = int(input("Please Enter your choice: "))

    if Ch == 1:
        regno = int(input("Please Enter your PNR number: "))
    elif Ch==2:
        regno = int(input("Please Enter your PNR number: "))
    elif Ch==3:
        regno = int(input("Please Enter your PNR number: "))
    else:
        regno = int(input("Please Enter your PNR number: "))

    while True:
        try:
            inFile = open("railway.dat", "rb")
            List = pickle.load(inFile)
            inFile.close()
            break
        except:
            List = []
            break

    for i in range(len(List)):
        L = List[i]
        if (Ch == 1 and regno==L[0]):
            FoundIndex = i
            old_arrial = List[i][4]
            new_arrival = input("Enter the New Destination for Arrival: ")
            List[i][4] = new_arrival
            print(old_arrial, " has been modified as ", new_arrival)
            break

        elif (Ch == 2 and regno== L[0]):
            FoundIndex = i
            old_depart = List[i][3]
            new_depart = input("Enter the Modified Name of the Person: ")
            List[i][3] = new_depart
            print(old_depart, " has been modified as ", new_depart)
            break

        elif (Ch==3 and regno==L[0]):
            FoundIndex=i
            old_date = List[i][5]
            new_date = input("Enter the modified date of departure(MM/DD/YYYY): ")
            List[i][5] = new_date
            print(old_date, " has been modified as ", new_date)
            break

        elif (Ch==4 and regno==L[0]):
            FoundIndex = i
            old_class = List[i][6]
            new_class = int(input("Enter the modified class of traveling(1/2/3): "))
            if new_class in (1,4):
                List[i][6] = new_class
                print(old_class, " has been modified as ", new_class)
            else:
                print("Please enter valid choice!!")
            break

    if (FoundIndex == -1):
        print("No Match Found!")
    else:
        outFile = open("railway.dat", "wb")
        pickle.dump(List, outFile)
        outFile.close()

def cancel():
    regno = int(input("Please enter your PNR number: "))
    FoundIndex = -1
    while True:
        try:
            inFile = open("railway.dat", "rb")
            List = pickle.load(inFile)
            inFile.close()
            break
        except:
            List = []
            break
    for i in range(len(List)):
        L=List[i]
        if regno==L[0] :
            FoundIndex = i
            break
    if FoundIndex==-1 :
        print("No match found!")
    else:
        Data = List.pop(FoundIndex)
        print("The Ticket ",regno," has been cancelled!")
        outFile = open("railway.dat", "wb")
        pickle.dump(List, outFile)
        outFile.close()

menu()


