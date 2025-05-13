import unittest
from database import add_task, complete_task, get_completed_tasks

class TestCompleteTask(unittest.TestCase):
    def test_complete_task(self):
        print("Testing complete_task() function.")
        task_id = add_task("Tamamlanacak görev")
        print(f"Added task with ID: {task_id}")

        print("Marking task as completed.")
        result = complete_task(task_id)

        completed_ids = [task[0] for task in get_completed_tasks()]
        if result and task_id in completed_ids:
            print("✅ Test passed: Task marked as completed.")
        else:
            print("❌ Test failed: Task was not marked as completed.")
        self.assertTrue(result)
        self.assertIn(task_id, completed_ids)

if __name__ == '__main__':
    unittest.main()
