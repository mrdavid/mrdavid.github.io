def paradox():
    try:
        print "enter try"
        raise Exception("Here")
        print "exit try"
    except:
        print "enter except"
        return "There"
        print "exit except"
    finally:
        print "enter finally"
        return "Or maybe there"
        print "exit finally"

    return "Or it that here?"
    
print paradox()