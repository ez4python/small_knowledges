# class EmailNotifier:
#     def send_notification(self, user, message):
#         # Отправка email-уведомления
#         pass

# Если нам потребуется добавить новый способ отправки уведомлений, например, SMS, нам придется изменить класс EmailNotifier.
#
# Решение:
#
# Используем абстрактный класс Notifier и создадим его наследников для разных типов уведомлений:

class Notifier:
    def send_notification(self, user, message):
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send_notification(self, user, message):
        # Sending email-notification
        pass


class SMSNotifier(Notifier):
    def send_notification(self, user, message):
        # Sending sms-notification
        pass
# Теперь, при необходимости добавить новый тип уведомления, достаточно создать новый класс-наследник Notifier,
# не изменяя существующий код.
