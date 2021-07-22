import configuration


def save_file():
    with open(configuration.file, f'w{configuration.access}') as f:
        configuration.dumpfile(directory, f)


def open_file():
    try:
        with open(configuration.file, f'r{configuration.access}') as f:
            data = configuration.loadfile(f)
    except (FileNotFoundError, EOFError):
        print('File Error. Create New ')
        data = {}
    return data


def check(func):
    def wrapper():
        name = func()
        return name in configuration.directory.keys(), name
    return wrapper


@check
def enter_name():
    return input('Enter name: ')


def create_contact():
    presence, name = enter_name()
    if not presence:
        configuration.directory[name] = input('Enter phone number: ')
        print(f'Contact created {name} number {configuration.directory[name]}')
    else:
        print('Contact exist. Please use Update contact')
    return


def read_contact():
    presence, name = enter_name()
    if presence:
        print(f'Contact: {name} phone: {configuration.directory[name]}')
    else:
        print('Contact not exist.')
    return


def update_contact():
    presence, name = enter_name()
    if presence:
        print(f'Contact: {name} phone: {configuration.directory[name]}')
        configuration.directory[name] = input('Enter new phone number: ')
        print(f'Contact update: {name} number: {configuration.directory[name]}')
    else:
        print('Contact not exist.')
    return


def delete_contact():
    presence, name = enter_name()
    if presence:
        print(f'Contact: {name} phone: {configuration.directory[name]}')
        del configuration.directory[name]
        print(f'Contact delete')
    else:
        print('Contact not exist.')
    return


directory = open_file()
