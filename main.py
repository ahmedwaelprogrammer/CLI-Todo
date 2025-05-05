
while True:
    user_action = input("Type 'add' , 'show' ,  'edit' , 'complete' 'exit':").strip()
    match user_action:
        case 'add':
            todo = input("Enter a TODO:")+ "\n"
            file = open("todos.txt" , "r")
            todos = file.readlines()
            file.close()
            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            #new_todos = [todo.strip('\n') for todo in todos]

            for i , todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{i+1} -{todo}")
        case 'edit':
            chose_todo = int(input("The number of the TODO you want to edit:")) - 1
            new_todo = input("Type the new TODO:")
            todos[chose_todo] = new_todo
        case 'complete':
            chose_todo = int(input("The number of the TODO you want to complete:")) - 1
            todos.pop(chose_todo)
        case 'exit':
            break
        case _:
            print("Invalid input")
print("Bye!")
