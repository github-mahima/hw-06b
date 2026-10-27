# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""


# -*- coding: utf-8 -*-
"""
SSW 567 - HW-06b
Triangle Classification Unit Tests
"""

import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    # Equilateral triangles
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    # Isoceles triangles
    def testIsocelesA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles')

    def testIsocelesB(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles')

    def testIsocelesC(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')

    # Scalene triangle
    def testScalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    # Right triangles
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right')

    # Invalid triangles
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 2, 4), 'NotATriangle')

    # Invalid inputs
    def testZeroSide(self):
        self.assertEqual(classifyTriangle(0, 5, 5), 'InvalidInput')

    def testNegativeSide(self):
        self.assertEqual(classifyTriangle(-1, 5, 5), 'InvalidInput')

    def testAboveMaximum(self):
        self.assertEqual(classifyTriangle(201, 5, 5), 'InvalidInput')

    def testNonInteger(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

    # Maximum valid boundary
    def testMaximumValid(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')
    def testZeroSideB(self):
        self.assertEqual(classifyTriangle(5, 0, 5), 'InvalidInput')

    def testZeroSideC(self):
        self.assertEqual(classifyTriangle(5, 5, 0), 'InvalidInput')
    def testStringInput(self):
        self.assertEqual(classifyTriangle("3", 4, 5), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

