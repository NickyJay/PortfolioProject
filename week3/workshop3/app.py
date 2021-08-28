from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
from donations_pkg import homepage

database = {"admin": "password123"}
donations = []
authorized_user = ""

show_homepage()

if authorized_user =="":
    print("You must be logged in to donate")
else:
    print("Logged in as: ", authorized_user)

while True:
    choice = input("Please Enter a choice: ")
    if choice == "1":
        username = input("Please Enter Username: ").lower()
        password = input("Please Enter password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("Please Enter Username: ").lower()
        password = input("Please Enter password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password
    elif choice == "3":
        if authorized_user != "":
            donation = donate(authorized_user)
            donations.append(donation)
        else:
            print("You are not logged in")

    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("Leaving DonateMe")
        break
    else:
        print("choose a valid option")

