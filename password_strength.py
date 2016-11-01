import re


# Проверяет чувствительность к регистру
def check_case_sensitivity(pass_string):
    return (False if(pass_string.islower() or pass_string.isupper()) else True)


# Проверяет, есть ли цифры в строке
def is_numerical_digits(pass_string):
    return (True if(re.search('[0-9]', pass_string) is not None) else False)


# Проверяет, есть ли метасимволы в строке
def is_metacharacters(pass_string):
    return (True if(re.search('\#|\$|\@|\%|\^|\&|\?|\!', pass_string) is not None) else False)


# Проверяет, является ли пароль числом
def is_number(pass_string):
    return(True if(pass_string.isnumeric()) else False)


# Проверяет, является ли пароль только строкой
def is_alpha_string(pass_string):
    return (True if(pass_string.isalpha()) else False)


# Считает оценку паролю
def get_password_strength(password):
    # Если пароль пустой
    if(password is ""):
        return None

    # Если пароль непустой
    strength_value = 1

    # Если пароль - это строка или число
    if(is_number(password) or is_alpha_string(password)):
        return strength_value

    if(check_case_sensitivity(password)):
        strength_value += 3
    if(is_numerical_digits(password)):
        strength_value += 2
    if(is_metacharacters(password)):
        strength_value += 4
    return strength_value


def main():

    password = input("Введите пароль:\n")
    if(get_password_strength(password) is not None):
        print("Оценка введённого пароля: ", get_password_strength(password))
    else:
        print("Введите непустой пароль")

if __name__ == '__main__':
    main()