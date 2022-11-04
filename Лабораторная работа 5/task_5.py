import random
import string
def get_random_password(x= 8) -> str:

    str= string.ascii_uppercase + string.ascii_lowercase+ string.digits  # TODO написать функцию генерации случайных паролей
    str = random.sample(str,x)
    return str

print(get_random_password())