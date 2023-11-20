def my_name_finder (myname):
    mylist = ["jon", "phil", "coxy", "malc", "tom", "danny"]
    myreturnvalue = "notfound"
    for myname2 in mylist:
       if myname == myname2:
            myreturnvalue = "foundphil"

    return (myreturnvalue)
            



print (my_name_finder ("phil"))      

