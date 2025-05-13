import unittest
from database import add_task, delete_task, get_tasks

class TestDeleteTask(unittest.TestCase):
    def test_delete_existing_task(self):
        print("Testing delete_task() function.")
        task_id = add_task("Silinecek görev")
        print(f"Added task with ID: {task_id}")
        
        print(f"Trying to delete task ID {task_id}")
        deleted = delete_task(task_id)
        print("Fetching tasks from database.")
        task_ids = [task[0] for task in get_tasks()]

        if deleted and task_id not in task_ids:
            print("✅ Test passed: Task deleted successfully.")
        else:
            print("❌ Test failed: Task still exists or delete failed.")
        self.assertTrue(deleted)
        self.assertNotIn(task_id, task_ids)

if __name__ == '__main__':
    unittest.main()
