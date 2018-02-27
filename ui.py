# ui.py

def hit_menu():

    # Display choices for user, return users selection
    print('''
        h. hit
        s. stay
    ''')

    choice = input("Enter your selection: ")
    return choice

def get_name():
    name = input("What is your name?\n")
    return name

def message(msg):
  print(msg)
