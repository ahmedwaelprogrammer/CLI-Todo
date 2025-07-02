import mods

todos = []
while True:
    user_action = input("Type 'add' , 'show' ,  'edit' , 'complete' 'exit':").strip()
    if user_action.startswith("add"):
        try:
            todo = user_action[4:].strip() + '\n'

            todos = mods.get_todos()
            todos.append(todo)

            mods.write_todos(todos)

        except:
            print("Something went wrong Please Follow the instructions for add command :add <YOUR NEW TODO>")
            continue
    elif user_action.startswith("show"):
        todos = mods.get_todos()

        for i , todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{i+1} -{todo}")
    elif user_action.startswith("edit"):
        try:
            chose_todo = int(user_action[4:]) - 1
            new_todo = input("Type the new TODO:") + '\n'

            todos = mods.get_todos()
            old_todo = todos[chose_todo]
            todos[chose_todo] = new_todo
            print(f"todo {chose_todo + 1} - {old_todo} -- has been updated to -- {new_todo}")

            mods.write_todos(todos)

        except:
            print("Something went wrong Please Follow the instructions for edit command :edit <TODO NUMBER IN THE LIST>")
            continue
    elif user_action.startswith("complete"):
        try:
            chose_todo = int(user_action[9:]) - 1
            todos = mods.get_todos()
            old_todo = todos[chose_todo]
            todos.pop(chose_todo)
            print(f"{chose_todo+1} - {old_todo} -- has been removed ")
            mods.write_todos(todos)

        except:
            print("Something went wrong Please Follow the instructions for complete command :complete <TODO NUMBER IN THE LIST>")
            continue

    elif 'exit' in user_action[0:4]:
        break
    else:
        print("Invalid input")
print("Bye!")
