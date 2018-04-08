from userdetail import spy, Spy, ChatMessage #importing a file with specific variables
from datetime import datetime#importing date time
import csv
time=datetime.now() # current date and time
print time#Display to the user
from steganography.steganography import Steganography#importing Steganography module
login = input ('What do you want to do? Here are your options!!! \n 1. Login \n 2. Register')#Login options given to the user
if login==1:#Conditional statement

    username = raw_input ('Enter your user name')#Login option of username
    if len(username)>3 and username.isalpha():#Conditional statement
        print 'Welcome back ' + username#Messege given to the user
        userpassword = raw_input ('Enter you password')#Login option of password
        if userpassword>4:#Conditional statement
            print 'Password validated'#Messege given to the user

            print 'Hello Buddy' #greetings given to the user
            print 'Let\'s get started' #initialising
            STATUS_MESSAGE=['Sleeping', 'Eating', 'I can see you']#predefined status
            frnd1 = Spy('Mr.','Rohit',20,2)
            frnd2 = Spy('Mr.','Rahul',20,2)
            friends=[frnd1,frnd2]

            def load_frnd():
                with open('friend.csv', 'rb') as friends_data:
                    reader = list(csv.reader(friends_data))

                    for row in reader[1:]:
                        frnd = Spy(name=row[1],salutation=row[0],age=row[2],rating=row[3])
                        friends.append(frnd)

            load_frnd()


            def specific_chats():  # for particular friend
                specific_name = raw_input('Enter Freind\'s name')  # asking for the user input name
                specific_sal = raw_input('Mr. or Ms.')  # asking for the user input salutation
                specific_name = specific_sal.upper() + specific_name.upper()  # converting for uppercase
                with open('chat.csv') as chats_data:  # opening chats.csv file
                    reader = list(csv.reader(chats_data))  # making this as a list
                    print 'Secret Text ' + 'Date & Time in format  Date/Month/Hour ' + 'Sender Name ' + 'Receiver Name'  # Displaying the message for the user

                    for message, date, sent_by_me, receiver_name in reader[1:]:  # The csv module already extracts the information for you

                        if specific_name == receiver_name:# conditional statement
                            print message,date,sent_by_me,receiver_name


            def load_chats():  # for loading all the chats
                with open('chat.csv') as chats_data:  # opening chats.csv file
                    reader = list(csv.reader(chats_data))  # making this as a list
                    print 'Secret Text ' + 'Date/Month/Hour ' + 'Sender Name ' + 'Receiver Name'  # Displaying it to the user
                    for message, date, sent_by_me, receiver_name in reader[1:]:  # Extracting specific information
                        print message, date, sent_by_me, receiver_name  # printing it for the user


            def add_status(c_status):#function for statud
                if c_status != None:#checking condition if status is not none
                    print "Your current status is "+ c_status#Displaying for the user
                else:
                    print"You don't have any status currently.."#Displaying for the user
                existing_status = raw_input("You want to select from old status? Y/N")#Asking user to select desired options
                if existing_status.upper() == 'N':#Checking condition
                    new_status=raw_input('Enter your status : ')#Required user input for the status
                    if len(new_status) > 0:#validating
                        STATUS_MESSAGE.append(new_status)#add the status in the list
                elif existing_status.upper()=='Y':#checking condition
                    serial_no=1#initialising
                    for old_status in STATUS_MESSAGE:#traversing the list
                        print str(serial_no)+'. '+old_status#displaying for the user
                        serial_no=serial_no+1#incrementing
                    user_choice=input('Enter your choice :')#required input for the user
                    new_status=STATUS_MESSAGE[user_choice-1]#Index value decremented not start with zero
                updated_status=new_status#updating the status
                return updated_status#returning back

            def add_friend():
                frnd = Spy('','',0,0.0)
                frnd.name=raw_input('Enter your friend\'s name ? ')#required an input
                frnd.salutation=raw_input('What should we call your friend (Mr. or Ms.)')
                frnd.age=input('Enter your friend\'s age ? ')#required an input
                frnd.rating=input('Enter your friend\'s rating ? ')#required an input
                frnd.is_online = True
                if len(frnd.name)>2 and 12<frnd.age<50 and frnd.rating>spy.rating and frnd.name.isalpha():#checking for the condition
                    friends.append(frnd)
                    with open('friend.csv','a') as friends_data:
                        writer = csv.writer(friends_data)
                        writer.writerow([frnd.name,frnd.salutation,frnd.age,frnd.rating,frnd.is_online])
                        print'Its done, your friend added successfully'



                else:
                    print 'Friend cannot be added..'#displaying for the user
                return len(friends)#returning the value for the function

            def select_frnd():#display all friend
                serial_no=1#initialising
                for frnd in friends:#showing all friends using loop
                    print str(serial_no)+". "+frnd.name#displaying for the user
                    serial_no=serial_no+1#incrementing
                user_selected_frnd=input("Enter your choice")#input from the user
                user_selected_frnd_index=user_selected_frnd-1#decrementing because list does not start with zero
                return user_selected_frnd_index#returning value to the function


            def send_message():#sending a message
                select_friend=select_frnd()#index value
                original_image = raw_input('What is the name of original image ? ')  # asking the user for an input of image
                secret_text = raw_input('What is your secret text ? ')# secret text to be entered
                output_path = "output.jpg"#predefined name of an image
                secret_text=str(select_friend)+secret_text#assigning the index with the text fro a reading a message validation
                Steganography.encode(original_image, output_path, secret_text)  # encoding the message with image
                print 'Message successfully encoded.'#displaying for the user
                new_chat = ChatMessage(secret_text,False)
                friends[select_friend].chats.append(new_chat)  # appending the friend chat detail
                print'Your message is ready.'#displaying for the user
                with open('chat.csv', 'a') as friends_data:
                    writer = csv.writer(friends_data)
                    writer.writerow([secret_text,time.strftime('%d %m %H'),spy.name,friends[select_friend].name])

            def read_message():#reading a message
                select_friend=select_frnd()#index value
                output_path = raw_input('Which image you want to decode ? ')# asking the user for an input of image
                secret_text = Steganography.decode(output_path)#decoding message
                a=int(secret_text[:1])#checking if the right person is decoding the message or not
                if a==select_friend:
                    secret_text=secret_text.replace(str(a),'')
                    print 'Secret text is:' + secret_text#Displaying for the user
                    new_chat = {  # dictionary
                        'message': secret_text,
                        'time': datetime.now(),
                        'sent_by_me': False
                    }
                    friends[select_friend].chats.append(new_chat)  # appending the friend chat detail
                    print'Your secret message has been saved...'#Displaying for the user
                else:

                    print "You can\'t able to see other\'s message"#displaying it for the user



            def start_chat(spy_name,spy_age,spy_rating):#user define function created
                print 'Here are your options ' +spy_name#Message given to the user
                current_status = None
                show_menu = True#by default value true for validation
                while show_menu:#using loop for multiple times show the same thing
                    choice = input('What do you want to do ?\n1.Add a status\n2.Add a friend\n3.Send a message\n4.Read a message\n5.Read chats from user\n0.Exit ')#choices given to the userinput from the user
                    if choice ==1:#conditional Statement
                        current_status = add_status(current_status)#calling add  status function
                        print'Updated status is ' + current_status#displaying for the user
                    elif choice==2:#conditional Statement
                        no_of_friend = add_friend()#calling the add friend function
                        print 'You have ' + str(no_of_friend) + ' friends.'#displaying for the user
                    elif choice == 3:
                        send_message()#calling send function for encoding
                    elif choice == 4:
                        read_message()#calling read function for decoding
                    elif choice == 5:
                        chats = raw_input('Load chats (press 1 for all friends, press 2 for a specific friend)')
                        if chats == '1':
                            load_chats()
                        elif chats == '2':
                            specific_chats()
                        else:
                            print 'Invalid option'#Messege given to the user
                    elif choice == 0:  # conditional Statement
                        show_menu = False  # Terminating the program
                    else:  # conditional Statement
                        print 'Invalid option selected by you.!! '  # Message givenfor the user


            spy_exist=raw_input('Are you an existing spy Y/N ')#asking the user whether he/she is an spy or not
            if spy_exist.upper()=='Y':#conditional Statement
                print 'Welcome back ' + spy.name + ' Age = ' + str(spy.age) + '.' + ' ' + 'Having a rating of = ' + str(spy.rating) #Displaying the previous data for the user
                start_chat(spy.name,spy.age,spy.rating)#Calling  a  chat function
            elif spy_exist.upper()=='N':#conditional Statement
                spy = Spy('','',0,0.0)
                spy.name = raw_input('Enter Your Name ')#Message for the user and input from the user

                spy_rating=0.0#Initalising the variable
                spy_age=0#Initalising the variable
                if spy.name.isalpha():#Checking for name entered by the user as input
                    spy_salutation = raw_input('What should we call you(Mr. or Ms.)')  # Message for the user and input from the user
                    if len(spy.name)>=2 :#Checking the length of the name which should be greater than two
                        if spy_salutation.upper()=='MR.' or spy_salutation.upper()=='MS.':#conditional Statement
                            spy_name = spy_salutation.upper() + '' + spy.name.upper()#Concatinationg  2 string
                            print 'Welcome '+spy_name +' Glad to have you back with us'##Concatinationg  2 string
                            print 'Alright '+spy_name+'. '+'I\'d like to know a little bit more about you ...'#Concatinationg  2 string
                            spy_age=input('what is your age ')#input taken from the user
                            if 50>spy_age>12:#conditional statement
                                print 'You are eligible for being spy '+str(spy_age)#concationating th integer with the string
                                spy_rating=input('Please enter your rating ')#input from the user
                                if spy_rating>5.0:#Conditional statement
                                    print'Great'#Message given to the user
                                elif 3.5<spy_rating<=5.0:#Conditional statement
                                    print 'Good'#Message given to the user
                                elif 2.5<spy_rating<=3.5:#Conditional statement
                                    print 'Average'#Message given to the user
                                else:#Conditional statement
                                    print 'Shame on you!!!'#Message given to the user
                                spy_is_online = True#Initialising the variable
                                print 'Authentication Complete.Welcome ' +spy_name+ ' age: ' +str(spy_age)+' and rating is '+str(spy_rating) # Concatinating two integer with a string
                                start_chat(spy_name, spy_age, spy_rating)#calling a  chat function

                            else:#Conditional statement
                                print 'You should grow up till now!! Common man'#Message to the user
                        else:#Conditional statementn
                            print 'Wrong Salutation'#Message given to the user
                    else:#Conditional statement
                        print 'Enter a valid name'#Message given to the user
                else:#conditional Statement
                    print 'invalid name'#Messege given to the user
            else:#Conditional statement
                print 'Invalid Option'#Message given to the user
        else:
            print 'Incorrect Password'#Messege given to the user
    else:
        print 'User name doesn\'t exist'#Messege given to the user
else:
    print 'This feature is not implemented yet'#Messege given to the user