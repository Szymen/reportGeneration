from unittest import TestCase
import unittest



def removeDuplicates(fieldName: str) -> str:
    if type(fieldName) != str:
        return fieldName

    if len(fieldName) < 5 or fieldName == "":
        return ""

    if fieldName.count( fieldName[0:4] ) == 1:
        return fieldName

    substring_len = 4
    while fieldName.count( fieldName[0:substring_len] ) > 1:
        substring_len += 1
        if fieldName.count( fieldName[0:substring_len] ) * substring_len == len(fieldName):
            # multiple ocurrences of same string
            substring_len += 1
            break

    # print("<><>")
    # print(fieldName[0:substring_len-1])
    # print("<><>")
    return fieldName[0:substring_len-1]


class TestGetNumberFromFieldVaule(TestCase):

    def test_Integer(self):
        fieldValue = 1
        returnValue = removeDuplicates(fieldValue)
        self.assertEqual(returnValue, 1)

    def test_Float(self):
        fieldValue = 1.3
        returnValue = removeDuplicates(fieldValue)
        self.assertEqual(returnValue, 1.3)

    def test_emptyField(self):
        fieldValue = ""
        returnValue = removeDuplicates(fieldValue)
        self.assertEqual(returnValue, "")

    def test_NoDuplicate(self):
        fieldValue = "Jednostka"
        returnValue = removeDuplicates(fieldValue)
        self.assertEqual(returnValue, "Jednostka")

    def test_DuplicateOne(self):
        fieldValue = \
        """Obrzędowość
(Nazwa kręgu, rocznice, procedura przyjęcia, barwy itp. )
Obrzędowość
(Nazwa kręgu, rocznice, procedura przyjęcia, barwy itp. )"""
        returnValue = removeDuplicates(fieldValue)
        correctValue = """Obrzędowość
(Nazwa kręgu, rocznice, procedura przyjęcia, barwy itp. )"""
        self.assertEqual(returnValue.strip(), correctValue.strip())

    def test_DuplicateTwo(self):
        fieldValue = \
            """Dodatkowe informacje
(Możliwość przyznania dodatkowych punktów za inne informacje zawarte w charakterystyce, np. HAL, HAZ, sprzęt lub elementy wymagające wyróżnienia i nagrodzenia. W uwagach napi...Dodatkowe informacje
(Możliwość przyznania dodatkowych punktów za inne informacje zawarte w charakterystyce, np. HAL, HAZ, sprzęt lub elementy wymagające wyróżnienia i nagrodzenia. W uwagach napi..."""
        returnValue = removeDuplicates(fieldValue)
        correctValue = """Dodatkowe informacje
(Możliwość przyznania dodatkowych punktów za inne informacje zawarte w charakterystyce, np. HAL, HAZ, sprzęt lub elementy wymagające wyróżnienia i nagrodzenia. W uwagach napi..."""
        self.assertEqual(returnValue.strip(), correctValue.strip())

    def test_DuplicateSix(self):
        fieldValue = \
            """Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)"""
        returnValue = removeDuplicates(fieldValue)
        correctValue = """Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)"""
        self.assertEqual(returnValue.strip(), correctValue.strip())



if __name__ == '__main__':
    unittest.main()