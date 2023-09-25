from collections import Counter


class Customer:
    def __init__(self, desired_shoe_nr, willing_to_pay):
        self.desired_shoe_nr = desired_shoe_nr
        self.willing_to_pay = willing_to_pay


class ShoeStore:
    def __init__(self, shoes_quantity, shoes_list):
        self.shoes_inventory = Counter(shoes_list)
        self.validate_input(shoes_quantity, len(shoes_list))
        self.revenue = 0

    def validate_input(self, shoes_quantity, num_shoes):
        if not (1 < shoes_quantity <= 1000 and 1 < num_shoes <= 1000):
            raise ValueError('Shoes quantity and shoes list length must be between 2 and 1000')
        if any(size < 2 or size > 20 for size in self.shoes_inventory):
            raise ValueError('Invalid shoe sizes. Sizes must be between 2 and 20.')

    def customer_transaction(self, customer):
        if customer.desired_shoe_nr in self.shoes_inventory and 20 <= customer.willing_to_pay <= 100:
            self.shoes_inventory[customer.desired_shoe_nr] -= 1
            self.revenue += customer.willing_to_pay
            if self.shoes_inventory[customer.desired_shoe_nr] == 0:
                del self.shoes_inventory[customer.desired_shoe_nr]

    def process_customers(self, customers):
        for customer in customers:
            self.customer_transaction(customer)

    def get_revenue(self):
        return self.revenue


def main():
    shoes_quantity = int(input("Enter the initial quantity of shoes: "))
    shoes_list = list(map(int, input("Enter the list of shoe sizes: ").split()))
    customers_number = int(input("Enter the number of customers: "))

    customers = []
    for _ in range(customers_number):
        desired_shoe_nr, willing_to_pay = map(int, input(
            "Enter desired shoe size and willing to pay (e.g., 8 50): ").split())
        customer = Customer(desired_shoe_nr, willing_to_pay)
        customers.append(customer)

    store = ShoeStore(shoes_quantity, shoes_list)
    store.process_customers(customers)
    print("Total revenue:", store.get_revenue())


if __name__ == '__main__':
    main()