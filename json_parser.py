"""
This module parses a .json file from the Twitter API.
"""

from json import load

def load_json(path: str) -> dict:
    """
    Return the .json file in a form of a dict.
    """
    json_file = open(path, mode='r', encoding='utf-8')
    json_dict = load(json_file)
    json_file.close()

    return json_dict


def get_json_path() -> str:
    """
    Get the path to the .json file using a standard input.
    """
    path = input('\nEnter the path to the .json file\n\n>> ')

    return path


def parse_list(key: list, path: str) -> tuple:
    """
    -> (new_key, new_path)
    Parse the list and return new key and path.
    """
    if len(key) == 0:
        print('\nThis list is empty. This is the end of the file')
        return (None, None)

    print('\nThis is a list. Do you want to display the entire list?\n')
    while True:
        choice = input(path)
        if choice == 'yes':
            for child in key:
                print(child, end ='    ')
            print('\n')
            break
        if choice == 'no':
            break
        print('\nEnter "yes" or "no"\n')

    print('\nThis is a list. Enter an index in range from 0 to {}\n'.format(len(key) - 1))
    while True:
        index = int(input(path))
        if index in range(len(key)):
            path = path[:-1] + str(index) + '>> '
            key = key[index]
            break
        print('\nEnter a valid index\n')

    return (key, path)


def parse_dict(key: dict, path: str) -> tuple:
    """
    -> (new_key, new_path)
    Parse the dict and return new key and path.
    """
    if len(key) == 0:
        print('\nThis dict is empty. This is the end of the file')
        return (None, None)

    print('\nThis is a dict. Enter a key from the next list:\n')
    for child in key:
        print(child, end='    ')
    print('\n')

    while True:
        new_key = input(path)
        if new_key in key:
            if path == '>> ':
                path = new_key + '>> '
            else:
                path = path[:-1] + new_key + '>> '
            key = key[new_key]
            break
        print('\nEnter a valid key\n')

    return (key, path)


def parse_int(key: int, path: str):
    """
    Parse the integer, return nothing.
    """
    print('\nThis is an integer. Do you want to display this integer?\n')
    while True:
        choice = input(path)
        if choice == 'yes':
            print(key)
            break
        if choice == 'no':
            break
        print('\nEnter "yes" or "no"\n')

    print('\nThis is the end of the file')


def parse_str(key: str, path: str):
    """
    Parse the string, return nothing.
    """
    print('\nThis is a string. Do you want to display this string?\n')
    while True:
        choice = input(path)
        if choice == 'yes':
            print(key)
            break
        if choice == 'no':
            break
        print('\nEnter "yes" or "no"\n')


def parse_bool(key: bool, path: str):
    """
    Parse the boolean, return nothing.
    """
    print('\nThis is a boolean. Do you want to display this boolean?\n')
    while True:
        choice = input(path)
        if choice == 'yes':
            print(key)
            break
        if choice == 'no':
            break
        print('\nEnter "yes" or "no"\n')


def parse_json(json_dict: dict):
    """
    The main function. Parse the .json file and return nothing.
    """
    key = json_dict
    path = '>> '
    while True:
        if isinstance(key, list):
            key, path = parse_list(key, path)
        elif isinstance(key, dict):
            key, path = parse_dict(key, path)
        elif isinstance(key, int):
            parse_int(key, path)
            break
        elif isinstance(key, str):
            parse_str(key, path)
            break
        elif isinstance(key, bool):
            parse_bool(key, path)
            break
        else:
            print('\nThis is the end of the file')
            break


if __name__ == '__main__':
    parse_json(load_json(get_json_path()))
