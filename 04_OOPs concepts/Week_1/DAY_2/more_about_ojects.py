class wallet:
    def __init__(self, currency, amount):
        self.currency=str(currency)
        self.amount=int(amount)
    def is_wealthier_than(self, other_wallet):
        return self.amount>other_wallet.amount
def compare_wallets(w1,w2):
    if w1.amount>w2.amount:
        print(f"{w1.currency} wallet has more money: {w1.amount}")
    else:
        print(f"{w2.currency} wallet has more money: {w2.amount}")
my_wallet=wallet("USD", 500)
friend_wallet=wallet("EUR", 150)
compare_wallets(my_wallet, friend_wallet)
print(my_wallet.is_wealthier_than(friend_wallet))

class laptop:
    def __init__(self, brand, ram):
        self.brand=brand
        self.ram=ram
    def show(self):
        print(f"{self.brand} laptop has {self.ram} GB RAM")
brands = ["Dell", "HP", "MacBook"]
rams = [8, 16, 32]
zipper = zip(brands, rams)
laptops =[laptop(brand, ram) for brand, ram in zipper]
for lap in laptops:
    lap.show()


# CHALLENGE 3: THE SYSTEM MONITOR (COMPLETED & SOLVED)

class server:
    def __init__(self, server_id, cpu_load):
        self.server_id = server_id
        self.cpu_load = cpu_load


def over_loaded_servers(server_list):
    overloaded = []
    for srv in server_list:
        if srv.cpu_load > 80:
            overloaded.append(srv.server_id)
    return overloaded


# 1. First, define the raw data arrays
ids = ["server1", "server2", "server3", "server4"]
loads = [85, 75, 90, 70]

# 2. Second, run the single-line factory conveyor belt using the raw data
servers = [server(srv_id, load) for srv_id, load in zip(ids, loads)]

# 3. Finally, pass the clean list of objects into the analyzer function
overloaded_list = over_loaded_servers(servers)

# 4. Print the final result string
print(f"Overloaded servers: {overloaded_list}")
