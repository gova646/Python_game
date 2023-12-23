import getpass




def get_digits_count():
    '''The method returns the number of digits choosen by
        the user.
    '''
    while True:
        try:
            digits_count = int(input('Please enter the input'))
        except ValueError:
            print('input should be integer!')
            continue
        break   
    return digits_count

def get_masked_user_number(digits_count,display_content):
    """This method is used to get the number that user chooses"""
    while True:
        try:
            user_number = int(getpass.getpass(display_content))
        except ValueError:
            print('input should be integer!')
            continue
        break   
    user_number = str(user_number)
    while not len(user_number) == digits_count:
        print('PLease choose the number of size'+str(digits_count))
        user_number = get_masked_user_number(digits_count,display_content)
    return user_number

def get_user_number(digits_count,display_content):
    """This method is used to get the number that user wants to check"""
    while True:
        try:
            user_number = int(input(display_content))
        except ValueError:
            print('input should be integer!')
            continue
        break   
    user_number = str(user_number)
    while not len(user_number) == digits_count:
        print('PLease choose the number of size'+str(digits_count))
        user_number = get_user_number(digits_count,display_content)
    return user_number

def get_user_name(display_content):
    user_name = input(display_content)
    return user_name
