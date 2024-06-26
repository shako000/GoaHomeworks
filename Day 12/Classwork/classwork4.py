correct_password = 'shako'
user_input = ''

while correct_password != user_input:
    user_input = input ("Please enter your password: ")


    if user_input == correct_password:
        print ("You succsesfully signed in")
    else:
        print ("Password is incorrect")