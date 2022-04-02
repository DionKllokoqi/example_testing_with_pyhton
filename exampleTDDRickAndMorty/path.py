import os


def current_path():
    value = os.getcwd()
    print(value)
    return value


def read_file():
    with open('test.txt') as file:
        contents = file.read()

    return contents
