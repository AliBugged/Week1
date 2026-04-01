from task import Task


def test_task_initialization():
    task = Task("Test Task")

    assert task.title == "Test Task"
    assert task.completed == False


def test_mark_completed_sets_completed_to_true():
    task = Task("Test Task")
    assert task.completed == False

    task.mark_completed()

    assert task.completed == True


def test_task_string_changes_after_completion():
    task = Task("Test Task")
    assert str(task) == "[ ] Test Task"

    task.mark_completed()

    assert str(task) == "[✓] Test Task"