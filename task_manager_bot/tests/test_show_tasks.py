import unittest
from database import add_task, complete_task, get_completed_tasks, get_uncompleted_tasks

class TestShowTasks(unittest.TestCase):
    def test_get_tasks_split(self):
        print("Testing get_tasks() function with split between completed and uncompleted.")
        task_id_1 = add_task("Görev 1")
        task_id_2 = add_task("Görev 2")
        print(f"Added tasks with IDs: {task_id_1}, {task_id_2}")

        print(f"Marking task ID {task_id_1} as completed.")
        complete_task(task_id_1)

        completed = get_completed_tasks()
        uncompleted = get_uncompleted_tasks()
        completed_ids = [task[0] for task in completed]
        uncompleted_ids = [task[0] for task in uncompleted]

        if task_id_1 in completed_ids and task_id_2 in uncompleted_ids:
            print("✅ Test passed: Tasks correctly split.")
        else:
            print("❌ Test failed: Task split incorrect.")
        self.assertIn(task_id_1, completed_ids)
        self.assertIn(task_id_2, uncompleted_ids)

if __name__ == '__main__':
    unittest.main()
