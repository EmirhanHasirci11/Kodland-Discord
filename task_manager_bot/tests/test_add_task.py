import unittest
from database import add_task, get_tasks

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        print("Testing add_task() function.")
        description = "Test görevi"
        print(f"Adding task: '{description}'")
        task_id = add_task(description)
        tasks = get_tasks()
        print("Fetching tasks from database.")

        task_descriptions = [task[1] for task in tasks]
        if description in task_descriptions:
            print("✅ Test passed: Task was added successfully.")
        else:
            print("❌ Test failed: Task not found.")
        self.assertIn(description, task_descriptions)

if __name__ == '__main__':
    unittest.main()
