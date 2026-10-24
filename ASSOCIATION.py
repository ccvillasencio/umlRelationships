class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []


class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        customer.orders.append(self)


# --- Running the code ---
alice = Customer("Alice")

order_1 = Order(101, alice)
order_2 = Order(102, alice)

print(f"Customer Profile: {alice.name}")
print("Linked orders tracked inside Customer:")

for order in alice.orders:
    print(f" - Order ID: {order.order_id}")

print(
    f"\nOrder #101 belongs to customer: "
    f"{order_1.customer.name}"
)
