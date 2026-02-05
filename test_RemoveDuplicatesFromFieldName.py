from unittest import TestCase
import unittest
from Report import remove_duplicates


class TestGetNumberFromFieldVaule(TestCase):

    def test_Integer(self):
        fieldValue = 1
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual(returnValue, 1)

    def test_Float(self):
        fieldValue = 1.3
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual(returnValue, 1.3)

    def test_emptyField(self):
        fieldValue = ""
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual(returnValue, "")

    def test_NoDuplicate(self):
        fieldValue = "Jednostka"
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual(returnValue, "Jednostka")

    def test_DuplicateOne(self):
        fieldValue = \
        """Obrzędowość
(Nazwa kręgu, rocznice, procedura przyjęcia, barwy itp. )
Obrzędowość
(Nazwa kręgu, rocznice, procedura przyjęcia, barwy itp. )"""
        returnValue = remove_duplicates(fieldValue)
        correctValue = """Obrzędowość
(Nazwa kręgu, rocznice, procedura przyjęcia, barwy itp. )"""
        self.assertEqual(returnValue, correctValue)

    def test_DuplicateTwo(self):
        fieldValue = \
            """Dodatkowe informacje
(Możliwość przyznania dodatkowych punktów za inne informacje zawarte w charakterystyce, np. HAL, HAZ, sprzęt lub elementy wymagające wyróżnienia i nagrodzenia. W uwagach napi...Dodatkowe informacje
(Możliwość przyznania dodatkowych punktów za inne informacje zawarte w charakterystyce, np. HAL, HAZ, sprzęt lub elementy wymagające wyróżnienia i nagrodzenia. W uwagach napi..."""
        returnValue = remove_duplicates(fieldValue)
        correctValue = """Dodatkowe informacje
(Możliwość przyznania dodatkowych punktów za inne informacje zawarte w charakterystyce, np. HAL, HAZ, sprzęt lub elementy wymagające wyróżnienia i nagrodzenia. W uwagach napi..."""
        self.assertEqual(returnValue, correctValue)

    def test_DuplicateSix(self):
        fieldValue = \
            """Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)"""
        returnValue = remove_duplicates(fieldValue)
        correctValue = """Czy program zawiera stronę tytułową? 
(Zaznaczamy tak, gdy ze strony tytułowej jasno wynika, dla której jednostki jest on stworzony i na jaki rok harcerski.)"""
        self.assertEqual(returnValue, correctValue)

    def test_DuplicateNoDuplicatesInText(self):
        fieldValue = """Stwarzanie warunków do intelektualnego rozwoju człowieka.;Kształtowanie ludzi dzielnych i zaradnych.;Stwarzanie warunków do społecznego rozwoju człowieka.;Kreowanie aktywnych członków wspólnot.;Zachęcanie do brania odpowiedzialności za własne decyzje, działania, własny rozwój.;Upowszechnianie wiedzy o świecie przyrody, przeciwstawianie się jego niszczeniu przez cywilizację, kształtowanie potrzeby kontaktu z nieskażoną przyrodą.;"""
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual(returnValue, fieldValue)

    def test_DuplicateNoDuplicatesInTextEasy(self):
        fieldValue = "Siala baba mak. Nie wiedziala jak. Siala baba kartofle."
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual(returnValue, fieldValue)

    def test_DuplicateFiveTimesEasy(self):
        fieldValue = "Siala baba mak.\nSiala baba mak.\nSiala baba mak."
        returnValue = remove_duplicates(fieldValue)
        correctValue = "Siala baba mak."
        self.assertEqual(returnValue, correctValue)

    def test_9Szczep(self):
        fieldValue = """Stwarzanie warunków do intelektualnego rozwoju człowieka.;Zachęcanie do brania odpowiedzialności za własne decyzje, działania, własny rozwój.;Kreowanie aktywnych członków wspólnot.;Wspieranie podopiecznych w dążeniu do prawości, uczciwości i życia zgodnie z zasadami.;Promowanie postawy człowieka uczącego się, czyli gotowego do zmian.;Kształtowanie ludzi dzielnych i zaradnych.;Stwarzanie warunków do społecznego rozwoju człowieka.;Stwarzanie warunków do duchowego rozwoju człowieka.;Stwarzanie warunków do fizycznego rozwoju człowieka.;Upowszechnianie i umacnianie w społeczeństwie przywiązania do przyjaźni.;Kształtowanie postaw patriotycznych.;"""
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual(returnValue, fieldValue)

    def test_tak(self):
        fieldValue = "Tak"
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual("tak", returnValue)

    def test_nieDot(self):
        fieldValue = "nie."
        returnValue = remove_duplicates(fieldValue)
        self.assertEqual("nie.", returnValue)

if __name__ == '__main__':
    unittest.main()