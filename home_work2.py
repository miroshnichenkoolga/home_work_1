from datetime import time

def test_dark_theme_by_time():
    current_time = time(hour=23)
    is_dark_theme =22 <= current_time.hour or current_time.hour<6
    assert is_dark_theme is True

def test_dark_theme_by_time_and_user_choice():

    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        is_dark_theme = 22 <= current_time.hour or current_time.hour < 6

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users=None
    for user in users:
        if user['name']=='Olga':
            suitable_users=user
            break

    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []
    for user in users:
        if user['age']< 20:
            suitable_users.append(user)
            print(suitable_users)


    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]



def print_readable_function_info(func, *args):
    function_name = func.__name__.replace('_', ' ').title()
    arguments = ', '.join([str(arg) for arg in args])
    print(f"{function_name} [{arguments}]")

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    # Печатаем имя функции и аргументы
    print_readable_function_info(open_browser, browser_name)
    actual_result = f"Open Browser [{browser_name}]"
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    # Печатаем имя функции и аргументы
    print_readable_function_info(go_to_companyname_homepage, page_url)
    actual_result = f"Go To Companyname Homepage [{page_url}]"
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    # Печатаем имя функции и аргументы
    print_readable_function_info(find_registration_button_on_login_page, page_url, button_text)
    actual_result = f"Find Registration Button On Login Page [{page_url}, {button_text}]"
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
