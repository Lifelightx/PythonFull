def display(fun):
    return "Hai " + fun

def message():
    return "How are you?"

print(display(message()))


def dis():
    def msg():
        return "how are you?"
    return msg

msg = dis()
print(msg())

