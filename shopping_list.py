# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your current list.
    """)

while True:
    # ask for new items
    new_item = input("> ")
      
    # be able to quit the app
    if new_item == 'DONE':
        break
        
    # add new items to our list
    shopping_list.append(new_item)

# print out the list
for item in shopping_list:
    print(item)