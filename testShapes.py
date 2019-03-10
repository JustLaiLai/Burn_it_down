import math
import logging
import unittest
from Shapes import Square, Triangle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestArea(unittest.TestCase):

    def setUp(self):
        logger.info('setting up test')
        self.x = Square(3,8)
        self.y = Triangle(3,8)
        
    def test_result(self):
        logger.info('verifying square area')
        self.assertEqual(self.x.area(),64)

    def test_result_type(self):
        logger.info('verifying triangle area')
        self.assertTrue(type(self.y.area())==float)
        self.assertFalse(type(self.y.area())==int)

    @unittest.skip("because I can")
    def test_meh(self):
        self.fail("no way hosay")

    def tearDown(self):
        logger.info('test well done, poorly written')
        pass

if __name__=='__main__':
    unittest.main()
