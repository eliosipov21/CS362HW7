def leapyear(i):
    if(i%4 == 0):
        if(i%100 == 0):
            if(i%400 == 0):
                return True
            return False 
        return True
    return

