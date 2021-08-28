total_donations = 0
def show_homepage():
    print("")
    print("          === DonateMe HomePage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register        |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.   Show Donations   |")
    print("------------------------------------------")
    print("|             5. EXIT                     |")
    print("------------------------------------------")

def donate(username):
    global total_donations
    donation_amt = float(input("Enter amount to donate: "))
    donation = f"{username} donated ${donation_amt}"
    total_donations += donation_amt
    print("Thank you for your donation!")
    return donation

def show_donations(donations):
    print("-------ALL DONATIONS-----------")
    if donations == []:
        print("No donations yet")
    else:
        for donation in donations:
            print(donation)
        print("total donations: $", total_donations)