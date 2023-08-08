python
import getpass

def login():
    username = input("Введите имя пользователя: ")
    password = getpass.getpass("Введите пароль: ")

    # Проверка имени пользователя и пароля
    if username == "admin" and password == "password":
        print("Авторизация успешна!")
        # Добавьте свой код здесь для выполнения после успешной авторизации
    else:
        print("Неверное имя пользователя или пароль.")

login()

print("succefly logged")
