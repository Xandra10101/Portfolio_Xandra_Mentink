cijferlijst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
oldpassword = '12345'
newpassowrd = 'qwert1'
def new_password(oldpassword, newpassword):
    cin = False
    for nummer in cijferlijst:
        if nummer in newpassword:
            cin = True
    if newpassword != oldpassword and len(newpassword) >= 6 and cin:
        return True
    else:
        return False
print(new_password('12345', 'hellow3'))
print(new_password('12345', 'Goodbye2'))
print(new_password('12345', '12345'))
