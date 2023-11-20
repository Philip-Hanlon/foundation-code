def what_card (forceoftackle, caughtplayer, gottheball):
    if caughtplayer == "false":
        return "no card"
    elif gottheball == "true" and forceoftackle >= 9:
        return "red card" 

    elif forceoftackle >= 8 and gottheball != "true":
        return "red card"
    elif forceoftackle >= 5:
        return "yellowcard"
    else : 
        return "no card"
print (what_card (8, "false", "true")) 