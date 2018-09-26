oldpassword = 'tijmen'
newpassword = 'muller'


def new_password(oldpassword, newpassword):
    'checks if password is not old password and longer than 6 characters'
    if oldpassword != newpassword and len(newpassword) == 6:
        return(True)
    else:
        return(False)

print(new_password(oldpassword, newpassword))