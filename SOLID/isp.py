# Рассмотрим интерфейс PaymentProcessor с множеством методов:

class PaymentProcessor:
    def pay_with_card(self, amount, card_details):
        pass

    def pay_with_paypal(self, amount, paypal_email):
        pass

    def pay_with_bank_transfer(self, amount, bank_account_details):
        pass


# Не все классы, использующие PaymentProcessor, будут нуждаться во всех этих методах.
#
# Решение:
#
# Разделим интерфейс PaymentProcessor на несколько более специализированных интерфейсов:


class CardPaymentProcessor:
    def pay_with_card(self, amount, card_details):
        pass


class PaypalPaymentProcessor:
    def pay_with_paypal(self, amount, paypal_email):
        pass


class BankTransferPaymentProcessor:
    def pay_with_bank_transfer(self, amount, bank_account_details):
        pass
