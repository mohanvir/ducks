def hello_ducks():
    return "hello_ducks"

def hello_humans():
    human_count = human_count +1
    return "hello humans"

def hello_class():
    class_count = class_count + 1
    return "hello class"

if __name__ == "__main__":
    print(hello_ducks())
    print(hello_humans())
