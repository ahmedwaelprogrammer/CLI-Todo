todos = []
while True:
    user_action = input("Type 'add' , 'show' ,  'edit' , 'complete' 'exit':").strip()
    if 'add' in user_action[0:3]:
        todo = user_action[4:].strip() + '\n'
        with open("todos.txt" , "r") as file:
            todos = file.readlines()
            todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action[0:4]:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for i , todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{i+1} -{todo}")
    elif 'edit' in user_action[0:4]:
        chose_todo = int(user_action[4:]) - 1
        new_todo = input("Type the new TODO:") + '\n'
        with open("todos.txt", "r") as file:
            todos = file.readlines()
            todos[chose_todo] = new_todo

        with open("todos.txt" , 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action[0:8]:
        chose_todo = int(user_action[9:]) - 1
        with open("todos.txt", "r") as file:
            todos = file.readlines()
            todos.pop(chose_todo)

        with open("todos.txt" , 'w') as file:
            file.writelines(todos)

    elif 'exit' in user_action[0:4]:
        break
    else:
        print("Invalid input")
print("Bye!")
