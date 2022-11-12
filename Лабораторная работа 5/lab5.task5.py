# TODO написать функцию генерации случайных паролей
# сразу возвращаем список, склееный в строку
# укажем на тип и значение по умолчанию для аргумента

def get_random_password(len_:int = 8) -> str:
     return "".join(random.sample(string.ascii_uppercase +
                                  string.ascii_lowercase +
                                  string.digits,
                                  len_))

import string, random

print(get_random_password())
