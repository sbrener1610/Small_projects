import json
import datetime

def load_clients():

    with open('clients.json') as file:
        data=json.load(file)
        return(data)
    
def save_clients(clients):
    with open("clients.json","w") as file:
        json.dump(clients, file, indent=4)

def get_age(dob):
    date_of_birth = datetime.datetime.strptime(dob,"%Y-%m-%d")
    now=datetime.datetime.now()
    birthday_this_year=datetime.datetime(year=now.year,month=date_of_birth.month,day=date_of_birth.day)
    if now>birthday_this_year:
        age=now.year-date_of_birth.year
    else:
        age=now.year-date_of_birth.year-1
    return age

def add_client(clients,name,dob,balance):
    if clients:
        client_id=clients[-1]["client_id"]+1
    else:
        client_id=1
    clients.append({
        "client_id":client_id,
        "name":name,
        "dob":dob,
        "balance":balance
    })
    save_clients(clients)
    print("Client added successfully.")

def update_client(clients,client_id, name=None,dob=None, balance=None):
    for client in clients:
        if client["client_id"]==client_id:
            if name:
                client.update({"name":name})
            if dob:
                client.update({"dob":dob})
            if balance:
                client.update({"balance":balance})
                #client["balance"]=balance
            save_clients(clients)
            print("Client updated successfully.")
            return
    print("Customer does not exist.")
    

def delete_client(clients, client_id):

    for client in clients:
        if client["client_id"]==client_id:
            clients.remove(client)
            save_clients(clients)
            print("Client deleted successfully.")
            return
    print("Customer does not exist.")
    

def display_client(clients,client_id):
    for client in clients:
        if client["client_id"]==client_id:
            print(f"Client ID: {client['client_id']}")
            print(f"Client Name: {client['name']}")
            print(f"Client DOB: {client['dob']}")
            print(f"Client Age: {get_age(client['dob'])}")
            print(f"Client Balance: {client['balance']}")
            return
    print("Customer does not exist.")

def display_total(clients):
    total=sum(client['balance'] for client in clients)
    print("Total bank balance:", total)

def make_trasfer(clients, id_from, id_to, transfer_sum):
    for client_from in clients:
        if client_from["client_id"]==id_from:
            for client_to in clients:
                if client_to["client_id"]==id_to:
                    client_to["balance"]+=transfer_sum
                    client_from["balance"]-=transfer_sum
                    save_clients(clients)
                    print(f"Successfully transered {transfer_sum} from client with ID {id_from} to client with id {id_to}")
                    return
            print("Receipient does not exist.")    
            return
    print("Sender does not exist.")  



"""clients=load_clients()
print(clients)

update_client(clients,1,dob="1962-07-03",balance=50000)
print(clients)"""