#2


def user_param(name='Kate', surname='Johnson', age='2000', city='London', email='k.johnson@gmail.com', phone='+345689784'):
    return ("Имя: {}  Фамилия: {}  Возраст: {}  Город: {}  Почта: {} Телефон: {}".format(name, surname, age, city, email, phone))


print(user_param())