# 5. Принцип инверсии зависимостей (DIP):
#
# Представим класс Order, который напрямую зависит от класса PaymentProcessor для обработки платежей:


class Order:
    def __init__(self, items, payment_processor):
        self.items = items
        self.payment_processor = payment_processor

    def process_payment(self):
        self.payment_processor.pay(self.total_amount)


class PaymentService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def pay(self, amount):
        self.payment_processor.pay(amount)


class CardPaymentService(PaymentService):
    def __init__(self, card_payment_processor):
        super().__init__(card_payment_processor)


class PaypalPaymentService(PaymentService):
    def __init__(self, paypal_payment_processor):
        super().__init__(paypal_payment_processor)


class BankTransferPaymentService(PaymentService):
    def __init__(self, bank_transfer_payment_processor):
        super().__init__(bank_transfer_payment_processor)

# Теперь класс Order не зависит от конкретной реализации PaymentProcessor,
# а работает с абстрактным интерфейсом PaymentService.
