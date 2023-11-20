def list_passwords (username):
    mylist = ["acebook", "password"], ["makersbnb", "123456"], ["chitter", "qwerty"]
    for pair in mylist:
     
     if pair[0] == username:

        username = pair[1]
        return (pair[1])
print (list_passwords("chitter")) 
