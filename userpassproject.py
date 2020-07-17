# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:40:58 2020

@author: Brian
"""
#Basic practice to store passwords and keys
#Task: match username to password and open vault if True else
#lock out attempts at access
def remove_duplicates(usednames):
    '''
    

    Parameters
    ----------
    input: usednames, a List of usernames indicated by user input
    sets list into dictionary, removing duplicate usernames.

    Returns 
    -------
    List, from dictionary created from usernames after duplicates are removed

    '''
    return list(dict.fromkeys(usednames))
    

#set username and password and create key value pair in dictionary
userbank='blank'
def setlogins(user_name):
    '''
    

    Parameters
    ----------
    user_name : generic type
        user input for username and password 

    Returns
    -------
    stored : Dictionary
        returns a dictionary populated by user values

    '''
    stored={}
    usednames=[]
    passwords=[]
    completed=False
    while not completed:
        user_name=input(str('please enter a username: '))
        usednames+=[user_name]
        if usednames.count(user_name) > 1:
            print('name already in use, please try another name')
            usednames=remove_duplicates(usednames)
        else:
            password=input(str('please set a password: '))
            passwords+=[password]
        check = input(str('are you done? yes or no? ')).lower()
        if check == str('yes'):
            completed = True
            break
        while check != str('yes'): ###check if user is done, invalid if there is a typo####
            if check == str('no'):
                print('please input more values')
                break
            else:
                print('sorry invaid input please say yes or no ') 
                check = input(str('are you done? yes or no?')).lower()
                    
    stored={usednames[i]: passwords[i] for i in range(len(usednames))} 
    global userbank
    userbank=stored
    return stored

####################Intro and function execution###############################
x="welcome, let's store some names"
print(x)
setlogins(x)



#######################match function##########################################
def access():
    '''
    matches password with the one set by user

    Returns
    -------
    Welcome if passwords match, otherwise prints lockout if all tried are exhausted

    '''
    if match[login_user] == userbank[test]:
        print('Welcome to the program')
        global welcome
        welcome = True
    else:
        print('access denied, ',match.pop(login_user, passw), 'is not valid please try again')
        global tries
        tries-=1
        


print('Welcome, please login')
ref=userbank
tries=2
match={}
user=''
passw=''
login_user=input(str('Please enter a username: '))
user+=str(login_user)
welcome= False
while not welcome:
    if tries == 0:
        print('LOCKED OUT!')
        break
    else:
        attempt=input(str('please enter a password: '))
        passw=str(attempt)
        match[login_user]=passw
        test=login_user
        access()



        








    
