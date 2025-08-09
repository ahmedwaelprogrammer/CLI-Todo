import mods as mods
import FreeSimpleGUI as sg


color_one = "#1e2224"
color_two = "#F7DF38"
color_white = "#ffffff"

# Label
label = sg.Text("Add a new ToDo :")
label.BackgroundColor = color_one
label.TextColor = color_two

# Text input for new ##Todo
todo_input = sg.InputText(key="user_todo")

# The Add BTN
add_button = sg.Button("Add")
add_button.TextColor = color_one

list_box = sg.Listbox(key="list_box_todos" , values=mods.get_todos(), enable_events=True ,size=(40, 10))
edit_button = sg.Button("Edit")


sg.DEFAULT_BACKGROUND_COLOR = color_one
app_window = sg.Window("ToDo List" , [[label], [todo_input , add_button] ,[list_box , edit_button]] , font="Helvetica 12 bold")
while True:
    event = app_window.read()
    ev_name, ev_value = event
    print(ev_name, ev_value)
    match ev_name:
        case "Add":
            print(ev_value['user_todo'])
            todos = mods.get_todos()
            todos.append(ev_value['user_todo'] + '\n')
            mods.write_todos(todos)
            app_window["list_box_todos"].update(values=todos)
        case "Edit":
            print(ev_value)
            todos = mods.get_todos()
            index = todos.index(ev_value['list_box_todos'][0])
            todos[index] = ev_value['user_todo'] + '\n'
            mods.write_todos(todos)
            app_window["list_box_todos"].update(values=todos)
        case "list_box_todos":
            app_window["user_todo"].update(ev_value['list_box_todos'][0])

        case sg.WINDOW_CLOSED:
            break



app_window.close()

