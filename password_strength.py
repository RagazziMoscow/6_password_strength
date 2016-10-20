import re


## Проверяет чувствительность к регистру
def check_case_sensitivity(string):
	if(string.islower()):
		return False
	if(string.isupper()):
		return False
	return True

## Проверяет, есть ли цифры в строке
def is_numerical_digits(string):
    if(re.search('[0-9]', string) is not None):
    	return True
    else:
    	return False
## Проверяет, есть ли метасимволы в строке
def is_metacharacters(string):
	if(re.search('\#|\$|\@|\%|\^|\&|\?|\!', string) is not None):
		return True
	else:
		return False
## Проверяет, является ли пароль числом
def is_number(string):
	if(string.isnumeric()):
		return True
	else:
		return False
## Проверяет, является ли пароль только строкой
def is_alpha_string(string):
	if(string.isalpha()):
		return True
	else:
		return False

## Даёт оценку паролю
def get_password_strength(password):
	# Если пароль пустой
	if(password is ""):
		return None

	# Если пароль непустой
	strength_value = 1
	if(is_number(password) or is_alpha_string(password)):
		return strength_value
	if(check_case_sensitivity(password)):
		strength_value+=3
	if(is_numerical_digits(password)):
		strength_value+=2
	if(is_metacharacters(password)):
		strength_value+=4
	return strength_value
    

def main():
    print("Введите пароль:")
    password = input()
    if(get_password_strength(password) is not None):
        print("Оценка введённого пароля: ", get_password_strength(password))
    else:
    	print("Введите непустой пароль")

if __name__ == '__main__':
    main()