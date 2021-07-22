import operations
import configuration


while True:
    operation = {'1': operations.create_contact,
                 '2': operations.read_contact,
                 '3': operations.update_contact,
                 '4': operations.delete_contact,
                 '5': 'exit_phonebook', }
    actions = input("""
You need: 
Create contact (1), 
Read contact (2), 
Update contact (3), 
Delete contact (4)
Exit (5)
""")

    try:
        if operation[actions] == 'exit_phonebook':
            print('By')
            configuration.save_file()
            break
        operation[actions]()

    except KeyError:
        print('Incorrect input. Please repeat')
