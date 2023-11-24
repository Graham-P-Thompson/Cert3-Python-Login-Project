# Graham Thompson 26/09/2022 Simple login program to be used for a game in unreal engine.
import random
import string


def menu_return(current_func):
    # Function to navigate back to the main menu, so I only had to write the code once rather than 3 times
    menu_option = input('Navigate back to the main menu? Y/N: ')
    menu_option = menu_option.strip()
    menu_option = menu_option[0].lower()
    if menu_option == 'y':
        main()
    elif menu_option == 'n':
        current_func()
        #Creating an argument that allows me to pass and call another function as the parameter of this function
    else:
        print('Please enter Y/N')


def login():
    # function for the login section of the program
    try:
        file = open('accounts.txt', 'r')
    except FileNotFoundError:
        print('File does not exist')
    else:
        line = file.readlines()
        #creates a list of the lines from the variable file and assigns the list to variable line
        file.close()
        user = input('Please enter your username: ')
        password = input('Please enter your password: ')
        user_okay = False
        for i in line:
            #iterates over each element of the list in variable line
            #added an IF statement check to resolve out of range error if accounts.txt file data is corrupt
            #the IF statement checks the length of the array has the correct number of elements
            if len(i.split()) >= 2:
                u = i.split()[0]
                #splits each element at white space and assigns u with first string in element
                p = i.split()[1]
                #splits each element at white space and assigns p with second string in element
                if user == u and password == p:
                    user_okay = True
                    #Used a variable here to allow conditional statements to run outside of loop
            else:
                print('\naccounts.txt file corrupt, please rectify and try again.')
                return exit_app()
        if user_okay:
            print('LOGIN SUCCESSFUL WELCOME!!!\n')
            menu_return(login)
            #This function gives the option to navigate back to menu or stay in current location
        else:
            print('Username or password invalid, please try again')
            login()


def register_user():
    #Function to register a new user
    new_user = input('Please enter a new username: ')
    option = input('Would you like to have a password generated for you? Y/N ')
    option = option.strip()
    option = option[0].lower()
#start of character type options for user to choose from
    if option == 'y':
        print('\nWhich character type would you like the password to be made from? ')
        while True:
            try:
                char_type = int(input('Enter 1 for numbers, Enter 2 for symbols, 3 for letters or 4 for mix: '))
                break
            except ValueError:
                print('Please enter the number 1, 2, 3 or 4')
        character = ''
        #I am using the python string library here to create the passwords
        if char_type == 1:
            character = string.digits
        elif char_type == 2:
            character = string.punctuation
        elif char_type == 3:
            character = string.ascii_letters
        elif char_type == 4:
            character = string.ascii_letters + string.digits + string.punctuation
        else:
            print('Please enter the number 1, 2, 3 or 4')
#start of password length option
        choice = input('Would you like to choose the password length? Y/N ')
        choice = choice.strip()
        choice = choice[0].lower()
        if choice == 'y':
            while True:
                try:
                    choice_len = int(input('Please enter the number of characters you would like to use: '))
                    break
                except ValueError:
                    print('That is not a number, please try again.')
        else:
            choice_len = 10
#start of code to generate password
        try:
            store = open('accounts.txt', 'a')
        except FileNotFoundError:
            print('Unable to store generated password, file not found')
        else:
            rand_password = ''
            for i in range(1, choice_len + 1):
                rand_password += random.choice(character)
                #Using the random python library and the choice function with the variable character as the argument
            store.write(new_user + ' ' + rand_password + '\n')
            store.close()
            print('\nYour username is ' + new_user)
            print('Your password is ' + rand_password + '\n')
            menu_return(register_user)
#start of users own choice password option
    elif option == 'n':
        password_choice = input('Please enter a password: ')
        try:
            store = open('accounts.txt', 'a')
        except FileNotFoundError:
            print('Unable to store password, file not found')
        else:
            store.write(new_user + ' ' + password_choice + '\n')
            store.close()
            print('\nYour username is ' + new_user)
            print('Your password is ' + password_choice + '\n')
            menu_return(register_user)
            # This function gives the option to navigate back to menu or stay in current location
#Way to catch incorrect input and retry
    else:
        print('Please re-enter a username and then confirm password generation by entering Y/N')
        register_user()


def view_accounts():
    #funtion to view accounts
    try:
        accounts = open('accounts.txt', 'r')
    except FileNotFoundError:
        print('File does not exist')
    else:
        view = accounts.read()
        accounts.close()
        print('\n' + view + '\n')
        menu_return(view_accounts)
        # This function gives the option to navigate back to menu or stay in current location


def exit_app():
    #function to exit application
    from time import sleep
    exit_msg = 'GOODBYE!'
    for i in exit_msg:
        print(i, end='')
        sleep(0.25)
        #calling sleep function with argument specifying time to sleep between iterations
        #0.25 milliseconds, 0.25*8characters= 2000 milliseconds(2 seconds)


def main():
    #main menu function for the application
    print('\n\nMenu options:')
    print(' ' + '~' * 34 + ' ')
    print('|                                  |')
    print('|  1. Login                        |')
    print('|  2. Register                     |')
    print('|  3. View accounts                |')
    print('|  4. Exit                         |')
    print('|                                  |')
    print(' ' + '~' * 34 + ' ')

    user_sel = input('Please select an option 1/2/3/4: ')
    print('\n')

    if user_sel == '1':
        while True:
            confirm1 = input('You have chosen to login as an existing user, continue? Y/N: ')
            confirm1 = confirm1.strip()
            confirm1 = confirm1[0].lower()
            if confirm1 == 'y':
                login()
                break
            elif confirm1 == 'n':
                main()
                break
            else:
                print('Please enter Y/N')
                continue

    elif user_sel == '2':
        while True:
            confirm2 = input('You have chosen to register a new account, continue? Y/N: ')
            confirm2 = confirm2.strip()
            confirm2 = confirm2[0].lower()
            if confirm2 == 'y':
                register_user()
                break
            elif confirm2 == 'n':
                main()
                break
            else:
                print('Please enter Y/N')
                continue

    elif user_sel == '3':
        while True:
            confirm3 = input('You have chosen to view accounts, continue Y/N: ')
            confirm3 = confirm3.strip()
            confirm3 = confirm3[0].lower()
            if confirm3 == 'y':
                view_accounts()
                break
            elif confirm3 == 'n':
                main()
                break
            else:
                print('Please enter Y/N')
                continue

    elif user_sel == '4':
        exit_app()

    else:
        print('Incorrect input, please try again!')
        main()


main()
