#---------------
#Created by 1702638
#---------------
from unittest import TestCase
import cv2, numpy
from ce316ass import *


class Test_ce316(TestCase):
    def test_display_result(self):
        result = []
        result2 = []
        temp1 = [433, 308]
        temp2 = [320, 256]
        result2.append(temp1)
        result2.append(temp2)
        self.assertEqual(check_if_empty(result), True)
        self.assertEqual(check_if_empty(result2), False)

    def test_print_statement(self):
        frame = 0
        red_distance = 120000000
        green_distance = 121000000
        blue_distance = 122000000
        yellow_distance = 123000000
        orange_distance = 124000000
        aqua_distance = 125000000
        white_distance = 126000000
        self.assertEqual(display_result(frame, red_distance, green_distance,
                                        blue_distance, yellow_distance,
                                        orange_distance, aqua_distance,
                                        white_distance), None)

    def test_get_X_left(self):
        self.assertEqual(get_X_left((200 * (10 ** (-6))), 120000000), 3599.98)

    def test_get_distance(self):
        fn_left = r".\left-045.png"
        fn_right = r".\right-045.png"
        self.assertEqual(get_distance(422, 262, cv2.imread(fn_left),
                                      cv2.imread(fn_right)), 26250000)

    def test_get_mid(self):
        fn_left = r".\left-045.png"
        result = [[[[319, 211]], [[319, 212]], [[320, 212]], [[320, 211]]]]
        self.assertEqual(get_mid(result,cv2.imread(fn_left)),(319, 211))

