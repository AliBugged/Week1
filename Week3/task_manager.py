from task import Task


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks")
            return
        
        for i, task in enumerate(self.tasks, start=1):
            print(i, task)

    def complete_task(self, index):
        self.tasks[index].mark_completed()

    def delete_task(self, index):
        del self.tasks[index]
    
    def save_to_file(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(f"{task.title}|{task.completed}\n")
                
    def load_from_file(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                for line in file:
                    title, completed = line.strip().split("|")
                    task = Task(title)
                    task.completed = completed == "True"
                    self.tasks.append(task)
        except FileNotFoundError:
            pass