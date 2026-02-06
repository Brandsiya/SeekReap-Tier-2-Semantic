from pure_functions import *
import unittest

class TestTier1(unittest.TestCase):
    def test_create_seeker(self):
        seeker = create_seeker()
        self.assertEqual(seeker.status, "active")
        self.assertIsInstance(seeker.id, str)

    def test_create_reap(self):
        seeker = create_seeker()
        reap = create_reap(seeker.id)
        self.assertEqual(reap.status, "pending")

if __name__ == "__main__":
    unittest.main()
