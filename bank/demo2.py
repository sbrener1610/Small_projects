import demo as banking
import datetime
import getch

def main():
    while True:

        print("""1: Add
2: Update
3: Delete
4: Display
5: Total
6: Transfer
7: Exit""")

        print("\nSelect an option: ")
        option = getch.getch()

        if option == "1":
            name = input("Name: ")
            while True:
                dob = input("DOB: ")
                try:
                    datetime.datetime.strptime(dob,"%Y-%m-%d")
                    break
                except ValueError:
                    print("Try again")
                
            while True:
                try:
                    balance = float(input("Balance: "))
                    break
                except ValueError:
                    print("Try again")
            banking.add_client(clients, name, dob, balance)
            #print("Client added successfully.")
        elif option == "2":
            client_id=int(input("Client ID: "))
            name = input("Name: ")
            while True:
                dob = input("DOB: ")
                if not dob:
                    break
                try:
                    datetime.datetime.strptime(dob,"%Y-%m-%d")
                    break
                except ValueError:
                    print("Try again")
            while True:
                    balance = input("Balance: ")
                    if not balance:
                        break
                    try:    
                       balance=float(balance)
                       break
                    except TypeError:
                        print("Try again")
            banking.update_client(clients,client_id,name,dob,balance)
            #print("Client updated successfully.")
        elif option == "3":
            while True:
                try:
                    client_id=int(input("Client ID: "))
                    break
                except ValueError:
                    print("Try again")
            banking.delete_client(clients,client_id)
            #print("Client deleted successfully.")
        elif option == "4":
            while True:
                try:
                    client_id=int(input("Client ID: "))
                    break
                except ValueError:
                    print("Try again")
            banking.display_client(clients,client_id)
            
        elif option == "5":
            banking.display_total(clients)
        elif option=="6":
            while True:
                try:
                    id_from=int(input("Sender ID: "))
                    break
                except ValueError:
                    print("Try again")
            while True:
                try:
                    id_to=int(input("Receipient ID: "))
                    if id_to==id_from:
                        print("Don't waste my time.")
                        continue
                    break
                except ValueError:
                    print("Try again")
            while True:
                try:
                    transfer_sum=float(input("Sum: "))
                    break
                except ValueError:
                    print("Try again")
            
            banking.make_trasfer(clients,id_from,id_to,transfer_sum)
        elif option == "7":
            break

clients=banking.load_clients()
main()
        