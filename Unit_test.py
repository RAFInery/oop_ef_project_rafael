import unittest

def function_one(x):
	return x + 3

class Lets_Test(unittest.TestCase):
	
	
	def test_one(self):
		self.assertEqual(function_one(1), 2)

if __name__ == "__main__":
	unittest.main()
	

