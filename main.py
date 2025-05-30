from run_task1_pz import run_task1
from run_task2_pz import run_task2
from run_task3_pz import run_task3

def show_menu():
    print("=== Меню вибору завдання ===")
    print("1 - Завдання 1 (SRP)")
    print("2 - Завдання 2 (OCP)")
    print("3 - Завдання 3 (ISP + DIP)")
    print("0 - Вихід")

def main():
    while True:
        show_menu()
        choice = input("Оберіть номер завдання: ")

        if choice == "1":
            run_task1()
        elif choice == "2":
            run_task2()
        elif choice == "3":
            run_task3()
        elif choice == "0":
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
