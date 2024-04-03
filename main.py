import hashlib

# Задаем строку с ФИО
full_name = input()

# Вычисляем хеш-сумму MD5 для строки
md5_hash = hashlib.md5(full_name.encode()).hexdigest()
print("MD5 хеш-сумма для строки:", md5_hash)

# Вычисляем оценку сложности пароля
password_strength = 0
password_length = len(full_name)
password_lowercase = False
password_uppercase = False
password_digits = 0
password_special_chars = 0

# Оценка длины пароля
if password_length <= 4:
    password_strength = 0
elif password_length <= 7:
    password_strength = 6
elif password_length <= 15:
    password_strength = 12
else:
    password_strength = 18

# Оценка наличия букв в пароле
for char in full_name:
    if char.islower():
        password_lowercase = True
    elif char.isupper():
        password_uppercase = True

if password_lowercase and password_uppercase:
    password_strength += 7
elif password_lowercase or password_uppercase:
    password_strength += 5

# Оценка наличия цифр в пароле
for char in full_name:
    if char.isdigit():
        password_digits += 1

if password_digits <= 2:
    password_strength += 5
else:
    password_strength += 7

# Оценка наличия специальных символов в пароле
for char in full_name:
    if char in "#$%@":
        password_special_chars += 1

if password_special_chars == 1:
    password_strength += 5
elif password_special_chars >= 2:
    password_strength += 10

# Оценка наличия букв, цифр и специальных символов в пароле
if password_lowercase and password_uppercase and password_digits > 0 and password_special_chars > 0:
    password_strength += 6
else:
    password_strength += 4

# Вывод оценки сложности пароля
if password_strength < 16:
    print("Пароль очень слабый")
elif password_strength < 25:
    print("Пароль слабый")
elif password_strength < 35:
    print("Пароль средний")
elif password_strength < 45:
    print("Пароль сильный")
else:
    print("Пароль очень сильный")
