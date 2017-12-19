def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "ZeroDivisionError, To infinity and beyond!"
    except:
        return "Something werid!"

print(divide(4,5))
print(divide(2,0))
print(divide('a',0))
