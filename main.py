import unittest

class RunUnitTest:
    def run():
        suite = unittest.defaultTestLoader.discover(
            "./Tests", pattern=f"test_*.py"
        )
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)

if __name__ == "__main__":
    RunUnitTest.run()