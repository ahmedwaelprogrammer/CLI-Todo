def get_todos():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
        return todos

todos = []
while True:
    user_action = input("Type 'add' , 'show' ,  'edit' , 'complete' 'exit':").strip()
    if 'add' in user_action[0:3]:
        try:
            todo = user_action[4:].strip() + '\n'

            todos = get_todos()
            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except:
            print("Something went wrong Please Follow the instructions for add command :add <YOUR NEW TODO>")
            continue
    elif 'show' in user_action[0:4]:
        todos = get_todos()

        for i , todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{i+1} -{todo}")
    elif 'edit' in user_action[0:4]:
        try:
            chose_todo = int(user_action[4:]) - 1
            new_todo = input("Type the new TODO:") + '\n'

            todos = get_todos()

            todos[chose_todo] = new_todo

            with open("todos.txt" , 'w') as file:
                file.writelines(todos)

        except:
            print("Something went wrong Please Follow the instructions for edit command :edit <TODO NUMBER IN THE LIST>")
            continue
    elif 'complete' in user_action[0:8]:
        try:
            chose_todo = int(user_action[9:]) - 1
            todos = get_todos()
            todos.pop(chose_todo)

            with open("todos.txt" , 'w') as file:
                file.writelines(todos)

        except:
            print("Something went wrong Please Follow the instructions for complete command :complete <TODO NUMBER IN THE LIST>")
            continue

    elif 'exit' in user_action[0:4]:
        break
    else:
        print("Invalid input")
print("Bye!")
