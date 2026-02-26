from user import User

my_user = User("Александр", "Силицкий")

print("Имя:")
my_user.print_first_name()

print("\nФамилия:")
my_user.print_last_name()

print("\nПолное имя:")
my_user.print_full_name()

input("\nНажмите Enter для выхода...")
