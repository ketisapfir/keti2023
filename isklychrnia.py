try:
    a = int|('kirill')
except ZeroDivisionError:
    print('на 0 делить нельзя')
except NameError:
    print('переменнаяне задана')
except ValueError:
    print('Невозможно привести к числу')
except TypeError:
    print('ошибка типа данных')
except:
    print('Произошла ошибка')