
def read():
    with open(r'C:\Users\TANU\PycharmProjects\to-do-app\tanu.txt', 'r')  as file:
        read = file.readlines()
        return read


def write(arg):
    with open(r'C:\Users\TANU\PycharmProjects\to-do-app\tanu.txt', 'w') as file:
        file.writelines(arg)


