from unittest import TestCase
import unittest
from Report import getNumberFromFieldVaule


class TestGetNumberFromFieldVaule(TestCase):

    def test_emptyField(self):
        fieldValue = ""
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, 0)

    def test_noNumberInField(self):
        fieldValue = "Analiza poprawna :)"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, 0)

    def test_onlyIntegerInField(self):
        fieldValue = "3"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, 3)

    def test_onlyFloatWithDotInField(self):
        fieldValue = "3.4"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, 3.4)

    def test_onlyFloatWithCommaInField(self):
        fieldValue = "3,4"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, 3.4)

    def test_negativeIntegerWithoutBrackets(self):
        fieldValue = "-1"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, -1)

    def test_negativeFloatWithoutBrackets(self):
        fieldValue = "-1.4"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, -1.4)

    def test_negativeIntegerWithBrackets(self):
        fieldValue = "Optymalnie (-1 pkt.)"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, -1)

    def test_negativeFloatWithBrackets(self):
        fieldValue = "Optymalnie (-1.5 pkt.)"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, -1.5)

    def test_integerNumberInBrackets(self):
        fieldValue = "Istnieje i jest poprawna (2 pkt.)"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, 2)

    def test_floatNumberInBrackets(self):
        fieldValue = "Istnieje i jest poprawna (2.4 pkt.)"
        returnValue = getNumberFromFieldVaule(fieldValue)
        self.assertEqual(returnValue, 2.4)


if __name__ == '__main__':
    unittest.main()