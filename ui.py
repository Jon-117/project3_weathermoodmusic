"""
User Interface:
Display anything to a user. Get input from a user.
"""
from classes import Menu
import subprocess
import platform


def clear_screen():
    # Check if the operating system is Windows
    if platform.system() == 'Windows':
        subprocess.run(['cls'], shell=True, check=True)
    else:
        subprocess.run(['clear'], shell=True, check=True)


def show_message(message: str) -> None:
    print(message)


def alert(message: str) -> None:
    show_message(f'WARNING: {message}')


def get_user_input(prompt: str) -> str:
    user_input = input(f'{prompt}')
    return user_input


def get_selection(menu_options):
    indexed_options = {idx + 1: option for idx, option in enumerate(menu_options)}
    for idx, option in indexed_options.items():
        print(f'[{idx}] {option}')

    while True:
        user_input = get_user_input('Choose an option: ')
        try:
            selection = int(user_input)
            if selection in indexed_options:
                show_message(indexed_options[selection])
                return indexed_options[selection]
            else:
                alert('Please select a valid option.')
        except ValueError:
            alert('Please enter a number.')


def confirm_choice() -> bool:
    while True:
        user_input = get_user_input('Are you sure? (Y/N): ').strip().upper()
        if user_input == 'Y':
            return True
        elif user_input == 'N':
            return False
        else:
            show_message('Please enter Y or N')


def show_menu(menu: Menu) -> None:
    while True:
        clear_screen()  # Clear the screen before showing the menu
        show_message(f"{menu.title}\n")
        show_message(f"{menu.message}\n")

        selection = get_selection(menu.options)

        if selection in menu.options:
            result = menu.options[selection]()
            if result == 'exit menu':
                break
        else:
            alert('Please select a valid option.')

