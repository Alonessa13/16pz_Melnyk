def run_task3():
    # Принцип ISP — клієнти не повинні залежати від інтерфейсів, які вони не використовують
    # Принцип DIP — залежності повинні будуватися на абстракціях, а не на конкретних класах

    # Базовий інтерфейс повідомлень
    class Notifier:
        def notify(self, message):
            raise NotImplementedError()

    # Клас, який надсилає Email
    class EmailNotifier(Notifier):
        def notify(self, message):
            print(f"Email: {message}")

    # Клас, який надсилає SMS
    class SMSNotifier(Notifier):
        def notify(self, message):
            print(f"SMS: {message}")

    # Клас, який надсилає Push-повідомлення
    class PushNotifier(Notifier):
        def notify(self, message):
            print(f"Push-повідомлення: {message}")

    # Клас системи оповіщень
    class AlertSystem:
        def __init__(self, notifiers: list):
            self.notifiers = notifiers # Ми використовуємо список інтерфейсів, а не конкретні класи

        def send_alert(self, message):
            for notifier in self.notifiers:
                notifier.notify(message)

    # --- Ввід користувача ---
    message = input("\nВведіть текст сповіщення: ")

    print("\nВиберіть способи надсилання (через кому):")
    print("1 - Email")
    print("2 - SMS")
    print("3 - Push")
    selected = input("Ваш вибір (наприклад: 1,3): ").split(",")

    notifiers = []

    for s in selected:
        s = s.strip()
        if s == "1":
            notifiers.append(EmailNotifier())
        elif s == "2":
            notifiers.append(SMSNotifier())
        elif s == "3":
            notifiers.append(PushNotifier())

    if not notifiers:
        print("Не вибрано жодного методу сповіщення.")
        return

    alerts = AlertSystem(notifiers)
    alerts.send_alert(message)
