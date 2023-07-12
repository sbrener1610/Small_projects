import json
import datetime


def load_clients():  #loads _clients_ from database
    with open("clients.json") as file:
        data = json.load(file)
        return data


def save_clients(clients):   #updates database
    with open("clients.json", "w") as file:
        json.dump(clients, file, indent=4)


def get_age(dob):  #full years from _dob_ to today
    date_of_birth = datetime.datetime.strptime(dob, "%Y-%m-%d")
    now = datetime.datetime.now()
    birthday_this_year = datetime.datetime(
        year=now.year, month=date_of_birth.month, day=date_of_birth.day
    )
    if now > birthday_this_year:
        age = now.year - date_of_birth.year
    else:
        age = now.year - date_of_birth.year - 1
    return age


def add_client(clients, name, dob, balance):
    if clients:    #if clients not empty, takes the maximum available ID and adds 1
        client_id = clients[-1]["client_id"] + 1
    else:
        client_id = 1
    clients.append(         #Adds a client
        {"client_id": client_id, "name": name, "dob": dob, "balance": balance}
    )
    save_clients(clients)  #update database
    print("Client added successfully.")

def find_client(clients,client_id):
    list_of_clients=list(map(lambda x:x["client_id"], clients))  #list of id's
    try:
       return list_of_clients.index(client_id)   #returns the index in the database of the user with given ID. None if not found
    except ValueError:
        return None

def update_client(clients, client_id, name=None, dob=None, balance=None):
    #for client in clients:
    #    if client["client_id"] == client_id:
    j=find_client(clients,client_id)
    if j==None:   #checks id client exists, 
        print("Customer does not exist.")
    else:    
        if name:
            clients[j].update({"name": name})
        if dob:
            clients[j].update({"dob": dob})
        if balance:
            clients[j].update({"balance": balance})
                # client["balance"]=balance
        save_clients(clients)
        print("Client updated successfully.")
        
    


def delete_client(clients, client_id):
    j=find_client(clients,client_id)
    if j==None:   #checks id client exists, 
        print("Customer does not exist.")
    else:
        clients.pop(j)
        save_clients(clients)
        print("Client deleted successfully.")
        


def display_client(clients, client_id):
    j=find_client(clients,client_id)
    if j==None:   #checks id client exists, 
        print("Customer does not exist.")
    else:
            #print(f"Client ID: {client['client_id']}")
        print(f"Client Name: {clients[j]['name']}")
        print(f"Client DOB: {clients[j]['dob']}")
        print(f"Client Age: {get_age(clients[j]['dob'])}")
        print(f"Client Balance: {clients[j]['balance']}")
       


def display_total(clients):
    total = sum(client["balance"] for client in clients)
    print("Total bank balance:", total)


def make_trasfer(clients, id_from, id_to, transfer_sum,limit=0): #limit is never actually different from 0. At least now.
    j_from=find_client(clients,id_from)  #checks id client exists
    j_to=find_client(clients,id_to)
    if j_from==None:   
        print("Sender does not exist.")
       
    elif j_to==None:   #checks id client exists,
        print("Receipient does not exist.")
    else:
        if clients[j_from]["balance"]-transfer_sum>limit:  #checks limit
            clients[j_to]["balance"] += transfer_sum
            clients[j_from]["balance"] -= transfer_sum
            save_clients(clients)
            print(
                f"Successfully transered {transfer_sum} from client with ID {id_from} to client with ID {id_to}"
            )
        else:
            print("Not enough funds")
    


"""clients=load_clients()
print(clients)

update_client(clients,1,dob="1962-07-03",balance=50000)
print(clients)"""
