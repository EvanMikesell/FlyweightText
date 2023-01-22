import unittest
from flyweights import *
from runarray import RunArray


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.__character_factory = CharacterFactory()
        self.__font_factory = FontFactory()
        self.__run_array = RunArray()
        self.__bold_font = self.__font_factory.get_flyweight(
            ("Times New Roman", 5, 'bold'))
        self.__italics_font = self.__font_factory.get_flyweight(
            ("Calibri", 11, 'italic'))

    def test_get_unicode(self):
        test_character = self.__character_factory.get_flyweight('A')
        unicode = test_character.get_unicode()
        self.assertEqual(unicode, ord('A'))

    def test_add_run(self):
        self.__run_array.add_run(0, 50, self.__bold_font)
        retrieved_font = self.__run_array.get(25)
        self.assertEqual(self.__bold_font, retrieved_font)

    def test_runarray_get(self):
        self.__run_array.add_run(0, 50, self.__bold_font)
        self.__run_array.add_run(25, 75, self.__italics_font)
        retrieved_font = self.__run_array.get(30)
        self.assertEqual(self.__italics_font, retrieved_font)

    def test_runarray_get_font_out_of_range(self):
        self.__run_array.add_run(0, 50, self.__bold_font)
        self.assertRaises(IndexError, self.__run_array.get, 100)

    def test_append_run(self):
        self.__run_array.add_run(0, 100, self.__bold_font)
        self.__run_array.append_run(20, self.__italics_font)
        self.assertEqual(self.__run_array.get(110), self.__italics_font)

    def test_font_factory_singleton(self):
        self.assertEqual(self.__font_factory, FontFactory())

    def test_character_factory_singleton(self):
        self.assertEqual(self.__character_factory, CharacterFactory())


if __name__ == '__main__':
    unittest.main()
