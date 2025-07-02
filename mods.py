def get_todos(file_path = "todos.txt"):
    """
    :param file_path: enter the file path directory to read the todos from
    :return: it returns a list of todos
    """
    with open(file_path, "r") as file:
        todos = file.readlines()
        return todos

def write_todos(todos, file_path = "todos.txt"):
    """
    :param todos: the list of todos you want to write on the file
    :param file_path: the file path directory to write to
    """
    with open("todos.txt", "w") as file:
        file.writelines(todos)