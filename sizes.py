"""
File to compare flyweight character/font size to non-flyweight size
"""

from flyweights import *
from runarray import RunArray

# objsize allows for size calculation of objects and their fields
import objsize


class CharacterWithFont:
    """
    For testing purposes, we store the character and font information together
    """

    def __init__(self, letter: str, font_info):
        self.__unicode = ord(letter)
        self.__font = tkinter.font.Font(font=font_info)


sample_text = "CS 635 Advanced Object-Oriented Design & Programming " \
              "Fall Semester, 2018 Doc 17 Mediator, Flyweight, Facade, " \
              "Demeter, Active Object Nov 19, 2019 " \
              "Copyright ©, All rights reserved. " \
              "2019 SDSU & Roger Whitney, 5500 Campanile Drive, San Diego, " \
              "CA 92182-7700 USA. OpenContent " \
              "(http://www.opencontent.org/opl.shtml) " \
              "license defines the copyright on this document."


char_factory = CharacterFactory()
font_factory = FontFactory()
font_run_array = RunArray()
text_with_flyweights = list()
text_with_characters_and_font = list()

bold_font = font_factory.get_flyweight(('Calibri', 11, 'bold'))
normal_font = font_factory.get_flyweight(('Calibri', 11, 'normal'))

# first 144 characters are bold
font_run_array.add_run(0, 144, bold_font)
font_run_array.append_run(212, normal_font)

for char in sample_text:
    text_with_flyweights.append(char_factory.get_flyweight(char))
    text_with_characters_and_font.append(
        CharacterWithFont(char, ("Calibri", 11, "normal")))


"""
To avoid double counting the flyweights in the factory and list, 
we use exclusive deep size
"""

flyweights_size = objsize.get_exclusive_deep_size(char_factory, text_with_flyweights,
                                                  font_factory, font_run_array)

no_flyweights_size = objsize.get_deep_size(text_with_characters_and_font)

"""
Sizes:
    Flyweights: 14832 Bytes
    No Flyweights: 132952 Bytes
"""
