# print('hello world!')

# def points_of_the_plane(x, y):
#     x = x
#     y = y
#     if x > 0 and y > 0:
#         print('I')
#     if x < 0 and y > 0:
#         print('II')
#     if x < 0 and y < 0:
#         print('III')
#     if x > 0 and y < 0:
#         print('IV')
#     else:
#         print()

# x = int(input('введите координаты x'))
# y = int(input('введите координаты y'))

# points_of_the_plane(x, y)

# def ask_password():
#     password = 'password'
#     for i in range(3):
#         bbedite_parolb = input('введите пароль')
#         if bbedite_parolb == password:
#             print('верно, проходите:)')
#             break
#         else:
#             print('неверно, попробуйте еще раз:(')

# ask_password()

def check_string_brackets(input_string):
    balance = 0
    for char in input_string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            print('no')
            return
        if balance == 0:
            print('yes')
        else:
            print('no')

check_string_brackets('()')
check_string_brackets('(()())')
check_string_brackets('(()(()')
check_string_brackets(")(")
check_string_brackets("")