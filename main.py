
from userdetail import username,userage,userrating #Importing a file with specific variables
print 'Hello Buddy!!!' # Greeting note given to the user
print 'Let\'s get started' #Initialising

def startchat (username,userage,userrarting): #user define functions created
    print 'Here are your options ' + username #Messege given to the user
    showmenu = True #By default value true for validation
    while showmenu : #Using loop for multiple times perform the same process
        option = input ('Now What do you want to do? \n 1. Add your status \n 2. Add your friend \n 3. EXIT ') #Choices given to the user
        if option == 1: #Conditional statement
            print 'Add a status'
        elif option == 2: #Conditional statement
            print 'Add friend'
        elif option == 3: #Conditional statement
         showmenu = False # Terminating the process
        else :
            print 'Invalid option selected by you..!! ' #Messege for the user

userexist = raw_input('Are you a new user? Y/N ') #Asking the user whether she/he is a new user or not
if userexist.upper() == 'N': # Conditional statement
    print 'Welcome Back %s. Age %d. Having rating of %d.' %(username,userage,userrating) #Displaying the privious data for the user
    startchat (username,userage,userrating) #Calling the existing function
elif userexist.upper() == 'Y': #Conditional statement

    username = raw_input ('What is your name? ') #Messege for the user to input her/his name
    if username.isalpha(): #Checking the name entered by the user as input
        if len(username) > 2: #Cheching the length of the name entered by the user
            print 'Welcome ' + username + '. Glad to have you back with us. ' #Concatinating two string
            usersalutation = raw_input('What should we call you(Mr. or Ms.)? ') #Messege for the user
            if usersalutation.upper() == 'MR.' or usersalutation.upper() == 'MS.': #Conditional statement
                username = usersalutation.upper() + ' ' + username #Concatinating two string
                print 'Alright ' + username + ', I\'d like to know a little bit more about you.' #Concatinating two string
                userage = input('Enter your age!! ') #Taking input from the user
                if 50>userage>12: #Conditional statement
                    print 'You are eligible. '
                    userrating = input('What is your rating? ') #Input from the user
                    if 8.0 <= userrating < 10.0: #Conditional statement
                        print 'Great. ' #Messege given to the user
                    elif 6.0 <= userrating < 8.0: #Conditional statement
                        print 'Good. ' #Messege given to the user
                    elif 4.0 <= userrating < 6.0: #Conditional statement
                        print 'Average. ' #Messege given to the user
                    elif 0.0 < userrating < 4.0: #Conditional satement
                        print 'Shame on you!!! ' #Messege given to the user
                    user_is_online = True #Initializing the variable
                    print 'Authentication complete. Welcome ' + username + '.' + ' ' + 'Age = ' + str(
                            userage) + '.' + ' ' + 'rating = ' + str(userrating) + '.' + ' ' + 'Proud to have you onboard. ' #Concatinating two integer with a string
                    startchat (username,userage,userrating) #Calling a chat function


                else: #Conditional statement
                    print 'You are not eligible ' #Messege given to the user
            else: #Conditional statement
                print 'Invalid Salutation' #Messege given to the user
        else: #Conditional statement
            print 'Please enter valid username' #Messege given to the user

    else: #Conditional statement
        print 'Invalid input' #Messege given to the user
else:
    print 'Invalid input'