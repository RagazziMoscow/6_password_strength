import re


def check_case_sensitivity(pass_string):
    return not(pass_string.islower() or pass_string.isupper())


def is_numerical_digits(pass_string):
    return bool(re.search('[0-9]', pass_string))


def is_metacharacters(pass_string):
    return bool(re.search('\#|\$|\@|\%|\^|\&|\?|\!', pass_string))


def is_number(pass_string):
    return pass_string.isnumeric()


def is_alpha_string(pass_string):
    return pass_string.isalpha()


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