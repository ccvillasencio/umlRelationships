from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


class GCashPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing P{amount:.2f} via GCash.")
        return True


# --- Running the code ---
gateway = GCashPayment()

success = gateway.process_payment(250.75)

print(f"Payment Status: {success}")
