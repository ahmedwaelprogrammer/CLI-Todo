todos = []
while True:
    user_action = input("Type 'add' , 'show' ,  'edit' , 'complete' 'exit':").strip()
    match user_action:
        case 'add':
            todo = input("Enter a TODO:")+ "\n"
            with open("todos.txt" , "r") as file:
                todos = file.readlines()
                todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'show':
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for i , todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{i+1} -{todo}")
        case 'edit':
            chose_todo = int(input("The number of the TODO you want to edit:")) - 1
            new_todo = input("Type the new TODO:") + '\n'
            with open("todos.txt", "r") as file:
                todos = file.readlines()
                todos[chose_todo] = new_todo

            with open("todos.txt" , 'w') as file:
                file.writelines(todos)
        case 'complete':
            chose_todo = int(input("The number of the TODO you want to complete:")) - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
                todos.pop(chose_todo)

            with open("todos.txt" , 'w') as file:
                file.writelines(todos)

        case 'exit':
            break
        case _:
            print("Invalid input")
print("Bye!")
