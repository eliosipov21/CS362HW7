def fbuzz(i):
    if(i%15 == 0):
        return "Fizzbuzz"
    if(i%3 == 0):
        return "Fizz"
    if(i%5 == 0):
        return "Buzz"
    else:
        return i
    return