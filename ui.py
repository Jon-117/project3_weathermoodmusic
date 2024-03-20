"""
User Interface:
Display anything to a user. Get input from a user.
"""

import logging

log = logging.getLogger(__name__)


def show_message(message: str) -> None:
    print(message)


def alert(message: str) -> None:
    show_message(f'WARNING: {message}')


def get_user_input(prompt: str, is_integer=False, is_float=False):
    """
    Used to get user input when not a menu interaction.
    :param prompt:      The message to display to the user when requesting input.
    :param is_integer:  Default: False. If True, used to ensure the response is an integer.
    :param is_float:    Default: False. If True, used to ensure the response is a float.
    """
    log.info('Getting input from user...')
    user_input = ""
    if is_integer and is_float:
        log.critical("Programmer tried asserting that input is an integer AND a float."
                     "\nFix the get_user_input call used.")
        raise Exception('is_integer and is_float and exclusive options. Only one or zero may be True. ')
    if is_integer:
        while user_input == "":
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError as e:
                log.error(f'Not an integer: {e}')
                alert("Not an integer, please try again.")
                user_input = ""
                continue

    if is_float:
        while user_input == "":
            try:
                user_input = float(input(prompt))
                return user_input
            except ValueError as e:
                log.error(f'Not a float: {e}')
                alert("Not an float, please try again.")
                user_input = ""
                continue

    if not is_integer and not is_float:
        try:
            user_input = input(prompt)
            return user_input
        except Exception as e:
            log.error(f'Error getting user input: {e}')
            alert("Error getting user input, please try again.")


def get_selection(menu_options: list or dict):
    """
    Get a user's selection from supplied list or dictionary
    """
    log.info('Creating selection options... ')
    indexed_options = {idx + 1: option for idx, option in enumerate(menu_options)}
    for idx, option in indexed_options.items():
        log.info(f'Presenting Option: {idx}: {option} ')
        show_message(f'[{idx}] {option}')

    while True:
        log.info('Getting user input for selection... ')
        user_input = get_user_input('Choose an option:  ', is_integer=True)
        log.info(f'User input for selection: {str(user_input)}')
        try:
            log.debug('Validating user input for selection... ')
            if user_input in indexed_options:
                log.debug(f'Selection validated. \nSelected "{user_input}: {indexed_options[user_input]}"')
                show_message(f'\nYou selected: {indexed_options[user_input]}')
                log.debug(f'Returning {indexed_options[user_input]}')
                return indexed_options[user_input]
            else:
                log.debug(f'Input "{user_input}" is not valid. ')
                alert('Please select a valid option.')
        except ValueError:
            alert('Please enter a valid number.')


