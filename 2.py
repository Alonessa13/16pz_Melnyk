def run_task2():
    def run_task2():
        # Принцип OCP — Клас має бути відкритим для розширення, але закритим для змін

        # Базовий клас для всіх типів оплат
        class PaymentMethod:
            def pay(self, amount):
                raise NotImplementedError("Метод потрібно реалізувати в підкласі")

        # Оплата кредитною карткою
        class CreditCardPayment(PaymentMethod):
            def pay(self, amount):
                print(f"Оплата {amount} грн кредитною карткою")

        # Оплата через PayPal
        class PayPalPayment(PaymentMethod):
            def pay(self, amount):
                print(f"Оплата {amount} грн через PayPal")

        # Оплата криптовалютою
        class CryptoPayment(PaymentMethod):
            def pay(self, amount):
                print(f"Оплата {amount} грн криптовалютою")

        # Клас обробляє оплату, але не знає, який саме тип оплати — це реалізується в підкласах
        class PaymentProcessor:
            def process(self, payment_method: PaymentMethod, amount):
                payment_method.pay(amount)

        # === Демонстрація ===

        processor = PaymentProcessor()

        # Можемо легко додавати нові методи оплати, не змінюючи існуючий код
        processor.process(CreditCardPayment(), 100)
        processor.process(PayPalPayment(), 200)
        processor.process(CryptoPayment(), 300)

    class PaymentMethod:
        def pay(self, amount):
            raise NotImplementedError()

    class CreditCardPayment(PaymentMethod):
        def pay(self, amount):
            print(f"Сплачено {amount} грн через кредитну картку")

    class PayPalPayment(PaymentMethod):
        def pay(self, amount):
            print(f"Сплачено {amount} грн через PayPal")

    class CryptoPayment(PaymentMethod):
        def pay(self, amount):
            print(f"Сплачено {amount} грн криптовалютою")

    class PaymentProcessor:
        def process(self, payment_method: PaymentMethod, amount):
            payment_method.pay(amount)

    # --- Ввід користувача ---
    print("\n=== Виберіть спосіб оплати ===")
    print("1 - Кредитна картка")
    print("2 - PayPal")
    print("3 - Криптовалюта")
    method = input("Ваш вибір: ")

    try:
        amount = float(input("Введіть суму оплати: "))
    except ValueError:
        print("Помилка: сума має бути числом.")
        return

    processor = PaymentProcessor()

    if method == "1":
        processor.process(CreditCardPayment(), amount)
    elif method == "2":
        processor.process(PayPalPayment(), amount)
    elif method == "3":
        processor.process(CryptoPayment(), amount)
    else:
        print("Невідомий спосіб оплати.")
