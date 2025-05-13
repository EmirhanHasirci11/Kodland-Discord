import os
import unittest
from database import init_database

def run_all_tests():
    init_database()  
   
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

if __name__ == '__main__':
    run_all_tests()
