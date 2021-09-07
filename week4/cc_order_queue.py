class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
    def take_order(self, customer, flavor, scoops):
        order = {}
        if flavor not in self.flavors:
            print("Flavor unavailable")
        elif scoops in range(1, 4):
            order[customer] = (flavor, scoops)
            self.orders.enqueue(order)
            print("Order Created")
        else:
            print("Hmm try again and choose 1-3 scoops \n")
    def show_all_orders(self):
        print("All Pending ice cream orders: ")
        for order in self.orders.items:
            name = list(order.keys())[0]
            print("Customer: ", name, "-- Flavor:", order[name][0], "-- Scoops: ", order[name][1])
    def next_order(self):
        next_order= self.orders.dequeue()
        name = list(next_order.keys())[0]
        print(f"\nNext order => {name} has order {next_order[name][1]} scoop(s) of {next_order[name][0]} ice cream! ")


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()