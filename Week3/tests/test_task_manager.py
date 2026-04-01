from task_manager import TaskManager
import os

def test_add_task_adds_task_to_list():
    manager = TaskManager()
    manager.add_task("Learn pytest")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Learn pytest"


def test_complete_task_marks_task_as_completed():
    manager = TaskManager()
    manager.add_task("Learn pytest")

    manager.complete_task(0)

    assert manager.tasks[0].completed == True


def test_delete_task_removes_task_from_list():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")

    manager.delete_task(0)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Task 2"


def test_show_tasks_prints_no_tasks_when_empty(capsys):
    manager = TaskManager()

    manager.show_tasks()
    captured = capsys.readouterr()

    assert captured.out.strip() == "No tasks"


def test_show_tasks_prints_tasks_when_list_is_not_empty(capsys):
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")

    manager.show_tasks()
    captured = capsys.readouterr()

    assert "1 [ ] Task 1" in captured.out
    assert "2 [ ] Task 2" in captured.out

def test_save_to_file_creates_tasks_file():
    manager = TaskManager()
    manager.add_task("Task 1")

    manager.save_to_file()

    with open("tasks.txt", "r", encoding="utf-8") as file:
        content = file.read()

    assert "Task 1|False" in content

def test_load_from_file_loads_tasks_correctly():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.write("Task 1|False\n")
        file.write("Task 2|True\n")

    manager = TaskManager()
    manager.load_from_file()

    assert len(manager.tasks) == 2
    assert manager.tasks[0].title == "Task 1"
    assert manager.tasks[0].completed == False
    assert manager.tasks[1].title == "Task 2"
    assert manager.tasks[1].completed == True

def test_load_from_file_when_file_does_not_exist():
    if os.path.exists("tasks.txt"):
        os.remove("tasks.txt")

    manager = TaskManager()
    manager.load_from_file()

    assert manager.tasks == []

def test_show_tasks_prints_completed_task_correctly(capsys):
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.complete_task(0)

    manager.show_tasks()
    captured = capsys.readouterr()

    assert "1 [✓] Task 1" in captured.out