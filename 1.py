print(111)

def fun():
    def inner():
        print('hello')
    return inner

print(111)
