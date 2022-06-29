duck_names = ["Quacks", "Waddles", "Steve"]

def hello_ducks(ducks):
    names = []
    print("Hello Ducks")
    for i in ducks:
        names.append(i)
    return names

def hello_humans():
    return "hello humans"

def hello_class():
    return "hello class"

if __name__ == "__main__":
    print(hello_ducks())
    print(hello_humans())
