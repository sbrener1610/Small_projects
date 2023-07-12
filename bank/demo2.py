import demo as banking
import datetime
import getch


def main():
    while True:
        print(
            """1: Add
2: Update
3: Delete
4: Display
5: Total
6: Transfer
7: Exit"""
        )

        print("\nSelect an option: ")
        option = getch.getch()

        if option == "1":
            name = input("Name: ")
            while True:  #Checks DOB is valid, repeats prompt until it is
                dob = input("DOB: ")
                try:
                    datetime.datetime.strptime(dob, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Try again")

            while True:
                try:  #Checks balance is valid, repeats prompt until it is
                    balance = float(input("Balance: "))
                    break
                except ValueError:
                    print("Try again")
            banking.add_client(clients, name, dob, balance)
            # print("Client added successfully.")
        elif option == "2":
            while True:    #Checks ID is valid, repeats prompt until it is
                try:
                    client_id = int(input("Client ID: "))
                    break
                except ValueError:
                    print("Try again")
            if banking.find_client(clients,client_id)==None:   #Checks user exists. If not - back to menu
                print("Customer does not exist.")    
                continue        
            name = input("Name: ")
            while True:   #again checks dob and balance for validity
                dob = input("DOB: ")
                if not dob:
                    break
                try:
                    datetime.datetime.strptime(dob, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Try again")
            while True:
                balance = input("Balance: ")
                if not balance:
                    break
                try:
                    balance = float(balance)
                    break
                except ValueError:
                    print("Try again")
            banking.update_client(clients, client_id, name, dob, balance)
            # print("Client updated successfully.")
        elif option == "3":
            while True:  #checks id is an integer. Check for existence is in the delete_client function
                try:
                    client_id = int(input("Client ID: "))
                    break
                except ValueError:
                    print("Try again")
            banking.delete_client(clients, client_id)
            # print("Client deleted successfully.")
        elif option == "4":
            while True:  #same as before
                try:
                    client_id = int(input("Client ID: "))
                    break
                except ValueError:
                    print("Try again")
            banking.display_client(clients, client_id)

        elif option == "5":
            banking.display_total(clients)
        elif option == "6":
            while True:  #checks both id's to be integers and checks if both users exist. If not integer prompts again, if does not exist - to the main menu
                try:
                    id_from = int(input("Sender ID: "))
                    break
                except ValueError:
                    print("Try again")
            if banking.find_client(clients,id_from)==None:
                print("Customer does not exist.")    
                continue 
            while True:
                try:
                    id_to = int(input("Receipient ID: "))
                    if id_to == id_from:
                        print("Don't waste my time.")
                        continue
                    break
                except ValueError:
                    print("Try again")
            if banking.find_client(clients,id_to)==None:
                print("Customer does not exist.")    
                continue 
            while True:  #checks transfer_sum is float. Prompts again if not.
                try:
                    transfer_sum = float(input("Sum: "))
                    break
                except ValueError:
                    print("Try again")

            banking.make_trasfer(clients, id_from, id_to, transfer_sum)
        elif option == "7":
            break


clients = banking.load_clients()
for client in clients:   
    """should never be necessary unless someone messes with the database manually.
       checking for validity of all database entries and demands to change them.
    """
    if not isinstance(client["client_id"],int):
        while True:
            try:
                client.update({"client_id":int(input(f"ID {client['client_id']} is not an integer. Change: "))})
                break
            except ValueError:
                print("Try again")    
    if not isinstance(client["balance"],float):
        while True:
            try:
                client.update({"balance":float(input(f"Balance of client ID {client['client_id']}, {client['balance']} is not a float. Change: "))})
                break
            except ValueError:
                print("Try again")    
    try:
        datetime.datetime.strptime(client["dob"], "%Y-%m-%d")
    except ValueError:
        while True:
            try:
                client.update({"dob":datetime.datetime.strftime(datetime.datetime.strptime(input(f"DOB of client ID {client['client_id']}, {client['dob']} is not a valid date. Change: "), "%Y-%m-%d"),"%Y-%m-%d")})
                break
            except ValueError:
                print("Try again")     
banking.save_clients(clients)   
clients.sort(key=lambda x:x["client_id"])  #in case ID's are not in ascending order after some un forseen actions
MAX_id=clients[-1]["client_id"]  #maximal ID
list_of_id=list(map(lambda x:x["client_id"], clients))  #creates list of ID's
if len(set(list_of_id))!=len(clients):   #checks for double ID's
    print("Fatal error, matching id's. Fix manually (y)/by default (n)")
    
    while True:
        option=getch.getch()
        if option.lower()=="y":       
           exit()
        if option.lower()=="n":  #scans list of ID's for repeated entries and changes the first one to the maximal ID+1
            for i in list_of_id:
                if list_of_id.count(i)!=1:
                    j=list_of_id.index(i)
                    clients[j].update({"client_id":MAX_id+1})
                    MAX_id+=1
                    list_of_id.pop(j)
                    list_of_id.insert(j,MAX_id)
            print("Fixed!")
            break
clients.sort(key=lambda x:x["client_id"]) #final sort
banking.save_clients(clients) #and save database
main()
