class CustomerQueue:
    def __init__(self):
        self.vip_queue = []
        self.regular_queue = []

    def add_customer(self, name, is_vip=False):
        if is_vip:
            self.vip_queue.append(name)
            print(f"Added VIP customer: {name}")
        else:
            self.regular_queue.append(name)
            print(f"Added Regular customer: {name}")

    def serve_customer(self):
        for _ in range(len(self.vip_queue) + len(self.regular_queue)):
            if self.vip_queue:
                customer = self.vip_queue.pop(0)
                print(f"Serving VIP customer: {customer}")
            elif self.regular_queue:
                customer = self.regular_queue.pop(0)
                print(f"Serving Regular customer: {customer}")
            else:
                print("No customers to serve!")

cafe_queue = CustomerQueue()

cafe_queue.add_customer("Alice")
cafe_queue.add_customer("Bob", is_vip=True)
cafe_queue.add_customer("Charlie")
cafe_queue.add_customer("Diana", is_vip=True)

cafe_queue.serve_customer()

