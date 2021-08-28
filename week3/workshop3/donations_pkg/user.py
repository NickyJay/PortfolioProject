def login(database, username, password):
    if username in database and password == database[username]:
        print(f"Welcome {username}")
        return username
    if username in database and password is not database[username]:
        print("Sorry, does not match. ")
        return ""
    else:
        print(username, " not found, please register!")
        return ""

def register(database, username, password):
    if username in database.keys():
        print("Username already registered")
        return ""
    elif len(username) >10:
        print("Username must be shorter than 10 characters")
        return ""
    elif len(password) <5:
        print("Password must be at least 5 characters")
        return ""
    else:
        print(f"{username} has been registered")
        return username
    




