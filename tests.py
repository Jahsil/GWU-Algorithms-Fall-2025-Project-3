import unittest
from main import (   
    generateRotations,
    isStakableOnTop,
    calculateMaximumHeight,
    generateLargeNumberOfBoxes
)


class TestBoxStacking(unittest.TestCase):

    def testRotations(self):
        h, w, d = 4, 6, 7
        rotations = generateRotations(h, w, d)
        self.assertEqual(len(rotations), 3)
        self.assertIn((7, 6, 4), rotations)
        self.assertIn((7, 4, 6), rotations)
        self.assertIn((6, 4, 7), rotations)

    def testStackability(self):
        bottom = (10, 8, 5)
        top_good = (9, 7, 4)
        top_bad = (10, 8, 2)
        self.assertTrue(isStakableOnTop(bottom, top_good))
        self.assertFalse(isStakableOnTop(bottom, top_bad))

    def testEmpty(self):
        height, stack = calculateMaximumHeight([])
        self.assertEqual(height, 0)
        self.assertEqual(stack, [])

    def testEasyExample(self):
        boxes = [(4, 6, 7)]
        height, stack = calculateMaximumHeight(boxes)
        self.assertEqual(height, 7)
        self.assertEqual(len(stack), 1)

    def testAnotherEasyExample(self):
        boxes = [(1, 2, 3), (4, 5, 6)]
        height, _ = calculateMaximumHeight(boxes)
        self.assertEqual(height, 14)

    def testLargeRandomInput(self):
        N = 5000
        boxes = generateLargeNumberOfBoxes(N)
        self.assertEqual(len(boxes), N)
        height, stack = calculateMaximumHeight(boxes)
        self.assertTrue(len(stack) <= 3 * N)
        self.assertTrue(height >= 0)


if __name__ == "__main__":
    unittest.main()
